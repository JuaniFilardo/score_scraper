## UTN FRC - Scraper de notas

Este script permite obtener las notas directamente de Autogestión 3 de la [UTN FRC] utilizando [selenium].

Por el momento tiene algunas cosas que sólo van a correr en Linux, pero puede correr en Windows. La URL de la materia a chequear está hardcodeada (por ahora), pero puede ser cambiada a gusto.

**Aviso**: usar responsablemente. Muchas peticiones a Autogestión y el sistema se va a caer, dejando a todos sin notas. Es una buena idea esperar un tiempo entre peticiones; no tiene sentido hacerlas cada menos de 5 minutos.

### Setup

Los requerimientos que no están incluidos aquí pueden obtenerse fácilmente:

#### Selenium
```
$ pip install selenium # O también:
$ pip install -r requirements.txt
```

#### Chromedriver (o el driver de tu browser preferido)
Las distintas versiones se pueden encontrar acá: https://sites.google.com/a/chromium.org/chromedriver/downloads

Atajo para Linux (última versión al día 20/11/2018):
```
$ wget https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
```
Otros drivers en: https://www.seleniumhq.org/download/

Es importante que el nombre del archivo sea chromedriver si estás en Linux, y chromedriver.exe si estás en Windows.


#### Sonido de notificación
Actualmente funcionando sólo para Linux. Puede ponerse cualquier sonido, pero dejo este a mano:
```
$ curl http://soundbible.com/grab.php?id=1746&type=wav > sound.wav
```

### Cómo usarlo
<pre>
usage: ScoreScraper.py [-h] [-l LEGAJO] [-s SERVICIO]

optional arguments:
  -h, --help            show this help message and exit
  -l LEGAJO, --legajo LEGAJO
                        legajo de estudiante
  -s SERVICIO, --servicio SERVICIO
                        cualquiera de los siguientes: civil, electrica,
                        electronica, industrial, mecanica, metalurgica,
                        quimica, sistemas, tecnicatura
</pre>


#### Notas de uso
- Luego te va a pedir la clave de Autogestión.
- Si corrés el script sin los flags -l o -s no pasa nada, después te los va a pedir igual. Vos tranqui.
- La URL de la materia está hardcodeada, ver método driver.get() que se encuentra en el bucle while True y cambiarla según sea necesario.
- Los servicios pueden ser cualquiera de los que están en Autogestión, no sólo los que aparecen ahí.

### Colaboradores
- [Juli De Angelis]
- [Juani Filardo]

A esta aplicación le vendrían bien muchos cambios para que sea más útil.
¡Cualquier pull request será bienvenida!


-----------------------------------------------------------------------
*"Every good work of software starts by scratching a developer’s
personal itch". [ESR]*

[//]:# (Links. This won't be seen after it's interpreted.)
[selenium]: <https://www.seleniumhq.org/>
[UTN FRC]: <https://www.frc.utn.edu.ar/>
[chromedriver]: <https://sites.google.com/a/chromium.org/chromedriver/downloads>
[alarma]: <http://soundbible.com/grab.php?id=1746&type=wav>
[Juli De Angelis]: <https://github.com/julideangelis>
[Juani Filardo]: <https://github.com/JuaniFilardo>
[ESR]:<http://www.unterstein.net/su/docs/CathBaz.pdf>
