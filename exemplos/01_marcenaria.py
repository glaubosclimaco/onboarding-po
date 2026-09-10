"""
Exemplo completo da Semana 2: a marcenaria.

Maximizar o lucro de uma marcenaria que produz mesas (x1) e armarios (x2),
respeitando a capacidade de tres recursos.

    max  z = 3*x1 + 5*x2
    s.a.      x1          <=  4      (serra)
                    2*x2  <= 12      (lixadeira)
         3*x1 + 2*x2      <= 18      (montagem)
              x1, x2      >=  0

Resposta esperada: x1 = 2, x2 = 6, z = 36.

Como rodar:  pip install pulp   e depois   python 01_marcenaria.py
"""

from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

# 1. O problema e o sentido da otimizacao
m = LpProblem("marcenaria", LpMaximize)

# 2. As variaveis de decisao: o que a marcenaria escolhe produzir
x1 = LpVariable("mesas", lowBound=0)
x2 = LpVariable("armarios", lowBound=0)

# 3. A funcao objetivo
m += 3 * x1 + 5 * x2

# 4. As restricoes, uma por linha, cada uma com nome
m += x1 <= 4, "serra"
m += 2 * x2 <= 12, "lixadeira"
m += 3 * x1 + 2 * x2 <= 18, "montagem"

# 5. Resolver
m.solve()

# 6. Ler a resposta. Sempre confira o status antes de acreditar nos numeros.
print("status:", LpStatus[m.status])
print("lucro otimo:", value(m.objective))
for v in m.variables():
    print(f"  {v.name} = {v.varValue}")

# 7. Tarefa da Semana 2: quanto de cada recurso foi usado, e quanto havia.
#    As restricoes que ficaram no limite sao os gargalos.
mesas, armarios = x1.varValue, x2.varValue
uso = {
    "serra":     (mesas,                    4),
    "lixadeira": (2 * armarios,            12),
    "montagem":  (3 * mesas + 2 * armarios, 18),
}

print("\nrecurso        usado  disponivel  situacao")
for nome, (usado, capacidade) in uso.items():
    situacao = "NO LIMITE (gargalo)" if abs(usado - capacidade) < 1e-6 else "sobrou"
    print(f"{nome:<13} {usado:>6.1f} {capacidade:>11.1f}  {situacao}")
