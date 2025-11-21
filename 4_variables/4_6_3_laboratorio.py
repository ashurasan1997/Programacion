"""
3. Ejercicios para el tipo de dato str (texto)
Empresa: "CustomerFirst" — Call Center de atención al cliente
Situación:
El supervisor necesita registrar el nombre del agente y el nombre del cliente atendido.
Ejercicio:
Pide al usuario:
Nombre del agente
 
Nombre del cliente
 
Objetivo:
Mostrar un mensaje combinando textos.
"""
# Solicitar datos al usuario GPT
agente = input("Ingrese el nombre del agente: ")
cliente = input("Ingrese el nombre del cliente: ")

# Mensaje combinado
mensaje = "El agente " + agente + " ha atendido al cliente " + cliente + "."

# Mostrar resultado
print(mensaje)
#carlos
nombre_agente: str = input("Ingrese el nombre del agente: ")
nombre_cliente: str = input("Ingrese el nombre del cliente: ")
print("El agente: ", nombre_agente, " ha atendido al cliente: ", nombre_cliente + ".")
