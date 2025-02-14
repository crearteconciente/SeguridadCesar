import string

#ejercicio 1.1 Cifrar una Letra
abecedarioMay= string.ascii_uppercase # trae todo el abecedario

def cifrarletra(letra, clave):
    indiceLetra= abecedarioMay.index(letra) #busca el indice de la letra
    return abecedarioMay[(indiceLetra+clave)%26] #se hace el cambio de la letra sumando la clave y con el % se busca el modulo para que no se pase de los 25 caractares

print("****************")
print("Ejercicio 1.1 Cifrar una Letra")
print(cifrarletra("A", 3))
print("****************\n")

#ejercicio 1.2 Cifrar un Mensaje Completo

def mensajeCompleto(frase, clave):    # Convertir todo a mayúsculas para evitar errores
    frase = frase.upper() 
    frase_cifrada = ""

    for letra in frase:
        if letra in abecedarioMay:
            frase_cifrada += cifrarletra(letra, clave)  # almacena la frase completa
        else:   
            frase_cifrada += letra #almacena la letra cambiada
    return frase_cifrada  # Devuelve la frase cifrada

print("****************")
print("Ejercicio 1.2 Cifrar un Mensaje Completo")
print(mensajeCompleto("CONTRASEÑA SEGURA",3))
print("****************\n")


#Ejercicio 1.3 descrifrar codigo

def descifrar_frase(frase, clave):
    abecedarioMayMin = string.ascii_letters  # Mayúsculas y minúsculas
    frase_descifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMay:
            indiceLetra = (abecedarioMay.index(letra) - clave) % 26 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_descifrada += abecedarioMay[indiceLetra] #almacena la letra cambiada
        else:
            frase_descifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_descifrada)

print("Ejercicio 1.3  Descifrar un Mensaje")
descifrar_frase("FRQWUDVHÑD VHJXUD", 3)
print("****************\n")


#Ejercicio 1.4 pruebas
print("Ejercicio 1.4  Pruebas")
print(mensajeCompleto("HOLA",3))
descifrar_frase("CDE", 5)
print(mensajeCompleto("¡Hola Mundo!",3))


#P2: Implementación Paso a Paso (Cifrado extendido) 

#3.1 Integrando mayúsculas y minúsculas [Con prubas]

def cifrar_frase(frase, clave):
    abecedarioMayMin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # Mayúsculas y minúsculas
    frase_cifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMayMin:
            indiceLetra = (abecedarioMayMin.index(letra) + clave) % 52 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_cifrada += abecedarioMayMin[indiceLetra] #almacena la letra cambiada
        else:
            frase_cifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_cifrada)

print("\n*****ALFABETO COMPLETO******")
print("3.1 Integrando mayúsculas y minúsculas")
cifrar_frase("ABCDabcd", 3)
print("****************\n")


#3.2 Intercalando mayúsculas y minúsculas [Con prubas] (33 pts)
def cifrar_frase_intercalado(frase, clave):
    abecedarioMayMin = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    frase_cifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMayMin:
            indiceLetra = (abecedarioMayMin.index(letra) + clave) % 52 #transforma la letra a la nueva letra 52 es la cantidad de letras con mayusculas y minusculas
            frase_cifrada += abecedarioMayMin[indiceLetra] #almacena la letra cambiada
        else:
            frase_cifrada += letra  # si no esta en el abecedario es un caracter

    print(frase_cifrada)

print("3.2 Intercalando mayúsculas y minúsculas")
cifrar_frase_intercalado("AaBbCcDd", 3)
print("****************\n")

#3.2 Usando simbolos 
def cifrar_frase_simbolos(frase, clave):
    abecedarioMayMinSim = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    frase_cifrada = ""  # Variable para almacenar la frase cifrada

    for letra in frase:
        if letra in abecedarioMayMinSim: 
            indiceLetra = (abecedarioMayMinSim.index(letra) + clave) % 83
            frase_cifrada += abecedarioMayMinSim[indiceLetra]  # almacena la letra cambiada
        else:
            frase_cifrada += letra  # Si no está en el abecedario, lo deja igual

    print(frase_cifrada)

print("3.3 Usando simbolo")
cifrar_frase_simbolos("AaBbCcDd  !#$%", 3)
print("****************\n")