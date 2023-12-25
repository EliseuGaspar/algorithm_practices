preco_produtos = []
quantidades = []
total = 0

print('Insira por favor as seguintes informações antes de comprares.')

quantidade_produtos = int(input("Quant.d'Produtos que comprarás: "))
taxa = int(input("Taxa de envio: "))
cobranca = int(input("Valor de cobrança: "))

for x in range(int(quantidade_produtos)):
    preco_produto_e_quantidade = input('Insira os valore do produto e a quantidade: \n')
    preco_produtos.append(preco_produto_e_quantidade[:preco_produto_e_quantidade.find(' ')])
    quantidades.append(preco_produto_e_quantidade[preco_produto_e_quantidade.find(' ')+1:])

for indice in range(len(preco_produtos)):
    total += int(preco_produtos[indice]) * int(quantidades[indice])

if total <= taxa:
    total += cobranca

print(f'Valor a cobrar: {total} AKZ')
