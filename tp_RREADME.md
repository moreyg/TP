# **Trabajo final : Especializacion Python ITBA**

## **Objetivo**

Realizar interfaz de usuario para analizar informacion recolectada via API a sitios que almacenan y comparten datos actuales y/o historicos. La informacion recolectada debe ser almacenada en base de datos. El usuario solicitara la informacion requerida y sus parametros. La informacion se mostrara al usuario via, ventana de informacion, una lista de datos o un grafico para su analisis, segun se solicite o corresponda.

## **Recursos analizados de fuentes de Datos**

Existe una lista interminable de sitios con informacion disponible, seleccionamos las siguientes opciones para su evaluacion:

(Recuerde "boton derecho - Abrir en una ventna/pestaña nueva", para no perder de vista este documento)

  [nASA](https://api.nasa.gov/#browseAPI) | [cOVID](https://covidtracking.com/data/api/version-2) | [cOIN_aPI](https://docs.coinapi.io) | [cOINgCEKO](https://www.coingecko.com/api/documentation)

Trabajaremos con CoinApi 

La direccion de github del proyecto es:


Es necesario obtener una API-KEY para utilizar el sistema, esta se obtiene solicitandola en el costado derecho superior de la pagina https://docs.coinapi.io/ que es la pagina de documentacion de la API a utilizar. una vez obtenida de configura mediante el menu File el valor de la KEY y luedo el sistema la recuerda 

Existen DOS alternativas primarias de APIs en el sitio, una para hacer negicios (PAGA) otra para solicitar informacion de indices, esta es parcialmente gratuita y esta bien documentada y con ejemplos provistos en la misma pagina. Vamos a utilizar la MARQUET DATA API en su version REST API gratuita.

Este sitio presenta tras tipos de indices (TIKERS) que son : SYMBOLS, EXCHANGES y ASSETS. Vamos a consultar los ID de los SYMBOLS y solicitaremos su cotizacion en un periodo determinado y mostraremos en tabla (vintage), y tambien en grafico tipo window, los valores de cierre de cotizacion de los dias solicitados.
En esta demo debemos acotar algunos parametros para poder tener un desarrollo acotado, vamos a solicitar 12 valores por request ya que la API solo nos permite 100 requests por dia Solicitaremos valores espaciados mensualmente.
Como base de datos se utiliza SQLITE en el directorio ./db si no existe se crea el archivo y la base necesaria, una vez que consultamos datos a la API, estos se graban en la base de datos yasi obtenemos persistencia de datos.
Definimos objetos SYMBOL que tienen tres variables, ID (str), INFO (str), DATA. La variable DATA es un objeto que contiene un SortedSet de otro objeto que se llama REGISTRO. Lo registros son las cotizaciones de cada SYMBOL, cuando solicitamos informacion de un determinado SYMBOL este conjunto de informacion recibido desde la API, via request, se suma (sin duplicar) a los registros existentes en DATA para el SYMBOL que corresponde.
La visualizacion entonces parte de obtener el objeto a analizar, solicitar los registos para el objeto, y asi armar los pares x,y para ver la informacion en formato tabla vintage DOS o bien en un una ventana.

Tanto la tabla vintage DOS, como en el grafico en ventada tienen las funcionalidades: de agregar un ID, remover un ID, mostrar tabla/graficos desde el menu correspondiente. Siempre trabajan con el objeto que corresponde.

Una vez que hayamos obtenido la API-KEY, y la configuramos mediante el menu File, hay dos pasos para solicitar informacion a la API, primero es traer los IDs disponibles para pedir cotizaciones, los nombres de los tikers. Eslo lo hacemos con la posibilidad de filtrar por nombre ya que son mas de 500.000 y puede tardar unos minutos. Con el filtro sugeridos vienen cerca de 200 elementos.
Una vez que tenemos los IDs podemos solicitar sus cotizaciones. El boton de solicitar informacion sobre in ID esta deshabilitado hasta que seleccionemos el ID, fecha de inicio de datos, fecha de fin de datos. Podemos solicitar datos mensuales o anuales en esta version por la limitacion diaria de pedidos del sitio.

Los paquetes necesarios son:

$ pip list

Package            Version
------------------ ----------
certifi            2023.11.17
charset-normalizer 3.3.2
contourpy          1.2.0
cycler             0.12.1
fonttools          4.47.2
idna               3.6
kiwisolver         1.4.5
matplotlib         3.8.2
numpy              1.26.3
packaging          23.2
pandas             2.2.0
pillow             10.2.0
pip                22.0.2
pyparsing          3.1.1
PyQt5              5.15.10
PyQt5-Qt5          5.15.2
PyQt5-sip          12.13.0
python-dateutil    2.8.2
pytz               2023.4
requests           2.31.0
setuptools         59.6.0
six                1.16.0
sortedcontainers   2.4.0
tzdata             2023.4
urllib3            2.2.0


