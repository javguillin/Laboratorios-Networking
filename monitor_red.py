import os
import platform
import subprocess

def check_ping(host):
    # Comando para ping (ajusta segun el sistema, en Linux es -c)
    param = '-c' if platform.system().lower() != 'windows' else '-n'
    command = ['ping', param, '1', host]
    
    print(f"Probando conexión con {host}...")
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

print("--- DIAGNÓSTICO DE RED ---")
destinos = ["8.8.8.8", "google.com", "github.com"]

for site in destinos:
    if check_ping(site):
        print(f"✅ {site} está ALCANZABLE")
    else:
        print(f"❌ {site} está CAÍDO o no hay respuesta")

print("--------------------------")
