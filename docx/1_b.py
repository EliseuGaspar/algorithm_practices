primorial = 1

def is_primo(number: int, count: int = 0) -> int:
    for x in range(1,number+1):
        if number % x == 0:
            count += 1
    if count == 2: return number
    return None

number = int(input('Insira um nº e descubra o seu primorial: '))

for x in range(2,number+1):
    if is_primo(x):
        primorial *= x

print(f'Primorial de {number} é: {primorial}')
