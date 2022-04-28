## API REST FLASK Gestion Immobiliere

API REST FLASK Gestion Immobiliere  using Flask, SQLAlchemy and the connecting Flask-SQLAlchemy library.


## Logical Data Model

![myimage-alt-tag](dbSchema\diagramme_logic.png)

### Installing Dependencies

```
pip install -r requirements.txt
```

### Edit informations Data Base

Edit first Data Base Host, Data Base User, Data Base Password, Data Base Name in `secrets.py`

```
$ python secrets.py
```

### Running the App

To run the microservice, first run the `server.py`

```
$ python server.py
```
Then :

Consume [http://127.0.0.1:5000/api/v1/propr] for operations propriétaire 

Consume (http://127.0.0.1:5000/api/v1/immobilier) for operations Bien Immobilier
