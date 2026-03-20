#!/bin/bash
DIR="/home/javier/bot2/laboratorio/Reporte_$(date +%Y-%m-%d)"
mkdir -p "$DIR"
echo "Reporte generado automáticamente el: $(date +"%H:%M:%S")" > "$DIR/notas.txt"
echo "Listo para trabajar, Javier." >> "$DIR/notas.txt"
