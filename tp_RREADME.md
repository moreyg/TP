# **Trabajo final : Especializacion Python ITBA**

## **Objetivo**

Realizar interfaz de usuario para analizar informacion recolectada via API a sitios que almacenan y comparten datos actuales y/o historicos. La informacion recolectada debe ser almacenada en base de datos. El usuario solicitara la informacion requerida y sus parametros. La informacion se mostrara al usuario via, ventana de informacion, una lista de datos o un grafico para su analisis, segun se solicite o corresponda.

## **Recursos analizados de fuentes de Datos**

Existe una lista interminable de sitios con informacion disponible, seleccionamos las siguientes opciones para su evaluacion:

(Recuerde "boton derecho - Abrir en una ventna/pestaña nueva", para no perder de vista este documento)

  [nASA](https://api.nasa.gov/#browseAPI) | [cOVID](https://covidtracking.com/data/api/version-2) | [cOIN_aPI](https://docs.coinapi.io) | [cOINgCEKO](https://www.coingecko.com/api/documentation)

Trabajaremos con CoinApi y CoinGecko,

Estructura a utilizar:

project_root/
|-- my_data/
|   |-- __init__.py
|   |
|   |-- my_requests/
|   |-- __init__.py
|   |-- requests_class.py
|   |
|   |-- my_database/
|   	|-- __init__.py
|   	|
|   	|-- my_firebase/
|   	|   |-- __init__.py
|   	|   |-- firebase_class.py
|   	|
|   	|-- my_sqlite/
|           |-- __init__.py
|           |-- sqlite_class.py
|
|-- my_matplotlib/
|   |-- __init__.py
|   |-- matplotlib_class.py
|
|
|-- my_gui/
|   |-- __init__.py
|   |-- PyQt_module.py
|
|-- scripts/
|   |-- __init__.py
|   |-- script1.py
|   |-- script2.py
|
|-- venv/
|   |-- (your virtual environment files)
|
|-- requirements.txt
|-- main.py
|-- README.md


project_root/: This is the root directory of your project.

my_data/: A directory for handling data-related operations.

my_requests/: Contains requests_class.py, likely for handling API requests.

my_database/: For database-related functionality.

my_firebase/: Contains firebase_class.py, for interacting with Firebase.

my_sqlite/: Contains sqlite_class.py, SQLite database operations.

my_matplotlib/: Contains matplotlib_class.py, for data plotting using Matplotlib.

my_gui/: Contains PyQt_module.py, which a GUI created using PyQt.

scripts/: Contains individual scripts.

venv/: The Python virtual environment directory.

requirements.txt: Lists the dependencies for the project.

main.py: The main entry point for your application.

README.md:this file


Workflow

Fetch Data:
Make an API request and receive data as a dictionary or list of dictionaries.

Process Data:
Perform any necessary data processing or transformation.

Store/Retrieve Data:
Save the processed data to your database and retrieve it as needed.

Display in GUI:
Show the data on the GUI, allowing the user to interact with it, such as displaying it in a table or generating plots based on it.

Plot Data:
Use Matplotlib to create visualizations from the data. You can then integrate these plots into your PyQt GUI.

Handling Data from APIs
When fetching data from an API:

The response is often in JSON format, which can be directly converted to a Python dictionary using response.json() if you're using the requests library.
If the API returns an array of items, it will be converted to a list of dictionaries in Python.
Storing and Retrieving Data from Databases
For databases like Firebase or SQLite:

When storing data, you can directly store Python dictionaries. Both Firebase and SQLite can handle dictionary-like structures (although SQLite will require some serialization for complex structures).
Retrieving data from the database will also give you dictionaries or lists of dictionaries, depending on the query and structure of your database.
Using Data in Plots
With Matplotlib:

Data for plotting can be easily managed if they are in dictionary or list format. For example, you can use dictionary keys as labels and values as data points.
Integrating with GUI
In a PyQt GUI:

You can display the data in various GUI elements. For instance, you could use a QTableWidget to display a list of dictionaries (each dictionary representing a row and its key-value pairs representing column data).


<<<<<<< HEAD
=======
Esta etapa se concentra en analizar al menos dos tipos de bases de datos, SQLite, integrada a Python utilizado y una dase de datos externa FireBase.

sopn dos tipos de DB totalmente diferentes, SQLite es relacional y estructurada, un modelo reducido de base SQL, pero perfectamente funcional para iniciar un proyecto y luego implementar ota db SQL, mientras que Firebase es una base de datos no relacional y no SQL, es una DB basada en jerarquias, con formato JSON. RealTime DB y FireStore DB son dos productos ofresidos online. Escapa a este proyecto ahondar en las direrencias de estos productos especificos de FireBase.
>>>>>>> f89a51bf069ba0b0c96fe4b3560dab965772d505
