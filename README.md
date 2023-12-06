# **Trabajo final : Especializacion Python ITBA**

## **Objetivo**

Realizar interfaz de usuario para analizar informacion recolectada via API a sitios que almacenan y comparten datos actuales y/o historicos. La informacion recolectada debe ser almacenada en base de datos. El usuario solicitara la informacion requerida y sus parametros. La informacion se mostrara al usuario via, ventana de informacion, una lista de datos o un grafico para su analisis, segun se solicite o corresponda.

## **Recursos analizados de fuentes de Datos**

Existe una lista interminable de sitios con informacion disponible, seleccionamos las siguientes opciones para su evaluacion:

(Recuerde "boton derecho - Abrir en una ventna/pestaña nueva", para no perder de vista este documento)

  [nASA](https://api.nasa.gov/#browseAPI) | [cOVID](https://covidtracking.com/data/api/version-2) | [cOIN_aPI](https://docs.coinapi.io) | [cOINgCEKO](https://www.coingecko.com/api/documentation)

Trabajaremos con CoinApi y CoinGecko por ser muy claras en su documentacion

## **Etapa 1:**

Esta etapa tendra el objerivo de introduccion a Girhub como repositorio de proyecto utilizando SO Linux,y MarkDown como lenguaje de documentacion de las etapas del trabajo a entregar. Este documento no intenta ser una guia de estudio, ni exlicativa, sobre temas mencionados, este documento refleja etapas seguidas por el autor en el desarrollo de su conocimiento y recomienda a otros dividir los temas de esta manera para seguir un plan para adquirir conocimiento, e interpretacion, de los temas tratados.

Trabajaremos con el lenguaje Python 3.10 con la funcionalidad nativa de virtualizacion localmente, esto no sera reflejado en el repositorio. El sistema estara compuesto por scripts de Pyton para poder ser ejecutado via linea de comando, por ejemplo "run_linux_tp" o "run_Windows_tp", o bien simplemente "run_tp".

Se trabajara con requirementes.txt para notificar dependencias al utilizar el repositorio.

Se implementara una interfaz grafica del modo "ventana" para facilitar al usuario su utilizacion.

En esta primera etapa tiene los objetivos:
0- Incursionar el el lenguaje MarkDown de esta nota (Edit para ver como formatear..)
1- Recolectar diferente informacion mediante API disponibles ejecutados en scripts simples y fijos para verificar el correcto entendimiento de la documentacion de la API
2- Crear script simple de lanzamiento de interfaz de usuario graficando par k,v simple.
3- Crear helper que contenga los recursos necesarios a utilizar en el sistema.
4- crear lista de dependencias via requirements.txt

## **Etapa 2:**

Esta etapa se concentra en analizar al menos dos tipos de bases de datos, SQLite, integrada a Python utilizado y una dase de datos externa FireBase.

sopn dos tipos de DB totalmente diferentes, SQLite es relacional y estructurada, un modelo reducido de base SQL, pero perfectamente funcional para iniciar un proyecto y luego implementar ota db SQL, mientras que Firebase es una base de datos no relacional y no SQL, es una DB basada en jerarquias, con formato JSON. RealTime DB y FireStore DB son dos productos ofresidos online. Escapa a este proyecto ahondar en las direrencias de estos productos especificos de FireBase.
