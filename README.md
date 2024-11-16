# prueba de cobertura o caja blanca:

Instalar la herramienta:
```bash
  pip install coverage
```
Ejecutar las pruebas con cobertura: Desde la terminal, en el directorio de tu proyecto, ejecuta:
```bash
  coverage run -m unittest nombre_del_archivo.py
```
Generar el informe de cobertura: Una vez que las pruebas se ejecuten, genera un informe en texto:
```bash
  coverage report
```
O genera un informe en HTML:
```bash  
  coverage html
```
Esto creará un archivo index.html en un directorio llamado htmlcov. Ábrelo en tu navegador para ver una visualización detallada.
