# Plantilla cifrar.py

mensaje = input("Introduce el mensaje a cifrar: ")

# Calcula k de manera aleatoria
k = (len(mensaje) % 13) + 3  

# Variable para almacenar el mensaje cifrado
mensaje_cifrado = ""

# Aplica el cifrado César
for char in mensaje:
    if 'A' <= char <= 'Z':  
        nuevo_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        mensaje_cifrado += nuevo_char
    elif 'a' <= char <= 'z':  
        nuevo_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        mensaje_cifrado += nuevo_char
    else:  
        mensaje_cifrado += char

# Muestra el resultado
print("\nMensaje cifrado:", mensaje_cifrado)
print("Número de desplazamiento (k):", k)
