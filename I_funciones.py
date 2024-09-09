#isaac antonio Jimenez Hernandez
print("Maneho de funciones v1")
def hola_mundo():
    print("hola aqui estoy dentro de la funcion")

def la_mensa(msgn):
    print(msgn)

def EscribeNC(nombre,Apellido):
    print(nombre, Apellido)
    print(f"tu nombre completo es: {nombre} {Apellido}")

def suma2numeros(n1,n2):
    S=n1+n2
    return f"la suma de {n1} + {n2} es:",S

# llamando a la funcion 
hola_mundo()
la_mensa("te la lavas")# llama a la mensa
la_mensa("el profe me sorprendio mensajeando con mi vieja 💋")# llama a la mensa
EscribeNC("isaac goku lionel cristiano ronaldiño javier neymar","jimenez")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,43))