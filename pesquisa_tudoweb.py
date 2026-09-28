# ============================================================
#  Pesquisa de Opiniao – TudoWeb Marketing
#  Autor  : Desenvolvido para a atividade escolar
#  Data   : 2026
#  Descricao: Coleta e exibe o grau de satisfacao de clientes
# ============================================================

import sys
import io

# Garante saida UTF-8 no Windows
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TOTAL_ENTREVISTADOS = 50   # Altere para 10 ao rodar o teste

SEPARADOR = "=" * 55
LINHA     = "-" * 55

def exibir_cabecalho():
    """Exibe o cabecalho da pesquisa."""
    print(SEPARADOR)
    print("   PESQUISA DE SATISFACAO - TudoWeb Marketing")
    print(SEPARADOR)
    print()

def exibir_menu_opiniao():
    """Exibe as opcoes de avaliacao disponiveis."""
    print("  Avaliacao do atendimento:")
    print("    1 - EXCELENTE")
    print("    2 - BOM")
    print("    3 - RUIM")

def obter_nome(numero_entrevistado: int) -> str:
    """Solicita e valida o nome do entrevistado."""
    while True:
        nome = input(f"  Nome do entrevistado {numero_entrevistado}: ").strip()
        if nome:
            return nome
        print("  Aviso: Por favor, informe um nome valido.\n")

def obter_idade() -> int:
    """Solicita e valida a idade do entrevistado."""
    while True:
        try:
            idade = int(input("  Idade: "))
            if 0 < idade < 130:
                return idade
            print("  Aviso: Idade invalida. Informe um valor entre 1 e 129.\n")
        except ValueError:
            print("  Aviso: Digite apenas numeros para a idade.\n")

def obter_opiniao() -> int:
    """Solicita e valida a opiniao do entrevistado (1, 2 ou 3)."""
    while True:
        try:
            exibir_menu_opiniao()
            opcao = int(input("  Sua escolha: "))
            if opcao in (1, 2, 3):
                return opcao
            print("  Aviso: Opcao invalida. Digite 1, 2 ou 3.\n")
        except ValueError:
            print("  Aviso: Digite apenas numeros.\n")

def classificar_opiniao(opcao: int) -> str:
    """Retorna o texto correspondente a opcao escolhida."""
    if opcao == 1:
        return "EXCELENTE"
    elif opcao == 2:
        return "BOM"
    else:
        return "RUIM"

def realizar_pesquisa(total: int) -> dict:
    """
    Executa a coleta de dados com 'total' entrevistados.
    Retorna um dicionario com as contagens por categoria.
    """
    contagem = {"EXCELENTE": 0, "BOM": 0, "RUIM": 0}

    for i in range(1, total + 1):
        print(f"\n{LINHA}")
        print(f"  Entrevistado {i} de {total}")
        print(LINHA)

        nome      = obter_nome(i)
        idade     = obter_idade()
        opcao     = obter_opiniao()
        avaliacao = classificar_opiniao(opcao)

        # Estrutura de decisao para incrementar os contadores
        if avaliacao == "EXCELENTE":
            contagem["EXCELENTE"] += 1
        elif avaliacao == "BOM":
            contagem["BOM"] += 1
        else:
            contagem["RUIM"] += 1

        print(f"\n  [OK] {nome} ({idade} anos) avaliou como: {avaliacao}")

    return contagem

def exibir_resultados(contagem: dict, total: int):
    """Apresenta o resumo final da pesquisa."""
    print("\n")
    print(SEPARADOR)
    print("         RESULTADO FINAL DA PESQUISA")
    print(SEPARADOR)
    print(f"  Total de entrevistados : {total}")
    print(f"  Respostas EXCELENTE    : {contagem['EXCELENTE']}")
    print(f"  Respostas BOM          : {contagem['BOM']}")
    print(f"  Respostas RUIM         : {contagem['RUIM']}")
    print(SEPARADOR)

    # Calcula e exibe percentuais
    for categoria, qtd in contagem.items():
        percentual = (qtd / total) * 100
        print(f"  {categoria:<10}: {percentual:5.1f}%")

    print(SEPARADOR)
    print()

def main():
    exibir_cabecalho()
    contagem = realizar_pesquisa(TOTAL_ENTREVISTADOS)
    exibir_resultados(contagem, TOTAL_ENTREVISTADOS)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
