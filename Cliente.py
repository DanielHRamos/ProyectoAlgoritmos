from funciones import validar_numero

class Cliente:
    def __init__(self, nombre, id, correo, direccion, telefono):
        self.nombre = nombre
        self.id = id
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    #Metodo para mostrar las caracteristicas de los productos
    def MostrarAtributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Correo: {self.correo}")
        print(f"Direccion: {self.direccion}")
        print(f"Telefono: {self.telefono}")
    
    
    #Metodo para registrar clientes
    def RegistrarCliente():
        while True:
            print("\nTipo de cliente:\n\n1) Cliente Natural\n2) Cliente Juridico") 
            tipo_cliente = input("\n>>> ")
            if tipo_cliente == "1" or tipo_cliente == "2":
                nombre = input("Nombre y Apellido o Razon Social: ") 
                cedula_rif = validar_numero("Cédula o RIF: ", int) 
                email = input("Correo electronico: ") 
                direccion_envio = input("Direccion de envio: ") 
                telefono = validar_numero("Telefono: ", int) 
                if tipo_cliente == "2": 
                    nombre_contacto = input("Nombre de la persona de contacto: ") 
                    telefono_contacto = validar_numero("Telefono de la persona de contacto: ", int) 
                    correo_contacto = input("Correo electronico de la persona de contacto: ") 
                    cliente = Juridico(nombre, cedula_rif, email, direccion_envio, telefono, nombre_contacto, telefono_contacto, correo_contacto) 
                else: 
                    cliente = Cliente(nombre, cedula_rif, email, direccion_envio, telefono) 
                
                return cliente 
            else: 
                print("Error, ha ingresado un valor incorrecto.")
                
                
    #Metodo para modificar clientes (No implementado en el menu)
    def ModificarCliente(self):
        self.nombre = input(f"Nombre y Apellido o Razon Social [{self.nombre}]: ") or self.nombre 
        self.id = input(f"Cedula o RIF [{self.id}]: ") or self.id 
        self.correo = input(f"Correo electronico [{self.correo}]: ") or self.correo 
        self.direccion = input(f"Direccion de envio [{self.direccion}]: ") or self.direccion 
        self.telefono = input(f"Telefono [{self.telefono}]: ") or self.telefono


#Clase Juridico creada a partir de la clase padre "Cliente" para el caso de los clientes de tipo Juridico
#Esta clase hereda los metodos de la clase Cliente agregando sus caracteristicas propias
class Juridico(Cliente):
    
    def __init__(self, nombre, id, correo, direccion, telefono, nombre_contacto, telefono_contacto, correo_contacto):
        super().__init__(nombre, id, correo, direccion, telefono)
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
    
    def MostrarAtributos(self): 
        super().MostrarAtributos()
        print(f"Nombre de Contacto: {self.nombre_contacto}") 
        print(f"Teléfono de Contacto: {self.telefono_contacto}") 
        print(f"Correo de Contacto: {self.correo_contacto}") 
        print()
        
    def ModificarCliente(self):
        super().ModificarCliente() 
        self.nombre_contacto = input(f"Nombre de la persona de contacto [{self.nombre_contacto}]: ") or self.nombre_contacto 
        self.telefono_contacto = input(f"Telefono de la persona de contacto [{self.telefono_contacto}]: ") or self.telefono_contacto 
        self.correo_contacto = input(f"Correo electronico de la persona de contacto [{self.correo_contacto}]: ") or self.correo_contacto