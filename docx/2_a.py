distancias = []

try:
    def check_value(number: int):
        if -10000 < int(number) < 10000:
            return None
        print('Valor fora da órbita do programa!')
        exit(0)

    def calcular_distancia(Xa: int, Xb: int, Ya: int, Yb: int) -> None:
        distancia = abs(Xa - Xb) + abs(Ya - Yb)
        distancias.append(distancia)

    casos = int(input('Insira o numeros de casos de teste: '))

    if not 1 <= casos <= 10000:
        print('Valor fora da órbita do programa!')
        exit(0)

    for x in range(casos):

        x1, y1, x2, y2 = input(': ').split(' ')

        (check_value(x1), check_value(x2), check_value(y1), check_value(y2))

        calcular_distancia(int(x1),int(x2),int(y1),int(y2))
        
    for distancia in distancias:
        print(distancia)

except:
    print('Ocorreu um durante a execução do programa!')

