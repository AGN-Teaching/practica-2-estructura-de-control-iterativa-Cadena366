# Plantilla descifrar.py


mensaje_cifrado = input("Introduce el mensaje cifrado: ")
k = int(input("Introduce el número de desplazamiento (k): "))

# Variable para almacenar el mensaje descifrado
mensaje_descifrado = ""

# Aplico el cifrado inverso
for char in mensaje_cifrado:
    if 'A' <= char <= 'Z':  
        nuevo_char = chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        mensaje_descifrado += nuevo_char
    elif 'a' <= char <= 'z':  
        nuevo_char = chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        mensaje_descifrado += nuevo_char
    else:  
        mensaje_descifrado += char

# Mostramos el resultado
print("\nMensaje descifrado:", mensaje_descifrado)