#Variables 
filas_tablero=10
columnas_tablero=10

#Creo diccionario con todos los barcos del tipo que son del 1 al cuatro vemos que son 1, del 5 al 7 con un 2 y del 8 al 9 con un 3 el 10 con un 4
barcos ={
    "barco_1": 1,
    "barco_2": 1,
    "barco_3": 1,
    "barco_4": 1,
    "barco_5": 2,
    "barco_6": 2,
    "barco_7": 2,
    "barco_8": 3,
    "barco_9": 3,
    "barco_10": 4
}
#HE UTILIZADO ESTO PARA NOMBRAR A AGUA BARCO IMPACTO Y FALLO DE PRIMERAS
agua=0
barco=1
impacto=2
fallo=3

#ESTO LO HE PUESTO POR SI DESPUES CUANDO FUNCIONE BIEN LE DAMOS ALGO DE FORMATO MAS BONITO
simbolos = {
    0: "💧", # Agua
    1: "🚢", # Barco
    2: "💥", # Impacto
    3: "😞"  # Fallo
}