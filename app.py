import random

frase = []

quien = ['el perro ','mi hermano ','el gato ','el vecino ']
accion = ['se comio ','me quemo ','vomito ','se robo ']
cuando = ['antes de clases','recien','anoche','cuando iba saliendo']
que = ['mi tarea ', 'mi laptop ', 'mis llaves ', 'mi mochila ']

def create_excuse():
    frase = quien[random.randint(0,3)] + accion[random.randint(0,3)] + que[random.randint(0,3)] + cuando[random.randint(0,3)]
    print(frase)

create_excuse()