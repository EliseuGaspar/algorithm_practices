def calcular_camisolas_a_comprar(planos: str):
    count = 0
    if '20' in planos:
        planos = planos+'2'
    for plano in planos:
        if plano == '2':
            count += 1
        elif plano == '0':
            count -= 1 if count >= 1 else 0
    return count

try:
    dias = int(input('Oí! Programação para quantos dias?: '))
except:
    print('Valor fora da órbita do programa! Insira um inteiro da proxima vez.')
    exit(0)

try:
    camisetas_lisas = int(input('Quantas camisetas lisas tu tens?: '))
except:
    print('Valor fora da órbita do programa! Insira um inteiro da proxima vez.')
    exit(0)

try:
    planos = input('Insira agora os planos: ')
    int(planos)
except:
    print('Valor fora da órbita do programa! Insira um inteiro da proxima vez.')
    exit(0)

camisetas_logo = calcular_camisolas_a_comprar(planos)

print(f'Comprarás {camisetas_logo} camisetas logo.')


