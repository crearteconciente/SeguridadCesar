import string


abecedarioMay= string.ascii_uppercase # trae todo el abecedario

def cifrarletra(letra, clave):
    indiceLetra= abecedarioMay.index(letra) #busca el indice de la letra
    return abecedarioMay[(indiceLetra+clave)%26] #se hace el cambio de la letra sumando la clave y con el % se busca el modulo para que no se pase de los 25 caractares

print("****************")
print("Ejercicio 1.1")
print(cifrarletra("A", 3))
print("****************\n")

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



def descifrar_frase(frase, clave):
    abecedarioMayMin = string.ascii_letters  # Mayúsculas y minúsculas
    frase_descifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMayMin:
            indiceLetra = (abecedarioMayMin.index(letra) - clave) % 52 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_descifrada += abecedarioMayMin[indiceLetra] #almacena la letra cambiada
        else:
            frase_descifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_descifrada)

print("Ejercicio 1.3")
print("Frase Desencriptada")
descifrar_frase("KROD PXQGR", 3)
print("****************\n")



print("*******PRUEBAS*********")
print("Frase Encriptada")
cifrar_fraseMay("HOLA", 3)

print("Frase Desencriptada")
descifrar_frase("CDE", 5)

print("Probar con espacios y símbolos:")
cifrar_fraseMay("¡Hola Mundo!", 3)

print("****************\n")


def cifrar_frase(frase, clave):
    abecedarioMayMin = string.ascii_letters  # Mayúsculas y minúsculas
    frase_cifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMayMin:
            indiceLetra = (abecedarioMayMin.index(letra) + clave) % 52 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_cifrada += abecedarioMayMin[indiceLetra] #almacena la letra cambiada
        else:
            frase_cifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_cifrada)

print("*****ALFABETO COMPLETO******")
print("Frase Encriptada May y Min")
cifrar_frase("ABCD abcd", 3)
print("****************\n")


print("Frase Encriptada intercaladas")
cifrar_frase("AaBbCcDd", 3)
print("****************\n")

print("Frase Encriptada intercaladas y simbolos")
cifrar_frase("AaBbCcDd !#$%&'()*+,-./:;<=>", 3)
print("****************\n")
