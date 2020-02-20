# Config

### Dependencias
* Instalar ```postgresql-12``` 
* Crear un entorno virtual con ```virtualenv venv```, si este comando
da error instalar ```virtualenv``` con ```pip install --user virtualenv```
* Activar el entorno virtual ```cmd venv/bin/activate.bat```
* Instalar dependencias (desde la raíz del repo) ```pip install -r requirements.txt```
* Usar la cli: ```python main.py run --with-migrations --with-fake-data```

#### Cadena de conexión
Debe tener el siguiente formato: 

    postgresql+psycopg2://user:password@host:port/dbname
    
Y estar especificada en la variable de entorno ```DATABASE_URL```.

### CLI

Existe una CLI ayudante, ejecutar ```python main.py```.