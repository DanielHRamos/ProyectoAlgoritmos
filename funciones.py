import requests

def cargar_api():
    url = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json")
    if url.status_code == 200:
        return url.json()
    else:
        print("Error, no se ha podido establecer conexion con la API")

def validar_numero(prompt, tipo=float):
    valor = input(prompt)
    if tipo == int:
        while not valor.isdigit() or int(valor) < 0:
            print("Entrada invalida. Por favor, ingresa un numero valido.")
            valor = input(prompt)
        return int(valor)
    elif tipo == float:
        while not valor.replace('.', '', 1).isdigit() or float(valor) < 0:
            print("Entrada invalida. Por favor, ingresa un numero valido.")
            valor = input(prompt)
        return float(valor)
    
