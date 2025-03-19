[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eZ_U6wFI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18771136)
# Práctica 2. Estructura de control iterativa

Plantilla para el ejercicio de la práctica 2

# Cifrado César en Python  

## Presentación del problema  
En esta práctica, se nos pidió desarrollar un programa en Python que implemente el **Cifrado César**, un método de encriptación utilizado por Julio César para proteger sus mensajes. Este cifrado consiste en **desplazar cada letra del alfabeto un número `k` de posiciones**.  

Por ejemplo, si `k = 3`:  
- **A** se convierte en **D**  
- **B** en **E**  
- **C** en **F**  
- ...  
- **X** se convierte en **A**, **Y** en **B** y **Z** en **C**.  

El programa debe cifrar un mensaje con un desplazamiento `k` aleatorio dentro de un rango (3-15) y, posteriormente, descifrarlo conociendo `k`.  

---

## Diseño del algoritmo  
Para diseñar el algoritmo, seguimos estos pasos:  
1. **Solicitar un mensaje** al usuario.  
2. **Calcular `k`** de manera pseudoaleatoria a partir de la longitud del mensaje.  
3. **Recorrer el mensaje** y modificar cada letra según el desplazamiento `k`:  
   - Si es **mayúscula**, se ajusta dentro del rango `'A'` a `'Z'`.  
   - Si es **minúscula**, se ajusta dentro del rango `'a'` a `'z'`.  
   - Si no es una letra, **no se modifica**.  
4. **Mostrar el mensaje cifrado** y el valor de `k`.  
5. Para descifrar, se repite el proceso, pero **restando `k`** en lugar de sumarlo.  

---

## Implementación en Python  
La implementación utiliza:  
- `input()` para recibir el mensaje.  
- `print()` para mostrar el resultado.  
- Un ciclo `for` para recorrer el texto y modificar los caracteres.  
- Condicionales `if` para diferenciar letras mayúsculas, minúsculas y otros caracteres.  
- Las funciones `ord()` (que obtiene el código ASCII de un carácter) y `chr()` (que convierte un código en carácter) para modificar letras dentro del alfabeto sin afectar otros símbolos.  

El código es claro y sencillo, permitiendo que cualquier persona comprenda cómo funciona este método de cifrado.
