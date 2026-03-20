echo "--- REPORTE DE SALUD DE JAVIER ---"
date
echo "Espacio en disco:"
df -h | grep "/$"
echo "Memoria RAM libre:"
free -h
echo "----------------------------------"
