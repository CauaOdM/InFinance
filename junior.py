import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def dados_calculate(acao):
    print(f"Processando {acao}...")

    dados = yf.download(acao,period="6mo", progress=False)

    if len(dados)==0:
        print("Dados não encontrados!")
        return
    
    precos = dados['Close'].values.flatten()

    #Média móvel de 20 dias:

    window = 20
    weights = np.ones(window)/window
    media_movel = np.convolve(precos,weights, mode='valid')

    print("-="*30)
    print("Gerando gráfico...")
    print("-="*30)

    plt.figure(figsize=(10, 5))

    #Preço real

    plt.plot(dados.index[window-1:], precos[window-1:], label='Preço Real', color='blue', alpha=0.5)

    #Média móvel

    plt.plot(dados.index[window-1:], media_movel, label='Média Móvel (20d)', color='orange', linewidth=2)

    plt.title(f'Análise de {acao}')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    acao = input("Digite o ticker (ex: PETR4.SA): ").upper()
    dados_calculate(acao)