print('Bem-vindo à loja do Henrique dos Santos Duarte')

# Dicionário com preços por sabor e tamanho
precos = {
    'cp': {'g': 18.00, 'm': 14.00, 'p': 9.00},
    'ac': {'g': 20.00, 'm': 16.00, 'p': 11.00}
}

total = 0

while True:
    print('\nTemos sabor cupuaçu (cp) ou açaí (ac)')
    print('Tamanho de copos G, M, P')
    print('Copo G de CP : R$18.00 ou copo G de AC : R$20.00')
    print('Copo M de CP : R$14.00 ou copo M de AC : R$16.00')
    print('Copo P de CP : R$9.00 ou copo P de AC : R$11.00')

    sabor = input('Qual sabor deseja? (cp/ac): ').lower()
    if sabor not in precos:
        print('Sabor inválido! Tente novamente.')
        continue

    tamanho = input('Qual tamanho deseja? (g/m/p): ').lower()
    if tamanho not in precos[sabor]:
        print('Tamanho inválido! Tente novamente.')
        continue

    # Adiciona o preço ao total
    preco_item = precos[sabor][tamanho]
    total += preco_item

    adc = input('Deseja mais alguma coisa? (S/N): ').lower()
    if adc != 's':
        break

print(f'Total da compra foi de R${total:.2f}')
