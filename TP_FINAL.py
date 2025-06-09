# Asunto: 24052 - Grupo xxx - TPO
# Integrantes: ¬ Nicolas Torres Quintero

# Desarrollar una aplicación de consola en Python. La temática de esta aplicación es libre

# VINOTECA CODITO A CODITO

#  Inicio del algoritmo

#-------------------------------------------
# Importamos librerias necesarias
#-------------------------------------------
import json

from colorama import Back, Fore, Style, init
init(autoreset=True)

from datetime import datetime

from stdiomask import getpass

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# Funciones y variables de diseño
#-------------------------------------------

def limpiar_terminal():
    print("\033[H\033[J")

def diseño_titulo(titulo, ancho=66): 
    
    titulo_centrado = titulo.center(ancho)
    print("=" * ancho)
    print(Fore.CYAN+Style.BRIGHT+Back.WHITE+titulo_centrado.upper())
    print("=" * ancho)

def diseño_subtitulos(sub_titulo, ancho=66):
    subtitulo_centrado = sub_titulo.center(ancho)
    print("-" * ancho)
    print(Fore.CYAN+subtitulo_centrado.title())
    print("-" * ancho)

def separador(ancho=66):
    print("-" * ancho)

def cierre_cuadro_sup():
    print(color_subtitulo+"╔",end="")
    print(color_subtitulo+"═"*64, end="")
    print(color_subtitulo+"╗")

def cierre_cuadro_inf():
    print(color_subtitulo+"╚",end="")
    print(color_subtitulo+"═"*64, end="")
    print(color_subtitulo+"╝")

def cierre_cuadro_izq():
    print(color_subtitulo+"║", end="")

def cierre_cuadro_der():
    print(color_subtitulo + "║")

def primer_menu():
    diseño_titulo("Menu Manejo de stock")
    print()
    print(color_menu + "1. Articulos (Crea/Modifica/Elimina)")
    print(color_menu + "2. Movimientos (Ingreso/Egreso)")
    print(color_menu + "3. Informes (Listar/Buscar/Historial/Filtrar)")
    print()
    separador()
    print("0. Cerrar el programa")
    print()

color_error = Fore.RED
color_ok = Fore.GREEN+Style.BRIGHT
color_fondo = Fore.BLACK+Back.YELLOW+Style.BRIGHT
color_subtitulo = Fore.CYAN+Style.BRIGHT
color_menu = Fore.LIGHTCYAN_EX
color_submenu = Fore.BLUE
color_totales = Fore.CYAN
#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# Creacion de listas necesarias
#-------------------------------------------

# Lista para Usuarios registrados
try:
    archivo = open("usuarios.json", "r")
    lista_user = json.load(archivo)
    archivo.close()
except:
    lista_user =[]

# Lista de articulos
try:
    archivo = open("productos.json", "r")
    lista_producto = json.load(archivo)
    archivo.close()
except:
    lista_producto=[]

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# Validaciones y creacion de usuario
#-------------------------------------------

def validar_usuario(user):
    resultado = False
    for nuevo_user in lista_user:
        if nuevo_user["usuario"] == user:
            resultado = True
    return resultado

def validar_contraseña(password):
    for user in lista_user:
        if user["password"] == password:
            return True
    return False

def crear_usuario():
    bucle_usuario = True
    while bucle_usuario:
        print()
        nombre = input("Ingrese su usuario: ").title()
        aux_usuario = validar_usuario(nombre)
        if aux_usuario:
            contraseña = getpass("Ingrese su Contraseña: ")
            aux_password = validar_contraseña(contraseña)
            if aux_password:
                separador()
                print(color_ok+f"Bienvenido {nombre}")
                menu_principal()
                break
            else:
                print()
                print(color_error+"Contraseña incorrecta, intente nuevamente:")
                separador()       
        else:
            print()
            print(color_error+"Usuario no encontrado")
            separador()
            nuevo_usuario = input("Desea crear un usuario nuevo: SI/NO: ").upper()
            print()
            while nuevo_usuario not in ["SI", "NO"]:
                print()
                nuevo_usuario = input(color_error+"Comando invalido, intente nuevamente: ").upper()
                separador()
            
            if nuevo_usuario == "SI":
                contraseña = input("Ingrese una contraseña para el nuevo usuario: ")
                print()
                usuario = {
                    "usuario": nombre,
                    "password": contraseña}  
                
                lista_user.append(usuario)

                archivo = open("usuarios.json", "w")
                json.dump(lista_user, archivo)
                archivo.close()
                print(color_ok+f"Usuario {nombre} creado exitosamente.")
                print()
                menu_principal()
                bucle_usuario = False
            else:
                print()
                diseño_subtitulos("Sesion cerrada, gracias por utilizar la interfaz")
                print()
                print(color_fondo + "Programa finalizado.")
                print()
                bucle_usuario = False

def validar_codigo(cod):
    resultado = False
    for articulo in lista_producto:
        if articulo["codigo"] == cod:
            resultado = True
    return resultado

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# funciones de menu carga
#-------------------------------------------

def crear(lista_producto):
    separador()
    print(color_subtitulo+Style.BRIGHT+"Creación de artículos")
    separador()
    while True:
        try:
            print("Ingrese un nuevo código de 6 dígitos")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su nuevo código: ").strip()
            if codigo == "0":
                return lista_producto
            
            codigo = int(codigo)
            if len(str(codigo)) != 6:
                print()
                print(color_error + "El código debe tener exactamente 6 dígitos. Intente nuevamente.")
                separador()
                continue
            elif validar_codigo(codigo):
                print()
                print(color_error + "Código repetido, intente nuevamente.")
                separador()
                continue
            else:
                False

            separador()
            print("Ingrese los datos de su articulo")
            print()
            bodega =     input("Bodega........: ").title()
            cepa   =     input("Cepa..........: ").title()
            linea  =     input("Linea.........: ").title()
            region =     input("Region........: ").title()
            
            bucle_anio = True
            while bucle_anio:
                try:
                    anio   = int(input("Año...........: "))
                    bucle_anio = False
                except ValueError:
                    print()
                    print(color_error + "Entrada inválida. Por favor, ingrese un número entero.")
                    separador()

            bucle_stock = True
            while bucle_stock:
                try:
                    stock  = int(input("Stock.........: "))
                    stock_ultimo = stock
                    bucle_stock = False
                except ValueError:
                    print()
                    print(color_error + "Entrada inválida. Por favor, ingrese un número entero.")
                    separador()

            bucle_precio = True
            while bucle_precio:
                try:
                    precio = float(input("Precio........: $"))
                    bucle_precio = False
                except ValueError:
                    print()
                    print(color_error + "Entrada inválida. Por favor, ingrese un valor.")
                    separador()

            print()
            print(color_ok+"El artículo ha sido CREADO con éxito!")
            print()

            vino = {
                "codigo": codigo,
                "bodega": bodega,
                "cepa": cepa,
                "region": region,
                "linea": linea,
                "anio": anio,
                "stock": stock,
                "precio": precio,
                "historial": [],
                "stock_ultimo": stock_ultimo}
            
            lista_producto.append(vino)

            archivo = open("productos.json", "w")
            json.dump(lista_producto, archivo)
            archivo.close()

            return lista_producto
    
        except ValueError:
                print()
                print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
                separador()

def modificar(lista_producto):
    separador()
    print(color_subtitulo+Style.BRIGHT+"Modificación de artículos")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su código: ")
            
            if codigo == "0":
                print("Volviendo al menú anterior.")
                return lista_producto
            
            codigo = int(codigo)
            
            
            aux = validar_codigo(codigo)
            if aux == False:
                print()
                print(color_error+"Codigo inexistente, intente nuevamente")
                separador()
            else:
                for vino in lista_producto:
                    if codigo == vino["codigo"]:
                        print()
                        print(f"Bodega......:", vino['bodega'])
                        print(f"Cepa........:", vino['cepa'])
                        print(f"Linea.......:", vino['linea'])
                        print(f"Region......:", vino['region'])
                        print(f"Año.........: {vino['anio']}")
                        print(f"Stock.......: {vino['stock_ultimo']}")
                        print(f"Precio......: $ {vino['precio']:.2f}")
                        separador()
                        print()
                        bodega_viejo =    vino['bodega']
                        cepa_viejo   =    vino['cepa']
                        linea_viejo  =    vino['linea']
                        region_viejo =    vino['region']
                        anio_viejo   =    vino['anio']
                        stock        =    vino['stock']
                        stock_ultimo =    vino['stock_ultimo']
                        precio_viejo =    vino['precio']
                        movimiento   =    vino['historial']

                        print(color_totales+"Dejar en blanco para mantener el dato anterior")
                        separador()
                        bodega =     input("Bodega........: ").title()
                        cepa   =     input("Cepa..........: ").title()
                        linea  =     input("Linea.........: ").title()
                        region =     input("Region........: ").title()
                        
                        while True:
                            anio = input("Año...........: ")
                            if anio == "":
                                anio = anio_viejo
                                break
                            try:
                                anio = int(anio)
                                break
                            except ValueError:
                                print(color_error + "Por favor, ingrese un año válido.")

                        while True:
                            precio = input("Precio........: $ ")
                            if precio == "":
                                precio = precio_viejo
                                break
                            try:
                                precio = float(precio)
                                break
                            except ValueError:
                                print(color_error + "Por favor, ingrese un precio válido.")

                        separador()
                        
                        if len(bodega) == 0:
                            bodega_nuevo = bodega_viejo
                        else:
                            bodega_nuevo = bodega
                        
                        if len(cepa) == 0:
                            cepa_nuevo = cepa_viejo
                        else:
                            cepa_nuevo = cepa

                        if len(linea) == 0:
                            linea_nuevo = linea_viejo
                        else:
                            linea_nuevo = linea

                        if len(region) == 0:
                            region_nuevo = region_viejo
                        else:
                            region_nuevo = region

                        for indice, vino in enumerate(lista_producto): 
                            if codigo == vino['codigo']:
                                del lista_producto[indice]
                        
                        vino = {
                            "codigo": codigo,
                            "bodega": bodega_nuevo,
                            "cepa": cepa_nuevo,
                            "linea": linea_nuevo,
                            "region": region_nuevo,
                            "anio": anio,
                            "stock": stock,
                            "precio": precio,
                            "historial": movimiento,
                            "stock_ultimo": stock_ultimo}
                                        
                        lista_producto.append(vino)

                        archivo = open("productos.json", "w")
                        json.dump(lista_producto, archivo)
                        archivo.close()

                        print()
                        print(color_ok+"El articulo ha sido MODIFICADO con exito!")
                        print()
                        cierre_cuadro_sup()
                        cierre_cuadro_izq()
                        print(f" Bodega.....: {vino['bodega'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Cepa.......: {vino['cepa'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Linea......: {vino['linea'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Region.....: {vino['region'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Año........: {vino['anio']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Stock......: {vino['stock_ultimo']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Precio.....: $ {vino['precio']:<47.2f} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_inf()
                        return lista_producto 
                break
        except ValueError:
                print()
                print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
                separador()

def eliminar(lista_producto):
    separador()
    print(color_subtitulo + Style.BRIGHT + "Eliminación de artículos")
    separador()
    
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = input("Su código: ")
            
            if codigo == "0":
                print("Volviendo al menú anterior.")
                return lista_producto
            
            codigo = int(codigo)
            
            articulo_encontrado = False
            for vino in lista_producto:
                if vino["codigo"] == codigo:
                    articulo_encontrado = True
                    
                    print()
                    print(f"Bodega.......: {vino['bodega']}")
                    print(f"Cepa.........: {vino['cepa']}")
                    print(f"Linea........: {vino['linea']}")
                    print(f"Región.......: {vino['region']}")
                    print(f"Año..........: {vino['anio']}")
                    print(f"Stock........: {vino['stock']}")
                    print(f"Precio.......: {vino['precio']:.2f}")
                    print()
                    
                    confirmacion = input("¿Está seguro que desea eliminar este artículo? (SI/NO): ").strip().lower()
                    
                    while confirmacion not in ["si", "no"]:
                        print()
                        print(color_error + "Por favor, responda con 'SI' o 'NO'.")
                        confirmacion = input("¿Está seguro que desea eliminar este artículo? (SI/NO): ").strip().lower()
                    
                    if confirmacion == "si":
                        lista_producto.remove(vino)
                        
                        archivo = open("productos.json", "w")
                        json.dump(lista_producto, archivo)
                        archivo.close()
                        
                        print()
                        print(color_ok + "El artículo ha sido ELIMINADO con éxito!")
                        separador()
                        return lista_producto
                    else:
                        print()
                        print(color_error+"Operación cancelada. Volviendo al menú anterior.")
                        separador()
                        return lista_producto
            
            if not articulo_encontrado:
                print()
                print(color_error + "Código inexistente, intente nuevamente.")
                separador()
        
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

#-------------------------------------------
# funciones de menu movimientos
#-------------------------------------------

def ingresar():
    separador()
    print(color_subtitulo+Style.BRIGHT+"Ingreso de Stock")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = int(input("Su código: "))
            
            if codigo == 0:
                return

            if not validar_codigo(codigo):
                print()
                print(color_error + "Código inexistente, intente nuevamente.")
                separador()
                continue

            vino = next((vino for vino in lista_producto if vino["codigo"] == codigo), None)

            if vino:
                bodega        = vino["bodega"]
                linea         = vino["linea"]
                cepa          = vino["cepa"]
                anio          = vino["anio"]
                stock_inicial = vino["stock"]
                stock_ultimo = vino.get("stock_ultimo", stock_inicial)

                print()
                separador()
                print(f"{codigo}:  {bodega} {linea} {cepa} {anio}")
                print(f"Stock actual: {stock_ultimo}")
                separador()

            try:
                cantidad = int(input("Unidades a ingresar: "))
                if cantidad <= 0:
                    print()
                    print(color_error + "La cantidad debe ser un número positivo. Intente nuevamente.")
                    separador()
                    return
                
                for vino in lista_producto:
                    if vino["codigo"] == codigo:
                        stock_ultimo += cantidad
                        vino["stock_ultimo"] = stock_ultimo
                        movimiento = {
                            "tipo": "entrada",
                            "cantidad": cantidad,
                            "fecha": datetime.now().strftime("%d/%m/%Y")}
                        
                        if not isinstance(vino.get("historial"), list):
                            vino["historial"] = []
                        
                        vino["historial"].append(movimiento)
                
                    archivo = open("productos.json", "w")
                    json.dump(lista_producto, archivo)
                    archivo.close()

                print()
                print(color_ok + "El stock ha sido INGRESADO con exito!")
                separador()
                print(color_totales + f"{codigo}:  {bodega} {linea} {cepa} {anio}")
                print(color_totales + f"Stock actualizado: {stock_ultimo}")
                separador()
                break

            except ValueError:
                print()
                print(color_error + "Entrada inválida. Ingrese un número entero.")
                separador()
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

def bajar():
    separador()
    print(color_subtitulo+Style.BRIGHT+"Egreso de Stock")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = int(input("Su código: "))
            
            if codigo == 0:
                return

            if not validar_codigo(codigo):
                print()
                print(color_error + "Código inexistente, intente nuevamente.")
                separador()
                continue
            
            vino = next((vino for vino in lista_producto if vino["codigo"] == codigo), None)
            
            if vino:
                bodega        = vino["bodega"]
                linea         = vino["linea"]
                cepa          = vino["cepa"]
                anio          = vino["anio"]
                stock_inicial = vino["stock"]
                stock_ultimo = vino.get("stock_ultimo", stock_inicial)

                print()
                separador()
                print(f"{codigo}:  {bodega} {linea} {cepa} {anio}")
                print(f"Stock inicial: {stock_ultimo}")
                separador()

            try:
                cantidad = int(input("Unidades a egresar: "))
                if cantidad <= 0:
                    print()
                    print(color_error + "La cantidad debe ser un número positivo. Intente nuevamente.")
                    separador()
                    return
                
                for vino in lista_producto:
                    if vino["codigo"] == codigo:
                        if vino["stock_ultimo"] < cantidad:
                            print()
                            print(color_error + "Stock insuficiente. Intente nuevamente.")
                            separador()
                            return
                        stock_ultimo -= cantidad
                        vino["stock_ultimo"] = stock_ultimo
                        movimiento = {
                            "tipo": "salida",
                            "cantidad": cantidad,
                            "fecha": datetime.now().strftime("%d/%m/%Y")}
                        
                        if not isinstance(vino.get("historial"), list):
                            vino["historial"] = []

                        vino["historial"].append(movimiento)
                
                        archivo = open("productos.json", "w")
                        json.dump(lista_producto, archivo)
                        archivo.close()

                print()
                print(color_ok + "El stock ha sido EGRESADO con exito!")
                separador()
                print(color_totales + f"{codigo}:  {bodega} {linea} {cepa} {anio}")
                print(color_totales + f"Stock actualizado: {stock_ultimo}")
                separador()
                break

            except ValueError:
                print()
                print(color_error + "Entrada inválida. Ingrese un número entero.")
                separador()
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# funciones de menu de informes
#-------------------------------------------

def listar():
    print()
    print(color_subtitulo+"Listado de vinos")
    titulos = ("Codigo","Bodega","Cepa","Linea","Region","Año","Stock"," ","Precio")
    print(color_subtitulo+"-"*118)
    print(color_subtitulo+f"|{titulos[0]:>5} | ", end="")
    print(color_subtitulo+f"{titulos[1]:<20} | ", end="")
    print(color_subtitulo+f"{titulos[2]:<18} | ", end="")
    print(color_subtitulo+f"{titulos[3]:<18} | ", end="")
    print(color_subtitulo+f"{titulos[4]:<12} | ", end="")
    print(color_subtitulo+f"{titulos[5]:<4} | ", end="")
    print(color_subtitulo+f"{titulos[6]:<5} | ", end="")
    print(color_subtitulo+f"{titulos[7]}", end="")
    print(color_subtitulo+f"{titulos[8]:>10} | ")
    print(color_subtitulo+"-"*118)
    for vino in lista_producto:

        if not isinstance(vino.get("stock_ultimo"), int):
            vino["stock_ultimo"] = vino["stock"]

        print(f"|{vino['codigo']:>6} | ", end="")
        print(f"{vino['bodega'][:20]:<20} | ", end="")
        print(f"{vino['cepa'][:18]:<18} | ", end="")
        print(f"{vino['linea'][:18]:<18} | ", end="")
        print(f"{vino['region'][:12]:<12} | ", end="")
        print(f"{vino['anio']} | ", end="")
        print(f"{vino['stock_ultimo']:>5} | ", end="")
        print(f"$", end="")
        print(f"{vino['precio']:>10.2f} | ")
    print(color_subtitulo+"-"*118)

def buscar():
    separador()
    print(color_subtitulo+Style.BRIGHT+"Buscar un artículo")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = int(input("Su código: "))
            
            if codigo == 0:
                return
            aux = validar_codigo(codigo)
            if aux == False:
                print()
                print(color_error+"Codigo inexistente, intente nuevamente")
                separador()
            else:
                for vino in lista_producto:
                    if not isinstance(vino.get("stock_ultimo"), int):
                        vino["stock_ultimo"] = vino["stock"]
                    if codigo == vino["codigo"]:
                        cierre_cuadro_sup()
                        cierre_cuadro_izq()
                        print(f" Bodega.....: {vino['bodega'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Cepa.......: {vino['cepa'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Linea......: {vino['linea'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Region.....: {vino['region'][:46]:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Año........: {vino['anio']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Stock......: {vino['stock_ultimo']:<49} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_izq()
                        print(f" Precio.....: $ {vino['precio']:<47.2f} ",end="")
                        cierre_cuadro_der()
                        cierre_cuadro_inf()
                        break 
                break
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

def consultar_movimientos():
    separador()
    print(color_subtitulo+Style.BRIGHT+"Hitorial de Movimientos de Stock")
    separador()
    while True:
        try:
            print("A continuación, ingrese el código del producto")
            print()
            separador()
            print("0. Volver al menu anterior")
            print()
            codigo = int(input("Su código: "))
            
            if codigo == 0:
                return

            if not validar_codigo(codigo):
                print()
                print(color_error + "Código inexistente, intente nuevamente.")
                separador()
                return

            vino = next((vino for vino in lista_producto if vino["codigo"] == codigo), None)
            
            if vino:
                bodega        = vino["bodega"]
                linea         = vino["linea"]
                cepa          = vino["cepa"]
                anio          = vino["anio"]
                stock_inicial = vino["stock"]
                historico     = vino.get("historial", [])
                stock_ultimo = vino.get("stock_ultimo", stock_inicial)


                if not isinstance(vino.get("stock_ultimo"), int):
                    vino["stock_ultimo"] = stock_inicial
                
                print()
                print(color_subtitulo + f"Historial de Movimientos de Stock para Código: {codigo}")
                print(color_subtitulo + "-" * 58)
                titulos = ("Fecha", "Entrada", "Salida", "Stock Remanente")
                print(Style.BRIGHT + f"{titulos[0]:<12} | {titulos[1]:>10} | {titulos[2]:>10} | {titulos[3]:>17}")
                print(color_subtitulo + "-" * 58)
                print(f"{codigo}:  {bodega} {linea} {cepa} {anio}")
                print(f"Stock inicial: {stock_inicial:>43}")
                print()
                
                

                stock_remanente = int(stock_inicial)
                total_entrada = 0
                total_salida = 0
                for movimiento in historico:
                    fecha = movimiento["fecha"]
                    if movimiento["tipo"] == "entrada":
                        entrada = int(movimiento["cantidad"])
                        salida = ""
                        stock_remanente += entrada
                        total_entrada += entrada
                    elif movimiento["tipo"] == "salida":
                        entrada = ""
                        salida = int(movimiento["cantidad"])
                        stock_remanente -= salida
                        total_salida += salida
                
                    
                    print(f"{fecha:<12} | {entrada:>10} | {salida:>10} | {stock_remanente:>17}")
                

                print(color_subtitulo + "-" * 58)
                print(color_totales + f"{'Totales':<12} | {total_entrada:>10} | {total_salida:>10} | {stock_ultimo:>17}")
                break
        
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese un número entero de 6 dígitos.")
            separador()

def filtrar_productos(lista_producto):
    diseño_subtitulos("Filtrar Artículos")
    print()

    criterios_disponibles = ['bodega', 'cepa', 'linea', 'region', 'anio']
    intentos = 0
    max_intentos = 3

    while True:
        print("Criterios disponibles para fitrar:")
        for valor in criterios_disponibles:
            print(color_totales+f"- {valor}")
        print()
        separador()
        print("0. Volver al menu anterior")
        print()
        criterio = input("Su elección: ").lower()
        print()
        if criterio == "0":
            return
        if criterio == "año":
            criterio = "anio"
        if criterio in criterios_disponibles:
            break
        else:
            intentos += 1
            if intentos >= max_intentos:
                print(color_error + "Ha superado el número máximo de intentos. Regresando al menú de informes.")
                return
            print(color_error + f"El criterio '{criterio}' no es válido. Por favor, ingrese un criterio válido.")
    
    valores_disponibles = sorted(set(str(vino[criterio]).title() for vino in lista_producto if criterio in vino))
    if not valores_disponibles:
        print(color_error + f"No hay valores disponibles para el criterio '{criterio}'. Regresando al menú de informes.")
        return

    print("Valores disponibles para el criterio seleccionado:")
    for valor in valores_disponibles:
        print(color_totales+f"- {valor}")

    intentos = 0

    while True:
        print(f"Ingrese cual '{criterio}' desea filtrar: ")
        print()
        separador()
        print("0. Volver al menu anterior")
        print()
        valor = input("Su elección: ").lower()
        separador()
        print()
        if valor == "0":
            return
        if criterio == "anio":
            try:
                valor = int(valor)
            except ValueError:
                print(color_error + "Debe ingresar un número válido para el año. Intente de nuevo.")
                continue
        if str(valor).title() in valores_disponibles:
            break
        else:
            intentos += 1
            if intentos >= max_intentos:
                print(color_error + "Ha superado el número máximo de intentos. Regresando al menú de informes.")
                return
            print(color_error + f"El valor '{valor}' no está disponible para el criterio '{criterio}'. Intente de nuevo.")

    print()
    print(color_subtitulo + f"Listado de vinos filtrados por {criterio}: {valor}")
    titulos = ("Codigo", "Bodega", "Cepa", "Linea", "Region", "Anio", "Stock", " ", "Precio")
    print(color_subtitulo + "-" * 118)
    print(color_subtitulo + f"|{titulos[0]:>5} | {titulos[1]:<20} | {titulos[2]:<18} | {titulos[3]:<18} | {titulos[4]:<12} | {titulos[5]:<4} | {titulos[6]:<5} | {titulos[7]}{titulos[8]:>10} | ")
    print(color_subtitulo + "-" * 118)

    for vino in lista_producto:
        if criterio in vino and str(vino[criterio]).title() == str(valor).title():
            print(f"|{vino['codigo']:>6} | {vino['bodega'][:20]:<20} | {vino['cepa'][:18]:<18} | {vino['linea'][:18]:<18} | {vino['region'][:12]:<12} | {vino['anio']} | {vino['stock_ultimo']:>5} | ${vino['precio']:>10.2f} | ")

    print(color_subtitulo + "-" * 118)

#-------------------------------------------
# Definimos los SubMenu
#-------------------------------------------

def menu_carga(lista_producto):
    while True:
        print()
        print()
        separador()
        print(color_submenu+Style.BRIGHT+"Sub-menu de articulos")
        separador()
        print(color_submenu+"1. Crear articulos")
        print(color_submenu+"2. Modificar articulos")
        print(color_submenu+"3. Eliminar articulos")
        print()
        separador()
        print("0. Volver al menu anterior")
        print()
        opcion = input("Ingrese su opción: ")
        separador()

        match opcion:
            case "1":
                limpiar_terminal()
                lista_producto = crear(lista_producto)
            case "2":
                limpiar_terminal()
                lista_producto = modificar(lista_producto)
            case "3":
                limpiar_terminal()
                lista_producto = eliminar(lista_producto)
            case "0":
                primer_menu()
                break
            case _:
                print()
                print(color_error+"Opción no válida. Intente de nuevo.")
                separador()

def menu_movimientos():
    while True:
        print()
        print()
        separador()
        print(color_submenu+Style.BRIGHT+"Sub-menu de Stock")
        separador()
        print(color_submenu+"1. Ingresos de stock")
        print(color_submenu+"2. Egresos de stock")
        print()
        separador()
        print("0. Volver al menu anterior")
        print()
        opcion = input("Ingrese su opción: ")
        separador()

        match opcion:
            case "1":
                limpiar_terminal()
                ingresar()
            case "2":
                limpiar_terminal()
                bajar()
            case "0":
                primer_menu()
                break
            case _:
                print()
                print(color_error+"Opción no válida. Intente de nuevo.")
                separador()

def menu_informes():
    while True:
        print()
        print()
        separador()
        print(color_submenu + Style.BRIGHT + "Sub-menu de informes")
        separador()
        print(color_submenu + "1. Listar artículos")
        print(color_submenu + "2. Buscar artículos")
        print(color_submenu + "3. Historial de movimiento")
        print(color_submenu + "4. Filtrar artículos")
        print()
        separador()
        print("0. Volver al menú anterior")
        print()
        opcion = input("Ingrese su opción: ")
        separador()

        match opcion:
            case "1":
                limpiar_terminal()
                listar()
            case "2":
                limpiar_terminal()
                buscar()
            case "3":
                limpiar_terminal()
                consultar_movimientos()
            case "4":
                limpiar_terminal()
                filtrar_productos(lista_producto)
            case "0":
                primer_menu()
                break
            case _:
                print()
                print(color_error + "Opción no válida. Intente de nuevo.")
                separador()

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# Definimos los Menu Principal
#-------------------------------------------

def menu_principal():
    primer_menu()

    bandera_menu = True
    while bandera_menu:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                limpiar_terminal()
                menu_carga(lista_producto)
            elif opcion == 2:
                limpiar_terminal()
                menu_movimientos()
            elif opcion == 3:
                limpiar_terminal()
                menu_informes()
            elif opcion == 0:
                limpiar_terminal()
                print()
                diseño_subtitulos("Sesión cerrada, gracias por utilizar la interfaz")
                print()
                print(color_fondo + "Programa finalizado.")
                print()
                bandera_menu = False
            else:
                print()
                print(color_error + "Opción incorrecta, intente nuevamente.")
                separador()
        except ValueError:
            print()
            print(color_error + "Entrada inválida. Por favor, ingrese una opción válida.")
            separador()

#+++++++++++++++++++++++++++++++++++++++++++

#-------------------------------------------
# Inicio del programa
#-------------------------------------------

diseño_titulo("VINOTECA CODITO A CODITO")
diseño_subtitulos("Bienvenido a la interfaz de Stock")
crear_usuario()

