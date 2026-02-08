#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar cotacao em tempo real.
import requests 

def buscar_cotacao():
    try:
        # Acessa a API de cotações
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        requisicao = requests.get(url)
        dados = requisicao.json()
        
        # Extrai o valor de compra (bid) do dólar
        return float(dados['USDBRL']['bid'])
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

# --- Fluxo Principal ---
cotacao_atual = buscar_cotacao()

if cotacao_atual:
    dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
    conversao = dinheiro / cotacao_atual

    print("-" * 30)
    print(f"Cotação atual do Dólar: R$ {cotacao_atual:.2f}")
    print(f"Com R$ {dinheiro:.2f} reais, você consegue comprar $ {conversao:.2f} dólares.")
    print("-" * 30)
else:
    print("Não foi possível realizar a conversão agora.")