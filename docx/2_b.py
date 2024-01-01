primorial = 1
numeros = []

def is_primo(number: int, count: int = 0) -> int:
    for x in range(1,number+1):
        if number % x == 0:
            count += 1
    if count == 2: return number
    return None

print('Insira N nºs e descubra o seu primorial. Para fechar insira 0.')

while True:

    number = int(input(': '))

    if number == 0:
        if numeros == []:
            print('Precisas inserir pelo menos um número natural diferente de 0.')
            exit(0)

        for num in numeros:
            print(f'R: {num}')
        exit(0)
    
    if number < 0:
        print('Valor fora da órbita do programa... insira um número natural.')
        exit(0)

    for x in range(2,number+1):
        if is_primo(x):
            primorial *= x
    
    numeros.append(primorial)
    primorial = 1

