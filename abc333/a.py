import psutil


def consumo_de_memoria():
    memory_info = psutil.Process().memory_info()
    consumo_em_megabytes = memory_info.rss / (1024 ** 2)
    print(f"Consumo de memória: {consumo_em_megabytes:.2f} MB")

def main():
    value = int(input("Insira um valor entre 1 e 9): "))
    
    if not 1 <= value <= 9:
        print('Valor fora da órbita do programa!')
        consumo_de_memoria()
        exit(0)

    print(F"{value}"*value)
    consumo_de_memoria()

if __name__ == '__main__':
    main()
