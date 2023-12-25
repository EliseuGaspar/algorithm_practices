import psutil

pentagono_circular = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
pentagono = ['a', 'b', 'c', 'd', 'e']

def calcular_distancia(primeiro: str, segundo: str):
    if primeiro != 'e' and segundo != 'a':
        return abs(pentagono.index(primeiro) - pentagono.index(segundo))
    else:
        return abs(pentagono.index(primeiro) - ''.join(pentagono_circular).rfind(segundo))

try:
    s1, s2 = input('Insira a primeira distância: ').lower()
except ValueError:
    print('Insira apenas duas letras!')
    exit(0)

try:
    t1, t2 = input('Insira a segunda distância: ').lower()
    if t1 not in pentagono or t2 not in pentagono:
        print('Valor fora da órbita do programa!')
        exit(0)
except ValueError:
    print('Insira apenas duas letras!')
    exit(0)

distancia1 = calcular_distancia(s1, s2)
distancia2 = calcular_distancia(t1, t2)

if distancia1 == distancia2:
    print('Yes')
else:
    print('No')

memory_info = psutil.Process().memory_info()
consumo_em_megabytes = memory_info.rss / (1024 ** 2)
print(f"Consumo de memória: {consumo_em_megabytes:.2f} MB")
