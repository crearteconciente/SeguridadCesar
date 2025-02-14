def cifrar_fraseMay(frase, clave):
    frase=frase.upper() #transforma la frase a mayusculas
    frase_cifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMay:
            indiceLetra = (abecedarioMay.index(letra) + clave) % 26 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_cifrada += abecedarioMay[indiceLetra] #almacena la letra cambiada
        else:
            frase_cifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_cifrada)

print("Ejercicio 1.2")
print("Frase Encriptada ")
cifrar_fraseMay("¡Hola Mundo!", 3)
print("****************\n")
