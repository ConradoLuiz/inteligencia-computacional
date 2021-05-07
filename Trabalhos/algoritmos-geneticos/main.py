import numpy as np 
import matplotlib.pyplot as plt 
import math

N_EXPERIMENTOS = 20
K = 22
N_POPULACAO = 100
N_GERACOES = 40

crossover_rate = .65
mutation_rate = .008

x_min = -100
x_max = 100

def decode(number):
    top = x_max - x_min
    bottom =  (2**K) - 1
    
    return number * (top/bottom) + x_min

def f6(x, y):
    top = math.sin( math.sqrt(x**2 + y**2) )**2 - 0.5
    bottom = (1.0 + 0.001*(x**2 + y**2))**2

    return 0.5 - (top/bottom)

def binToDecimal(binary_array):
    str_bin = ''.join([str(b) for b in binary_array])
    decimal = int(str_bin, 2)

    return decimal

def avalia(populacao):
    aptidao = [0] * len(populacao)

    melhor_aptidao = -math.inf
    melhor_individuo = -1
    for i, dna in enumerate(populacao):

        x = dna[:K]
        y = dna[K:]

        x = binToDecimal(x)
        y = binToDecimal(y)

        x = decode(x)
        y = decode(y)

        apt = f6(x, y)

        if apt > melhor_aptidao:
            melhor_aptidao = apt
            melhor_individuo = i

        aptidao[i] = apt

    return aptidao, populacao[melhor_individuo]
    

def roleta(populacao, aptidao):

    aptidao_acc = [0] * len(aptidao)
    for i, apt in enumerate(aptidao):
        aptidao_acc[i] = apt + aptidao_acc[max(i-1,0)]
    
    nova_populacao = []
    for i, _ in enumerate(populacao):
        rand = np.random.uniform(low=0, high=max(aptidao_acc))
        escolhido = None
        for j, apt in enumerate(aptidao_acc):
            if apt > rand:
                escolhido = j
                break
        nova_populacao.append( populacao[escolhido] )
    
    return nova_populacao

def mutacao(populacao):
    for i, dna in enumerate(populacao):
        rand = np.random.rand()
        if rand < mutation_rate:
            novo_bit = np.random.randint(2)
            dna[-1] = novo_bit
    
    return populacao

def crossover(populacao):
    nova_populacao = []
    
    for i in range(len(populacao)//2):

        dna1 = populacao[i]
        dna2 = populacao[i+1]

        if np.random.rand() > crossover_rate:
            nova_populacao.append(dna1)
            nova_populacao.append(dna2)
            continue
        
        ponto_de_corte = np.random.randint(len(dna1))

        novo1 = [*dna1[:ponto_de_corte], *dna2[ponto_de_corte:]]
        novo2 = [*dna2[:ponto_de_corte], *dna1[ponto_de_corte:]]

        nova_populacao.append(novo1)
        nova_populacao.append(novo2)

    return nova_populacao

def encontrarN9(numero):
    count = 0
    for n in str(numero).split('.')[1]:
        if int(n) != 9:
            break
        count += 1
    return count


if __name__ == '__main__':

    medias_experimentos = []
    medias_9_experimentos = []
    for EXPERIMENTO in range(N_EXPERIMENTOS):
        POPULACAO = [
            np.random.randint(2, size=K*2) for _ in range(N_POPULACAO)
        ]

        media_aptidao = []
        media_9 = []
        for GERACAO in range(N_GERACOES):
            
            aptidao, melhor_individuo = avalia(POPULACAO)

            noves = [encontrarN9(n) for n in aptidao]
            
            media = np.mean(aptidao)
            media_noves = np.mean(noves)
            
            media_aptidao.append(media)
            media_9.append(media)

            POPULACAO = roleta(POPULACAO, aptidao)
            
            POPULACAO = mutacao(POPULACAO)
            POPULACAO = crossover(POPULACAO)

            # ELITISMO
            posicao_aleatoria = np.random.randint(len(POPULACAO))
            POPULACAO[posicao_aleatoria] = melhor_individuo
        
        medias_experimentos.append(media_aptidao)
        medias_9_experimentos.append(media_9)

        print('-------------------------------------')
        print(f'EXPERIMENTO {EXPERIMENTO}')
        print(f'\tMAX APTIDAO: {max(media_aptidao)}')
        print(f'\tMAX 9: {max(media_9)}')
        print(f'\tMÉDIA APTIDAO: {np.mean(media_aptidao)}')
        print('-------------------------------------')
        print('-------------------------------------\n\n')

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for i, medias in enumerate(medias_experimentos):
        _range = range(N_GERACOES)
        ax1.plot(_range, medias, i)
        ax2.plot(_range, medias_9_experimentos[i], i)

    fig.suptitle('Algoritmo Genético (Cada linha é um experimento)', fontsize=14)

    ax1.set_ylim([0.4, 1.1])
    ax1.set_xlabel('Geração')
    ax1.set_ylabel('Aptidão')
    ax1.set_title("Aptidão por geração")

    ax2.set_ylim([0.4, 1.3])
    ax2.set_xlabel('Geração')
    ax2.set_ylabel('N° 9')
    ax2.set_title("N° 9 depois da virgula por geração")
    plt.show()