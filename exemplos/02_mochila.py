"""
Esqueleto da Semana 3: mochila 0-1.

Voce tem uma mochila que aguenta ate CAPACIDADE quilos e uma lista de itens,
cada um com um peso e um valor. Escolha quais itens levar para maximizar o
valor total sem estourar a capacidade.

A decisao de cada item e do tipo sim ou nao, entao a variavel e BINARIA.

O que voce precisa completar esta marcado com TODO.
Comece com 3 itens se 5 parecer demais.
"""

from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value, lpSum

# ---------------------------------------------------------------- os dados
ITENS = ["barraca", "agua", "comida", "livro", "lanterna"]
PESO = {"barraca": 6, "agua": 4, "comida": 3, "livro": 2, "lanterna": 1}
VALOR = {"barraca": 9, "agua": 8, "comida": 7, "livro": 3, "lanterna": 4}
CAPACIDADE = 10

# ------------------------------------------------------------- o modelo
m = LpProblem("mochila", LpMaximize)

# TODO 1: crie uma variavel binaria para cada item.
#         Dica: LpVariable(f"leva_{i}", cat="Binary")
x = {}
# for i in ITENS:
#     x[i] = ...

# TODO 2: escreva a funcao objetivo (maximizar o valor total levado).
#         Dica: lpSum(VALOR[i] * x[i] for i in ITENS)
# m += ...

# TODO 3: escreva a restricao de capacidade (o peso levado nao passa da mochila).
# m += ..., "capacidade"

# ------------------------------------------------------------- resolver
if not x:
    print("O modelo ainda esta vazio. Complete os TODO acima e rode de novo.")
    raise SystemExit

m.solve()

print("status:", LpStatus[m.status])
print("valor total:", value(m.objective))
levados = [i for i in ITENS if x[i].varValue and x[i].varValue > 0.5]
print("itens levados:", ", ".join(levados))
print("peso usado:", sum(PESO[i] for i in levados), "de", CAPACIDADE)

# TODO 4 (a comparacao que fecha a entrega da semana):
#   Rode o mesmo modelo trocando cat="Binary" por variaveis continuas entre 0 e 1
#   (LpVariable(..., lowBound=0, upBound=1)), arredonde o resultado a mao e
#   anote o que aconteceu: a solucao arredondada ainda cabe na mochila?
#   Ela da o mesmo valor da solucao inteira?
