# Pesquisa de Opinião – TudoWeb Marketing

## Descrição
Programa em Python desenvolvido para coletar o grau de satisfação de clientes da empresa TudoWeb Marketing, utilizando estruturas de repetição e decisão.

## Funcionalidades
- Coleta **nome**, **idade** e **opinião** de cada entrevistado
- Classificação da opinião em: **EXCELENTE** (1), **BOM** (2) ou **RUIM** (3)
- Pesquisa configurada para **50 entrevistados**
- Exibe ao final:
  - Quantidade de respostas **EXCELENTE**
  - Quantidade de respostas **BOM**
  - Quantidade de respostas **RUIM**
  - Percentual de cada categoria
- Validação de entradas (nome vazio, idade inválida, opção fora do intervalo)

## Estruturas Utilizadas
| Recurso               | Onde é usado                                        |
|-----------------------|-----------------------------------------------------|
| `for`                 | Loop principal – percorre os 50 entrevistados       |
| `while True`          | Loops de validação de cada campo                    |
| `if / elif / else`    | Classifica a opinião e incrementa contadores        |
| `try / except`        | Trata erros de conversão de tipo (idade/opção)      |
| Funções               | Código modularizado em funções bem definidas        |

## Como Executar

### Programa principal (50 entrevistados)
```bash
python pesquisa_tudoweb.py
```

### Teste automático (10 entrevistados simulados)
```bash
python teste_10_entrevistados.py
```

## Estrutura do Projeto
```
pesquisa_tudoweb/
├── pesquisa_tudoweb.py        # Programa principal
├── teste_10_entrevistados.py  # Script de teste automatizado
└── README.md                  # Documentação
```

## Exemplo de Saída
```
=======================================================
   PESQUISA DE SATISFAÇÃO – TudoWeb Marketing
=======================================================

───────────────────────────────────────────────────────
  Entrevistado 1 de 10
───────────────────────────────────────────────────────
  Nome do entrevistado 1: Ana Lima
  Idade: 28
  Avaliação do atendimento:
    1 – EXCELENTE
    2 – BOM
    3 – RUIM
  Sua escolha: 1

  OK: Ana Lima (28 anos) avaliou como: EXCELENTE

...

=======================================================
           RESULTADO FINAL DA PESQUISA
=======================================================
  Total de entrevistados : 10
  Respostas EXCELENTE    : 5
  Respostas BOM          : 3
  Respostas RUIM         : 2
=======================================================
  EXCELENTE :  50.0%
  BOM       :  30.0%
  RUIM      :  20.0%
=======================================================
```

## Competências Desenvolvidas
- **Implementar algoritmos de programação** – programa estruturado com funções e fluxo claro
- **Utilizar linguagem de programação** – Python com boas práticas
- **Elaborar algoritmos** – lógica de coleta, validação e contagem
- **Codificar com programação estruturada** – uso de `for`, `while`, `if/elif/else`
- **Raciocínio lógico com estrutura de repetição** – loop principal e loops de validação
