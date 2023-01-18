import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

lista_1 =  [elemento for elemento in set(json.dumps(repetidos)) if elemento.isdigit()]  # Punto 1
lista_2 =  [elemento for elemento in set(json.dumps(r)) if elemento in lista_1]  # Punto 2
diccionario = json.loads(d_str)  # Punto 3