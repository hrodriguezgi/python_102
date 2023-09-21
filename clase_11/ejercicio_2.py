# Definición de la clase Carro
____ Carro:
    # Constructor de la clase
    def __init__(self, marca, modelo, ____, ____):
        self.marca = marca
        self.modelo = modelo
        self.____ = anio
        self.____ = color
        self.encendido = False  # El carro comienza apagado
    
    # Método para encender el carro
    def encender(____):
        if not ____.encendido:
            ____.encendido = True
            print("El carro está encendido.")
        else:
            print("El carro ya está encendido.")
    
    # Método para apagar el carro
    def apagar(____):
        if ____.encendido:
            ____.encendido = False
            print("El carro está apagado.")
        else:
            print("El carro ya está apagado.")
    
    # Método para obtener información del carro
    def obtener_informacion(____):
        estado = "encendido" if self.____ else "apagado"
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Color: {self.color}, Estado: {estado}"

# Creación de un objeto de la clase Carro
mi_carro = ____("Toyota", "Camry", 2022, "Azul")

# Encendemos el carro
mi_carro.____

# Obtener información del carro
print("Información del Carro:")
print(mi_carro.____)

# Apagamos el carro
mi_carro.____
