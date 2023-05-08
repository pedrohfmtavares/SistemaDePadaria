import time

estoqueQueijo = 50.0
estoquePao = 50.0



queijoPreco = 24.90
farinhaDeTrigoPreco = 6.99
produtosUN = ["farinha de trigo"]
produtosKG = ["pao", "queijo"]


espacoEmBranco = " "
sucesso = "Venda registrada com sucesso!"


precosKG = {produtosKG[0]: estoquePao, produtosKG[1]: estoqueQueijo}
precosUN = {produtosUN[0]: float(20)}


valoresKG = precosKG.values()
valoresUN = precosUN.values()


dinheiro = 0
faturamento = 0



while True:
    registraProduto = input('Qual produto deseja registrar para a venda? \n')
    if registraProduto in produtosKG:
        registraQuilo = float(input(f'Quantos quilogramas deseja registrar para a venda? \n '))
        dinheiro = registraQuilo * queijoPreco
        faturamento += dinheiro 
        if registraProduto == "pao":
            precosKG.update({produtosKG[0]: estoquePao - registraQuilo})
            estoquePao -= registraQuilo
        elif registraProduto == "queijo":
            precosKG.update({produtosKG[1]: estoqueQueijo - registraQuilo})
            estoqueQueijo -= registraQuilo
        print(sucesso)
        print(espacoEmBranco)
    elif registraProduto in produtosUN:
        registraUnidade = float(input(f'Quantas unidades desse produto deseja registrar para a venda? \n '))
        if registraProduto == "farinha de trigo":
            dinheiro = registraUnidade * farinhaDeTrigoPreco
            faturamento += dinheiro
        print(sucesso)
        print(espacoEmBranco)
    else:
        print("Esse produto não existe ou não está disponível na nossa loja")
        print(espacoEmBranco)

    while True:
        voltar = input('Para registrar um novo produto,digite "y",para fechar o caixa,digite "n" ')

        if voltar == "y" or voltar == "Y" or voltar == "n" or voltar == "N":
            break
        else:
            print('opcão inválida,tente novamente! ')
            print(espacoEmBranco)

    if voltar == "n" or voltar == "N":
        break

tempo = 3
print(f'Fechando o caixa em {tempo} segundos... ')
tempo -= 1
time.sleep(1)

print(f'Fechando o caixa em {tempo} segundos... ')
tempo -= 1 
time.sleep(1)

print(f'Fechando o caixa em {tempo} segundo... ')
time.sleep(1)


print(f'O faturamento total do dia foi de {faturamento:,.2f}R$')
        