print("funciones creadas por el usuario")
# las funciones 
def Mi_lista():
    amigos=["Ronaldo Nazario","Lionel Messi","Pele"]
    for yo in amigos:
        print(yo)
print("")
print("esta es mi lista de amigos: ")
Mi_lista()  
def Mi_tupla():
    carros=("mustang","porche","challenguer helcat")
    for modificados in carros:
        print(modificados)
# llamadas a funciones 
print("")
print("esta es mi tupla de carros modificados: ")
Mi_tupla()  
def Mi_diccionario():
    propiedad={
            "color":"rojo",
            "pisos":"30",
            "vecino":"lionel messi"}
    for lugar in propiedad:
        print(lugar)
# llamadas a funciones 
print("")
print("este es mi diccionario: ")
Mi_diccionario()
def Mi_conjunto():
    propiedades={"miami","sau paulo","vaticano","dubai"}
    for lugar in propiedades:
        print(lugar)
# llamadas a funciones 
print("")
print("este es mi conjunto ")
Mi_conjunto()