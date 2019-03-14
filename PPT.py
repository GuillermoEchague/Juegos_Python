import random

opciones=['Piedra','Papel','Tijeras']
magia=random.randint(0,2)
compu=opciones[magia]
print("Elección de la computadora",compu)
tu=input("Opción: ")
print("Tu selección fue: ",tu)

if(tu==compu):
    print("Empate!")

if (tu=='Tijeras'):
    if(compu=='Papel'):
        print("Ganaste!")
    if(compu=='Piedra'):
        print("Perdiste! :( ")
if (tu=='Papel'):
    if(compu=='Piedra'):
        print("Ganaste!")
    if(compu=='Tijeras'):
        print("Perdiste! :( ")
if (tu=='Piedra'):
    if(compu=='Tijeras'):
        print("Ganaste!")
    if(compu=='Papel'):
        print("Perdiste! :( ")
