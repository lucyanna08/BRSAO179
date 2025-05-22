resposta = ""
soma = 0.0
itens = 0
while resposta.lower() != "fim":
    resposta = input("Para sair digite fim: ")
    try:
        numero = float(resposta)
        if numero < 0.0 or numero > 10.0:
            print("Erro: O número deve estar entre 0 e 10.")
            continue
        soma = soma + numero
        itens = itens + 1
    except ValueError:
        if resposta.lower() != "fim":
            print("Erro: Por favor, insira um número válido.")
        else:
            print("Você saiu do loop.")
    if resposta.lower() == "fim":
        break
print("a média de notas é: ", round (soma / itens,2)) 