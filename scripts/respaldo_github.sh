#!/bin/bash
# Ir a la carpeta principal
cd /home/javier/
# Agregar todos los cambios (scripts, reportes y docs)
git add .
# Hacer el commit con la fecha actual
git commit -m "Respaldo automático: $(date +'%Y-%m-%d %H:%M')"
# Empujar a la nube
git push origin master
