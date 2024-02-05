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

IMPORTANTE: EN esta version hay que crear un directorio "db" en la raiz del proyecto, junto a los directorios: muy_data y my_icons. 

Instalacion del proyecto:

Este proyecto utiliza Python 3 en su totalidad, yo tengo instalada la version 3.10.12, vamos a suponer que el comando "py" es tu comando de ejecutar Python.

Te recomiendo crear un entorno virtual para trabajar con py -m venv test en el directorio de trabajo. No te olvides de activarla para trabajar, este comando depende de tu sistema operativo.Los comandos de git son independientes si el entorno esta activo o desactivo. Te recomiendo crear un directorio para instalar el proyecto y tener un entorno virtual e Python en el.

Se necesitara tener disponible git para instalar el presente proyecto en tu maquina personal:

Para ver que version de git esta instalada y ver si esta disponible en tu equipo ejecuta el siguente comando en una ventana de comandos de tu sistema operativo:

git --version

Si obtienes un error: ve a consultar los instaladores disponibles en GitHub y elige el que corresponda a tu sistema operativo, es simple y seguro. Una vez instalado repite el comando anterior, si la respuesta no es un error y es la version de git instalada, Felicitaciones!!, sigue el paso siguiente, en el directorio que escogiste, para el instalar el proyecto en tu maquina.

git clone https://github.com/moreyg/TP.git

Si no hay errores, esta copiado el proyecto en tu maquina y ahora hay que preparar Python, seguramente ya tienes un entorno virtual, recuerda activarlo para preparar el entorno virtual con los paquetes necesarios, asi no molestamos a la instalacion de Python de tu sistema operativo.

pip install -r requirement.txt

Si no tienes experiencia en esto, no te asustes, esta utilizando sitios y paquetes muy seguros del mismo Python.

Cuando termine podemos iniciar el sistema y correra sin errores:

py tp_main.py

Esto iniciara el systema, lo ver, Felicitaciones nuevamente!

Que tenemos ahi?

Una interfaz grafica para ver los valores finales de cotizaciones de critomonedas solicitadas al sitio COINAPI.

El primer paso es obtener una API-KEY, si no la tienes no podremos avanzar. La obtienes en el sitio https://www.coinapi.io/get-free-api-key solicitando una free key para MARKET DATA API, No te olvides de esta seleccion, recibiras la api key en ti correo en minutos.

Una vez recibida la API-KEY, en la plaicacion vas al menu File-Set Api Key y pegas la clave, le das OK y la key se guarda y no necesitas introducirla nunca mas, ya esta configurado tu sistema.

Ahora vas a ver que el indicador CANTIDAD DE SIMBOLOS, dice CERO (numero 0), esto es porque ahun no conectamos a la API para traer informacion. Para traer informacion utilizamos el boton GET SYMBOLS INFO. Este boton solicita a la API os simbolos y puede ser via un filtro en el nombre de los simbolos. Traer todos puede tardar cinco munitos o un poco mas, son mas de 500.000 simbolos. Si ya esta configurada la API-KEY solicita los simbolos sin problema. Cuando termine, puede quedar la ventana sin responder por cinco minutos o mas (ya que no llegue a implemanter threads), veras que CANTIDAD DE SIMBOLOS cambio de numero. Ademas los simbilos disponibles se listan en el boton pull down que se encuentra arriba de esa leyenda, mostrando el nobre del primer symbolo traido. El pull down muestra e a 20, para cambiar a los siguientes 20 tienes el boton SIGUIENTE PAGINA un poco mas arriba en la interfaz del sistema, el otro boton: PAGINA ANTERIOR traera los 20 anteriores una vez que hayas avanzado para ver los diferentes nombres.
Arriba, abajo del menu, tienes una ventana de texto con la leyenda : Escribir symbol para filtrado
Lo que tipees aca filtrara el contenido del pulldown, si buscas Bitcoin, seria BTC o btc, se filtrara todo lo que contenca ese string, USD o usd, lo mismo. Te dejo una lista de nobmres validos:

BINANCE_SPOT_ETH_BT
BINANCE_SPOT_ETH_USDT

Si llegamos aca estamos mas que bien,

Ahora solicitaremos a la API informacion de vaores sobre un simbolo, por ejemplo uno de los anteriores. Como ves el boton SOLICITAR DATA DE SYMBOL ELEJIDO esta desactivado ya que necesitamos datos de fecha de inicio, fecha de fin , espacio temporal entre valores para solicitar esta informacion.
Para esto dejamos en el pulldown el simbolo elejido, elejimos la fecha de inicio con la flechita de fecha de la izquierda, repetimos para la fecha de fin. El orden fisico en la pantalla es: La leyenda esta arriba y el seleccionador correspondiente de fecha esta abajo. No importe el orden que elijas los valores, al elejir las dos el boton SOLICITAR DATA DE SYMBOL ELEJIDO se activara. Ya lo puedes utilizar. Esto consulta a la API las cotizaciones, si la ventana no responde es porque tarda unos segundos la respuesta de la API, nuevamente, esto es debido a que no utilize threads por tiempo, si lo agregas, por favor comparte el codigo.

Como vemos los valores?????

Hay dos formas, una mediante una tabla vintage en la misma ventana que ejecutaste el sistema, y a otra en una ventana tipo Window de tu sistema operativo. Para esto tenemos dos menues:
TablaVintege y Grafico. En ambos menues vas a ver las funciones de ADD_SYMBOL, esto es para agregar el simbolo en la tabla o en los graficos a mostrar, REM_SYMBOL saca de la tabla el simbolo a mostrar.

Como le digo que simbolo agrego o que simbolo saco de los reportes a mostrar???

Estas funciones descriptas trabajan con el simbolo seleccionado, que es el que muestra el pull down de los simblos disponibles, tambien lo ves en el indicador SYMBOL debajo del indicador CANTIDAD DE SIMBOLOS, dedajo del pull down de los symbolos (o simbolos) disponibles. El mismo selector que utllizamos para solicitar informacion especifica y que podemos afinar con el filtro!!
ya agregue los simbolos (puede ser uno solo), o ninguno, con la funcion SHOW TABLA del menu TABLAVINTAGE, veras la tabla, por ejemplo:

Eje X | BINANCE_SPOT_BTC_USDT | BINANCE_SPOT_BTC_NGN
----------------------------------------------------
2020-01-01T00:00:00.0000000Z | 28923.63 |  0
2020-11-01T00:00:00.0000000Z | 19695.87 |  9750282
2020-12-01T00:00:00.0000000Z | 28923.63 |  13637011
2021-01-01T00:00:00.0000000Z | 46216.93 |  16140003
2021-02-01T00:00:00.0000000Z | 45135.66 |  22527662
2021-03-01T00:00:00.0000000Z | 58740.55 |  30087323
2021-04-01T00:00:00.0000000Z | 57694.27 |  35173547
2021-05-01T00:00:00.0000000Z | 37253.81 |  33808227
2021-06-01T00:00:00.0000000Z | 35045    |  33364445
2021-07-01T00:00:00.0000000Z | 41461.83 |  21723236
2021-08-01T00:00:00.0000000Z | 47123.51 |  25726405
2021-09-01T00:00:00.0000000Z | 43824.1  |  26443932
2021-10-01T00:00:00.0000000Z | 61299.8  |  34417975
2022-01-01T00:00:00.0000000Z | 16542.4  |  0
2023-01-01T00:00:00.0000000Z | 42283.58 |  0
2023-06-01T00:00:00.0000000Z | 0        |  23419540
2023-07-01T00:00:00.0000000Z | 0        |  25296902
2023-08-01T00:00:00.0000000Z | 0        |  23589177
2023-09-01T00:00:00.0000000Z | 0        |  26388878
2023-10-01T00:00:00.0000000Z | 0        |  39498613
2023-11-01T00:00:00.0000000Z | 0        |  43835373
2023-12-01T00:00:00.0000000Z | 0        |  50364475




Y COMO VEO EL GRAFICO????

Eso lo dejo como un acertijo a resolver.

Te recomiendo cerrar los graficos antes de solicitar que te los muestre el menu correspondiente, esta version, te muestra todos los graficos disponibles,


Cualquier error, avisame a gmorey@gmail.com por favor, es mi primer sistema en Python y fue muy duro, quedo codigo que tengo que eliminar, objetos que no se utilizan, funciones que no se utilizan, la TablaVintaje y el Grafico pueden ser objetos de una clase abstracta REPORTE(ABC) donde TablaVintage(REPORTE) y Grafico(REPORTE) hereden funciones comunes, pero eso sera en otro momento. No esta desarrollado para ASSETS ni para EXCHANGE, solo consultamos la parte SYMBOLS de la API ya que la consigna fue consultar+guardar+mostrar info de API. Mi extra fue darle una interfaz grafica amigable, Espero que te guste y si no puedes cambiarlo como te parezca mejor para tus necesidades. Tiene mucho para corregir, lo hare con tiempo.


Saludos, espero que te guste

