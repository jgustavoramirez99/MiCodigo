#Mi primera lista en Python
productos = ["Laptop","Mouse","Teclado","Camara","Pantalla"]

print("======  BIENVENIDO  AL SISTEMA DE INVENTARIO =======")
nuevo_producto = input("Introduce un nuevo accesorio para la oficina: ")

#Se agrega el nuevo producto a la lista
productos.append(nuevo_producto)
print("\n Tu inventario actualidado es:")

for item in productos:
    if item == "laptop":
        print (f"- {item} (Este es el equipo principal)")
else: 
    print(f"- {item}")

    print("\n PROCESO TERMINADO CON EXITO")
