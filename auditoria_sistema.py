import os
import socket
import shutil

print("--- REPORTE DE SISTEMA LINUX ---")

# 1. Obtener el nombre del equipo
hostname = socket.gethostname()
print(f"Nombre del equipo: {hostname}")

# 2. Obtener la IP local
ip_local = socket.gethostbyname(hostname)
print(f"Dirección IP local: {ip_local}")

# 3. Revisar espacio en disco
total, used, free = shutil.disk_usage("/")
print(f"Espacio libre en disco: {free // (2**30)} GB")

print("--------------------------------")
print("Reporte generado con éxito.")
