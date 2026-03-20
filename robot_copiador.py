import shutil
import os

# Definimos las rutas
origen = os.path.expanduser("~/resumen_hoy.txt")
destino = "/mnt/c/Users/veroh/OneDrive/Desktop/Reporte_Automatico.txt"

try:
    shutil.copy(origen, destino)
    print("✅ ¡Robot: Archivo copiado al escritorio de Windows con éxito!")
except Exception as e:
    print(f"❌ Error del Robot: {e}")
