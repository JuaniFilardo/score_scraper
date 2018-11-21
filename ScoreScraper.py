import os
import selenium
import getpass
import time
import subprocess
import argparse
from selenium.webdriver.support.ui import Select
from selenium import webdriver

is_linux = os.name == 'posix'
# TODO: levantar los servicios desde el select de la página
servicios = ["civil","electrica","electronica","industrial",
            "mecanica","metalurgica","quimica","sistemas","tecnicatura"]

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--legajo", help="legajo de estudiante")
    parser.add_argument("-s","--servicio", help="cualquiera de los siguientes: {}".format(", ".join(servicios)))
    args = parser.parse_args()

    user = args.legajo
    servicio = args.servicio

    if user and servicio:
        password = getpass.getpass("Ingrese su contraseña: ")
    else:
        user, servicio, password = get_datos_usuario()

    driver = webdriver.Chrome("./chromedriver") if is_linux else webdriver.Chrome("./chromedriver.exe")
    # Acceder a la página de la facultad
    driver.get("https://www.frc.utn.edu.ar/")

    try:
        driver.maximize_window()
    except:
        print('Error al maximizar, puede ocurrir al usar un manejador de ventanas como i3.')

    driver.find_element_by_id("B").click() # Click para llevar a la página de login

    # Ingresar nombre de usuario, contraseña y servicio
    driver.find_element_by_id("txtUsuario").send_keys(user)
    driver.find_element_by_id("pwdClave").send_keys(password)

    service = Select(driver.find_element_by_id("txtDominios"))
    service.select_by_value(servicio)
    driver.find_element_by_id("btnEnviar").click() # Ingresar a autogestión

    old_len = 999 # Valor deliberadamente alto para que no dé mayor al largo de los labels, después se pisa.

    while True:
        # Modificar con la url de la materia que uno quiere chequear
        # TODO: mostrar las materias del alumno para que elija de cuáles quiere las notas.
        driver.get("https://www.frc.utn.edu.ar/academico3/aula.frc?t=88987858&vC=2018-5-2008-541-3&vNM=Sistemas%20de%20Gesti%F3n")

        labels = driver.find_elements_by_xpath("//tr[@class='clrFndEncGrillaDefault']/td[@width='22%']") # Elemento que contiene las etiquetas
        scores = driver.find_elements_by_xpath("//p[@class='tTitT14']") # Elemento que contiene las notas

        print('-' * 60)
        print(time.strftime('%X'))

        if old_len < len(labels):
            try:
                print('Subieron las notas\n' * 10)
                subprocess.call('notify-send NOTAS :)'.split())
                subprocess.call('aplay sound.wav'.split())
            except:
                pass
            break
        # No pisar valor de old_len si las labels vinieron vacías, lo cual puede ocurrir si se cayó la página
        old_len = len(labels) if len(labels) != 0 else old_len

        for index in range(len(labels)):
            parcial = labels[index].text #.encode('utf-8') usar este encode si se imprime desde jupyter o algo así
            nota = scores[index].text

            print('{}\t{:>20}'.format(str(parcial), nota))

        print('-' * 60)
        time.sleep(60*10) # Chequear cada 10 minutos


def get_datos_usuario():
    user = input("Ingrese su legajo: ")
    print('-' * 60)
    print("Servicios: ")
    for i in range(len(servicios)):
        print('{}- {}'.format(i+1, servicios[i]))
    print('-' * 60)
    servicio = input("Ingrese su servicio (carrera): ")
    password = getpass.getpass("Ingrese su contraseña: ")

    return user, servicio, password

if __name__ == '__main__': main()
