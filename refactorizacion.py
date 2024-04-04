def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('La puntuación debe ser un número.')

def mostrar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: punto de evaluación e ingresar comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Terminación')
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            ingresar_puntuacion_y_comentario()
        elif num == 2:
            mostrar_resultados()
        elif num == 3:
            print('Terminación.')
            break
        else:
            print('Introduzca de 1 a 3')
    else:
        print('Introduzca de 1 a 3')