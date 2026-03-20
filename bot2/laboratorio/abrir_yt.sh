#!/bin/bash

echo "¿Qué quieres buscar en YouTube, Javier?"
read BUSQUEDA

# Esta línea usa comillas especiales para que Windows no se confunda con los espacios
powershell.exe -c "start \"https://www.youtube.com/results?search_query=$BUSQUEDA\""
