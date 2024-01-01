

def show_as(diametro: int, a: str = 'A') -> str:
    for x in range(diametro):
        a += 'a'
    return a

raio = int(input('Insira o raio do instrumento: '))

diametro = (raio * 2) + (raio * 2)

print(f'{show_as(diametro)}h')
