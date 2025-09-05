
# Renombrador de logs — Marco Vivanco

## ¿Qué incluye este ZIP?
- `renombra_logs_marco_vivanco.py`: Script Python para renombrar archivos `.log`.
- `logs/`: Carpeta de ejemplo con archivos `.log` de prueba.
- `README.md`: Este archivo con instrucciones.

## ¿Dónde colocar la carpeta?
Colocar la carpeta en donde se prefiera. Ejemplo recomendado:
```
C:\xampp\htdocs\PROCESOS_INFORMATICOS\renombrador_logs\
```

Dentro de esa carpeta deberías tener:
```
renombra_logs_marco_vivanco.py
logs\
README.md
```

## Cómo usar
1. Abrir Visual Studio Code y abrir la carpeta donde se encuentran los archivos.
2. Abrir la terminal integrada (Ctrl+ñ).
3. Ejecutar primero en modo simulación:
   ```bash
   python renombra_logs_marco_vivanco.py -p "logs" --dry-run
   ```
   Esto mostrará cómo se renombrarán los archivos sin cambiarlos.

4. Para renombrar de verdad:
   ```bash
   python renombra_logs_marco_vivanco.py -p "logs"
   ```

## Nota
- El parámetro `-p` debe ser la carpeta donde están los `.log`.
- En el ejemplo incluí la carpeta `logs` con archivos de prueba (`test1.log`, `test2.log`, ...).
