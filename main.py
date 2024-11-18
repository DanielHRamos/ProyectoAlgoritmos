from Cliente import Cliente, Juridico
from funciones import cargar_api, validar_numero
from Producto import Producto


def main():
    productos = [] #Lista de objetos de tipo Producto
    clientes = [] #Lista de objetos de tipo Cliente
    
    #Recorrido de la API para almacenar los productos en la lista anterior
    for product in cargar_api():
        vehiculos_compatibles = ", ".join(product["compatible_vehicles"])
        productos.append(Producto(product["id"],
                                  product["name"],
                                  product["description"],
                                  product["price"],
                                  product["category"],
                                  product["inventory"],
                                  vehiculos_compatibles))
    
    
    #Menu principal del programa
    while True:
        opcion = input(f"\nBienvenido, ¿Qué desea hacer? \n\n1) Gestionar productos.\n2) Gestionar ventas. \n3) Gestionar clientes. \n4) Gestionar pagos. \n5) Gestionar envios. \n6) Indicadores de gestion. (Estadisticas) \n\n0) Salir.\n\n\n>>> ")
        
        if opcion == "1":
            while True:
                primero = input(f"\n1) Mostrar productos. \n2) Agregar producto. \n3) Buscar producto. \n4) Modificar producto. \n5) Eliminar producto. \n\n0) Volver al menu principal.\n\n\n>>> ")
                if primero == "1":
                    for producto in productos:
                        producto.MostrarAtributos()

                elif primero == "2":
                    Producto.AgregarProducto(productos)

                elif primero == "3":
                    while True:
                        filtro_elegido = input(f"Seleccione uno de los siguientes filtros:\n1) Categoria. \n2) Precio. \n3) Nombre. \n4) Disponibilidad.\n\n0) Volver.\n\n\n>>> ")
                        if filtro_elegido == "1":
                            categoria = input(f"Estas son las categorias disponibles:\n1) Aceites. \n2) Filtros. \n3) Empacaduras. \n4) Tren delantero. \n5) Rodamientos. \n6) Motor. \n7) Grasas. \n8) Gomas. \n\n0) Volver.\n\n\n>>> ")
                            if categoria.lower() == "1": 
                                categoria = "aceites" 
                            elif categoria.lower() == "2":
                                categoria = "filtros" 
                            elif categoria.lower() == "3": 
                                categoria = "empacaduras" 
                            elif categoria.lower() == "4": 
                                categoria = "tren delantero" 
                            elif categoria.lower() == "5": 
                                categoria = "rodamientos" 
                            elif categoria.lower() == "6": 
                                categoria = "motor" 
                            elif categoria.lower() == "7": 
                                categoria = "grasas" 
                            elif categoria.lower() == "8": 
                                categoria = "gomas"
                            else: 
                                print("Categoría no válida.") 
                                continue
                            resultados = Producto.FiltrarProductos(productos, criterio="categoria", valor=categoria)
                        elif filtro_elegido == "2":
                            precio = validar_numero("Introduce el precio del producto: ", float)
                            resultados = Producto.FiltrarProductos(productos, criterio="precio", valor=precio)
                        
                        elif filtro_elegido == "3":
                            nombre = input("Introduce el nombre del producto: ") 
                            resultados = Producto.FiltrarProductos(productos, criterio="nombre", valor=nombre)
                        
                        elif filtro_elegido == "4":
                            disponibilidad = validar_numero("Introduce el stock disponible del producto: ", int) 
                            resultados = Producto.FiltrarProductos(productos, criterio="disponibilidad", valor=disponibilidad)
                        
                        elif filtro_elegido == "0":
                            break
                        
                        else:
                            print("Error, ha ingresado un valor incorrecto")
                        for producto in resultados: 
                            producto.MostrarAtributos()
                elif primero == "4":
                    id_modificar = int(input("Introduce el ID del producto a modificar: ")) 
                    Producto.ModificarProducto(productos, id_modificar)
                
                elif primero == "5":
                    for producto in productos:
                        producto.MostrarAtributos()
                    id_eliminar = int(input("Introduce el ID del producto a eliminar: "))
                    Producto.EliminarProducto(productos, id_eliminar)
                    
                    
                elif primero == "0":
                    break
                
                else:
                    print("Error, ha ingresado un valor incorrecto")
                    
        elif opcion == "2":
            pass
            
        elif opcion == "3":
            while True:
                tercero = input(f"\n1) Mostrar clientes. \n2) Registrar cliente. \n3) Modificar cliente. \n4) Eliminar cliente. \n5) Buscar cliente. \n\n0) Volver al menu principal.\n\n\n>>> ")
                if tercero == "1":
                    for cliente in clientes:
                        cliente.MostrarAtributos()
                
                elif tercero == "2":
                    nuevo_cliente = Cliente.RegistrarCliente()
                    clientes.append(nuevo_cliente)
                    print("\nEl cliente se ha registrado satisfactoriamente.")
                elif tercero == "3":
                    pass

                elif tercero == "4":
                    pass
                
                elif tercero == "5":
                    pass
                
                elif tercero == "0":
                    break
                
                else:
                    print("Error, ha ingresado un valor incorrecto")
                    
        elif opcion == "4":
            pass
            
        elif opcion == "5":
            pass
        
        elif opcion == "6":
            pass
        
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Error, ha ingresado un valor incorrecto")
            
main()