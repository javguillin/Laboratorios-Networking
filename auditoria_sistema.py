import os
import socket
import shutil
from datetime import datetime

# Configuración del nombre del archivo con la fecha de hoy
fecha_hoy = datetime.now().strftime("%Y-%m-%d_%H-%M")
nombre_archivo = f"reporte_{fecha_hoy}.txt"

reporte = []
reporte.append("--- REPORTE DE SISTEMA LINUX ---")
reporte.append(f"Fecha y Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
reporte.append(f"Nombre del equipo: {socket.gethostname()}")
reporte.append(f"Dirección IP local: {socket.gethostbyname(socket.gethostname())}")

total, used, free = shutil.disk_usage("/")
reporte.append(f"Espacio libre en disco: {free // (2**30)} GB")
reporte.append("--------------------------------")

# Guardar en el archivo
with open(nombre_archivo, "w") as f:
    f.write("\n".join(reporte))

print(f"✅ Reporte generado y guardado como: {nombre_archivo}")
