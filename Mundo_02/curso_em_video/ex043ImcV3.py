#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

historico_imc = []  # Lista para armazenar os resultados

while True:
    print('-' * 20)
    peso = float(input('Peso (kg): '))
    altura = float(input('Altura (m): '))
    
    imc = peso / (altura ** 2)
    
    # Armazenando o valor na lista
    historico_imc.append(imc)
    
    print(f'IMC calculado: {imc:.1f}')
    
    # Pergunta se quer continuar
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

print('\n' + '=' * 30)
print('      RELATÓRIO FINAL')
print('=' * 30)

# Mostrando os dados armazenados
print(f'Total de pessoas consultadas: {len(historico_imc)}')
print(f'Maior IMC registrado: {max(historico_imc):.1f}')
print(f'Menor IMC registrado: {min(historico_imc):.1f}')
print(f'Média dos IMCs: {sum(historico_imc)/len(historico_imc):.1f}')