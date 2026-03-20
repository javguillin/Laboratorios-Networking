#!/bin/bash
LOG="/home/javier/reportes/errores_red.txt"
RESUMEN="/home/javier/reportes/resumen_diario.txt"

# Contar cuántas veces aparece "ALERTA" en el log
CAIDAS=$(grep -c "ALERTA" $LOG 2>/dev/null || echo 0)

echo "--- RESUMEN DE RED $(date +'%Y-%m-%d') ---" > $RESUMEN
echo "Total de fallos detectados: $CAIDAS" >> $RESUMEN
echo "---------------------------------------" >> $RESUMEN

# Limpiar el log para que no se acumule para mañana
> $LOG
