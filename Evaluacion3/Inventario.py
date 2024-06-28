import csv

def menu():
    print("****Bienvenido al sistema de menu de inventario****")
    print("1.Agregar productos al inventario")
    print("2.Ver inventario")
    print("3.Clasificar y exportar productos")
    print("4.Salir")
    opcion=input("elija opcion:")
    return opcion

def agregar_productos():
    id=input("ingrese id del producto:")
    nombre=input("ingrese el nombre del producto")
    categoria=input("ingrese la categoria[textil,electronica o calzado]")
    precio=int(input("ingrese el precio del producto"))
    with open ("inventario.csv","a", newline="")as inventario:
        escritor_produc=csv.writer(inventario)
        escritor_produc.writerow([id,nombre,categoria,precio])
    print(f"El producto con id {id} con nombre {nombre}, categorizado como {categoria} fue ingresado con un precio de ${precio}")

def ver_inventario():
    with open ("inventario.csv", "r", newline="")as inventario:
        leer_archivo=csv.reader(inventario)
        for row in leer_archivo:
            id, nombre, categoria,precio=row
    print(f"ID: {id}, Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")

    
def clasificar_productos():
    categorias = {
        "electronica": [],
        "textil": [],
        "calzado": []}
    
   
    with open("inventario.csv", "r", newline="") as inventario:
        leer_archivo = csv.reader(inventario)
        for row in leer_archivo:
            id_producto, nombre, categoria, precio = row
            producto = f"ID: {id_producto}, Nombre: {nombre}, Precio: ${precio}"
            
            if categoria.lower() == "electronica":
                categorias["electronica"].append(producto)
            elif categoria() == "textil":
                categorias["textil"].append(producto)
            elif categoria() == "calzado":
                categorias["calzado"].append(producto)
            else:
                print(f"Producto {nombre} con categoría {categoria}  no reconocida.")
    
 
    with open("clasificacion_productos.txt", "w") as clasificacion_produc:
        clasificacion_produc.write("----- Productos de Electrónica -----\n")
        for producto in categorias["electronica"]:
            clasificacion_produc.write(f"{producto}\n")
        
        clasificacion_produc.write("\n----- Productos Textiles -----\n")
        for producto in categorias["textil"]:
            clasificacion_produc.write(f"{producto}\n")
        
        clasificacion_produc.write("\n----- Productos de Calzado -----\n")
        for producto in categorias["calzado"]:
            clasificacion_produc.write(f"{producto}\n")
    
    print("Clasificación de productos completada.")


while True:
    opcion = menu() 
    if opcion == '1':
        agregar_productos() 
    elif opcion == '2':
        ver_inventario()     
    elif opcion=="3":
        clasificar_productos()
    elif opcion=="4":
        break
    else:
        print("opcion no valida, por favor ingrese una opcion valida")    