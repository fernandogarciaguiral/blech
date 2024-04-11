


import os
from bs4 import BeautifulSoup
import requests

class Menu:
    def __init__(self):
        self.opciones = []

    def agregar_opcion(self, opcion, color='\033[1;32m'):
            opcion_formateada = f"{color}{opcion}\033[0m"  # Aplicando el color especificado
            self.opciones.append(opcion_formateada)

    def mostrar_menu(self):
        print("Menú: ")
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")

    def obtener_seleccion(self):
        while True:
            try:
                seleccion = int(input("Seleccione una opción: "))
                if 1 <= seleccion <= len(self.opciones):
                    return seleccion
                else:
                    print("Selección no válida. Por favor, elija una opción válida.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
                
    def limpiar_pantalla(self):
        if os.name == 'nt':
            ___ = os.system('cls')
##################################################################################################
"""class SubMenu(Menu):
    def mostrar_menu(self):
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")

    def obtener_seleccion(self):
        while True:
            try:
                seleccion = int(input("\nSeleccione una opción: "))
                if 1 <= seleccion <= len(self.opciones):
                    return seleccion
                else:
                    print("\nSelección no válida. Por favor, elija una opción válida.")
            except ValueError:
                print("\nEntrada no válida. Ingrese un número.")"""
#####################################################################################################                
                
class BleachScraper:
    def __init__(self):
        self.url_base = "https://bleach.fandom.com/es/wiki/"
        self.shinigamis = []
        self.zanpakuto = []
        self.bankai = [] 
        
    def obtener_shinigami_zampakuto_bankai(self):
        url_armas = self.url_base + "Lista_de_Armas"
        response = requests.get(url_armas)
        if response.status_code != 200:
            raise ValueError('No se pudo obtener información de la página')
        soup = BeautifulSoup(response.text, "html.parser")

        h3 = soup.find('span', {'id': 'Zanpaku-t.C5.8D_de_Shinigamis_y_Visored'})
        tabla = h3.find_next('table')

           
        for fila in tabla.find_all('tr')[2:]:
            columnas = fila.find_all('td')
            if len(columnas) >=3:                
                nombre = columnas[1].text.strip()
                espada = columnas[0].text.strip()
                poder = columnas[2].text.strip()
                self.shinigamis.append(nombre)
                self.zanpakuto.append(espada)
                self.bankai.append(poder)
        
        return self.shinigamis, self.zanpakuto, self.bankai

    def obtener_quincys(self):
        url_quincy = self.url_base + "Lista_de_Quincy"
        response = requests.get(url_quincy)
        if response.status_code != 200:
            raise ValueError('No se pudo obtener información de la página')
        soup = BeautifulSoup(response.text, "html.parser")

        h3 = soup.find('span', {'id': 'Sternritter'})
        listado = h3.find_next('ul')

        quincys = []
        for li in listado.find_all('li'):
            nombre = li.text.strip()
            quincys.append(nombre)
        
        return quincys

    
###################################################################################################

if __name__ == '__main__':
    
    scraper = BleachScraper()  # Crear una instancia de BleachScraper fuera del bucle
    nombre, _, _ = scraper.obtener_shinigami_zampakuto_bankai()  # Usar la instancia de BleachScraper creada fuera del bucle
    shinigamis_creados = []
    while True:
        menu = Menu()
        menu.limpiar_pantalla()
        menu.agregar_opcion('Crear personaje')
        menu.agregar_opcion('Ver personajes creados')
        menu.agregar_opcion('Ver detalles de personaje')
        menu.agregar_opcion('Activar habilidad o atacar')
        menu.agregar_opcion('Salir', '\033[1;31m')
        menu.mostrar_menu()
        seleccion = menu.obtener_seleccion()
        menu.limpiar_pantalla()

        if seleccion == 1:
            submenu = Menu()
            print('--------- CREAR PERSONAJE ----------')
            print('\nSeleciona el tipo de personaje que deseas crear: \n')
            submenu.agregar_opcion('Shinigami')
            submenu.agregar_opcion('Holow')
            submenu.agregar_opcion('Quincy')
            submenu.agregar_opcion('Visored  (Shinigami con padres Holow)')
            submenu.mostrar_menu()    
            subseleccion = submenu.obtener_seleccion()
            submenu.limpiar_pantalla()
            
            if subseleccion == 1:                
                for i, n in enumerate(nombre, start=1):
                    print(f"{i}. {n}")
                ## Validación de datos                  
                while True:
                    numero_shinigami = int(input('\nDigita el número del Shinigami que deseas crear: ')) - 1
                    try:
                        if 0 <= numero_shinigami < len(nombre):
                            shinigami_seleccionado = nombre[numero_shinigami]
                            print(f"Has seleccionado a {shinigami_seleccionado}.")
                            shinigamis_creados.append(shinigami_seleccionado)
                        else:
                            print("Número de Shinigami no válido.")
                        print(shinigamis_creados)
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("\nEntrada no válida. Ingrese un número.")
                    submenu.limpiar_pantalla()
                    break
            
            elif seleccion == 2:
                pass
                # Lógica para la opción 2
            elif seleccion == 3:
                pass
                # Lógica para la opción 3
            elif seleccion == 4:
                pass
                # Lógica para la opción 4
            elif seleccion == 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
        elif seleccion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        