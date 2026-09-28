# Pesquisa de Opiniao - TudoWeb Marketing
# Programa que coleta e exibe o retorno de uma pesquisa de atendimento ao cliente

excelente = 0
ruim = 0

for i in range(1, 51):
    print("\n--- Entrevistado", i, "de 50 ---")

    nome = input("Nome: ")
    idade = input("Idade: ")

    print("Avaliacao do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opcao (1, 2 ou 3): "))

    if opiniao == 1:
        excelente = excelente + 1
        print("Avaliacao registrada: EXCELENTE")
    elif opiniao == 2:
        print("Avaliacao registrada: BOM")
    else:
        ruim = ruim + 1
        print("Avaliacao registrada: RUIM")

print("\n========================================")
print("       RESULTADO FINAL DA PESQUISA")
print("========================================")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("========================================")
