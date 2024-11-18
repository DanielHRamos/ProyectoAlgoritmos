from funciones import validar_numero


class Producto:
    def __init__(self, id, nombre, descripcion, precio, categoria, stock, vehiculo_compatible):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.vehiculo_compatible = vehiculo_compatible
        
    #Metodo para mostrar detalles de los productos
    
    def MostrarAtributos(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")
        print(f"Stock: {self.stock}")
        print(f"Vehiculo compatible: {self.vehiculo_compatible}")
        print()
        print()
    
    #Metodo para agregar productos a la lista de productos
    
    def AgregarProducto(lista):
        
        id = len(lista) + 1
        nombre = input("Introduce el nombre del producto: ") 
        descripcion = input("Introduce la descripción del producto: ") 
        precio = validar_numero("Introduce el precio del producto: ", float)
        categoria = input("Introduce la categoría del producto: ") 
        stock = validar_numero("Introduce el stock del producto: ", int) 
        vehiculo_compatible = input("Introduce el vehículo compatible del producto (Opcional): ") 
        nuevo_producto = Producto(id, nombre, descripcion, precio, categoria, stock, vehiculo_compatible) 
        lista.append(nuevo_producto) 
        print(f"Producto {nombre} ha sido añadido al inventario.")
    
    #Metodo para eliminar productos de la lista
    
    def EliminarProducto(lista, id):
        
        producto_encontrado = None 
        for producto in lista: 
            if producto.id == id: 
                producto_encontrado = producto 
                break 
        if producto_encontrado: 
            lista.remove(producto_encontrado) 
            print(f"El producto con ID {id} ha sido eliminado.") 
        else: 
            print(f"No se encontró ningún producto con ID {id}.")
    
    #Metodo para modificar productos de la lista
    
    def ModificarProducto(lista, id):
        
        producto_encontrado = None 
        for producto in lista: 
            if producto.id == id: 
                producto_encontrado = producto 
                break 
        if producto_encontrado: 
            print("\nIngrese los nuevos valores. Si no desea cambiar un campo, simplemente presione Enter.") 
            nombre = input(f"Nombre actual ({producto_encontrado.nombre}): ") or producto_encontrado.nombre 
            descripcion = input(f"Descripción actual ({producto_encontrado.descripcion}): ") or producto_encontrado.descripcion 
            precio = input(f"Precio actual ({producto_encontrado.precio}): ") 
            precio = float(precio) if precio else producto_encontrado.precio 
            categoria = input(f"Categoría actual ({producto_encontrado.categoria}): ") or producto_encontrado.categoria 
            stock = input(f"Stock actual ({producto_encontrado.stock}): ") 
            stock = int(stock) if stock else producto_encontrado.stock 
            vehiculo_compatible = input(f"Vehículo compatible actual ({producto_encontrado.vehiculo_compatible}): ") or producto_encontrado.vehiculo_compatible
        
            producto_encontrado.nombre = nombre 
            producto_encontrado.descripcion = descripcion 
            producto_encontrado.precio = precio 
            producto_encontrado.categoria = categoria 
            producto_encontrado.stock = stock 
            producto_encontrado.vehiculo_compatible = vehiculo_compatible 
            
            print(f"El producto ha sido modificado.")
        
        else: 
            print(f"No se encontró ningún producto con el ID {id}.")

    #Metodo para buscar productos de la lista mediante filtros
                
    def FiltrarProductos(productos, criterio, valor): 
        
        if criterio == "nombre": 
            for producto in productos: 
                if producto.nombre.lower() == valor.lower(): 
                    return [producto] 
        elif criterio == "categoria": 
            resultado = [] 
            for producto in productos: 
                if producto.categoria.lower() == valor.lower(): 
                    resultado.append(producto)
            return resultado 
        elif criterio == "disponibilidad": 
            resultado = [] 
            for producto in productos: 
                if producto.stock == int(valor):
                    resultado.append(producto) 
            return resultado 
        elif criterio == "precio": 
            resultado = [] 
            for producto in productos: 
                if producto.precio == float(valor): 
                    resultado.append(producto) 
            return resultado 
        return []