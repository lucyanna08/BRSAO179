senha = ""
qtdletras = 0
qtdnumeros = 0
while senha.lower() != "sair":
    senha = input("Digite a senha: ")
    if senha.lower() == "sair":
        break
    else:
        for i in range(len(senha)):
            if senha[i].isalpha():
                qtdletras += 1
            elif senha[i].isdigit():
                qtdnumeros += 1
        if qtdletras >= 8 and qtdnumeros >= 1:
            print("Senha [",senha,"] é válida")
            break
        else:
            print("Senha incorreta, tente novamente.")