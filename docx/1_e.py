P = []
Q = []
Sequence = set()

def sequence():
    for b in range(1,100):
        for a in range(2,11):
            data = b ** a
            if data <= 1000000000:
                Sequence.add(data)
    #print(sorted(Sequence))

sequence()

def define_case(p: int, q: int, case: int, count: list = [0,[]]):
    for ii in range(p,q):
        for x in range(2,10):
            data = ii ** x
            if data in Sequence and data <= q:
                count[0] += 1 if data not in count[1] else 0
                count[1].append(data)
    print(f'case{case}: {count[0]}')

T = int(input('Insira o nº casos a testar: '))
print('Insira os valores P e Q')

for x in range(T):
    P_ , Q_ = input(': ').split(' ')

    if 1 <= int(P_) <= int(Q_):
        P.append(int(P_))
    else:
        print('O valor inserido está fora da órbita do programa!')
    if (int(P_) <= int(Q_) <= 1000000000):
        Q.append(int(Q_))
    else:
        print('O valor inserido está fora da órbita do programa!')

for y in range(T):
    define_case(P[y],Q[y],y+1)