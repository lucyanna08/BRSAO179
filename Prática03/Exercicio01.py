while True:
    try:
        print("informe um número")
        numero1 = float(input())
        print("informe outro número")
        numero2 = float(input())
        print("informe a operação:  +(adicao), -(subtracao), *(multiplicacao) ou /(divisao)")
        operacao = input()
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        continue  # Reinicia o loop se houver erro na entrada
    if operacao in ["+", "-", "*", "/"]:
        break  # Sai do loop
    else: 
        print("Operação inválida, tente novamente.")
    
try:
       
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
except ZeroDivisionError:
        # Código para lidar com a exceção ZeroDivisionError
        print("Erro: Divisão por zero não é permitida.")
except ValueError as e:
        print(e)
finally:
    if 'resultado' in locals():
        print(f"O resultado da operação {operacao} entre {numero1} e {numero2} é: {resultado}")
    else:
        print("Nenhum resultado a exibir.")
        print("Fim do programa")

