# ============================================================
#  TESTE – Pesquisa de Opinião TudoWeb (10 entrevistados)
#  Simula respostas automáticas para validar o programa
# ============================================================

from io import StringIO
import sys

# Dados simulados de 10 entrevistados:
# Cada linha: nome, idade, opinião (1=EXCELENTE, 2=BOM, 3=RUIM)
ENTRADAS_SIMULADAS = """Ana Lima
28
1
Carlos Souza
35
2
Maria Oliveira
22
1
João Silva
45
3
Fernanda Costa
30
1
Rafael Mendes
27
2
Luciana Pereira
33
3
Bruno Santos
41
1
Patrícia Rocha
25
2
Eduardo Alves
38
1
"""

def main():
    # Redireciona stdin para simular digitação automática
    sys.stdin = StringIO(ENTRADAS_SIMULADAS)

    # Importa e executa com 10 entrevistados
    import pesquisa_tudoweb as pw
    pw.TOTAL_ENTREVISTADOS = 10

    pw.main()

    # Restaura stdin
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
