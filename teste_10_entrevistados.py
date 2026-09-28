# Script de demonstracao - 50 entrevistados preenchidos automaticamente

import sys
import io

# 50 entrevistados: Nome, Idade, Opiniao (1=EXCELENTE, 2=BOM, 3=RUIM)
entradas = """Ana Lima
28
1
Carlos Souza
35
2
Maria Oliveira
22
1
Joao Silva
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
Patricia Rocha
25
2
Eduardo Alves
38
1
Amanda Ferreira
29
2
Ricardo Lima
52
1
Juliana Martins
24
3
Marcos Pereira
47
1
Camila Rodrigues
31
2
Thiago Nascimento
26
1
Beatriz Carvalho
39
3
Leonardo Araujo
44
1
Natalia Gomes
23
2
Felipe Barros
36
1
Gabriela Moreira
28
1
Vinicius Costa
42
3
Isabela Dias
27
2
Rodrigo Melo
55
1
Larissa Sousa
32
1
Daniel Oliveira
48
2
Priscila Lima
25
3
Gustavo Ferreira
37
1
Renata Santos
29
2
Anderson Silva
43
1
Mariana Costa
26
1
Paulo Rocha
50
2
Carla Mendes
34
3
Sergio Alves
46
1
Tatiana Pereira
28
2
Leandro Gomes
39
1
Vanessa Martins
24
1
Roberto Nascimento
53
3
Aline Carvalho
31
2
Julio Araujo
27
1
Samara Barros
36
1
Diego Moreira
41
2
Bianca Dias
23
1
Alexandre Melo
49
3
Raquel Sousa
30
1
Andre Oliveira
38
2
Flavia Lima
26
1
Marcelo Santos
44
1
Debora Ferreira
33
2
Henrique Costa
40
1
"""

sys.stdin = io.StringIO(entradas)
exec(open("pesquisa_tudoweb.py").read())
sys.stdin = sys.__stdin__
