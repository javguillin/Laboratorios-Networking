import os
import datetime

# La IP que queremos vigilar (Google DNS)
ip_objetivo = "8.8.8.8"
ruta_web = "/var/www/html/index.html"

def check_red():
    # Hacemos un ping rápido
    response = os.system(f"ping -c 1 {ip_objetivo} > /dev/null 2>&1")
    
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if response == 0:
        estado = '<span style="color: #3fb950;">CONECTADO (OK)</span>'
        fondo = "#0d1117"
    else:
        estado = '<span style="color: #f85149;">DESCONECTADO (ERROR)</span>'
        fondo = "#3e1010" # Fondo rojizo si hay error

    # El nuevo contenido HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"><title>Monitor de Javier</title></head>
    <body style="background-color: {fondo}; color: white; text-align: center; font-family: sans-serif; padding-top: 50px;">
        <h1>DASHBOARD DE RED: JAVIER GUILLIN</h1>
        <div style="font-size: 1.5em; border: 2px solid #30363d; display: inline-block; padding: 20px; border-radius: 10px;">
            <p><strong>Última revisión:</strong> {ahora}</p>
            <p><strong>Estado de Internet:</strong> {estado}</p>
        </div>
        <p style="margin-top: 20px; color: #8b949e;">Monitoreando IP: {ip_objetivo}</p>
    </body>
    </html>
    """
    
    # Escribimos el archivo en la carpeta de Apache
    with open("temp_index.html", "w") as f:
        f.write(html_content)
    
    # Lo movemos con sudo para que Apache lo vea
    os.system(f"sudo cp temp_index.html {ruta_web}")

if __name__ == "__main__":
    check_red()
    print("¡Página web actualizada con el estado de red!")
