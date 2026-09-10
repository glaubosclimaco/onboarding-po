"""
Esqueleto da Semana 3: problema de designacao.

Tres pessoas, tres tarefas, e um custo (em horas) para cada par pessoa-tarefa.
Cada pessoa recebe exatamente uma tarefa, e cada tarefa vai para exatamente
uma pessoa. Minimize o total de horas.

Tamanho de proposito pequeno: voce consegue conferir a resposta de cabeca.

O que voce precisa completar esta marcado com TODO.
"""

from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, value, lpSum

# ---------------------------------------------------------------- os dados
PESSOAS = ["Ana", "Bruno", "Carla"]
TAREFAS = ["relatorio", "coleta", "codigo"]
CUSTO = {
    ("Ana",   "relatorio"): 4, ("Ana",   "coleta"): 6, ("Ana",   "codigo"): 9,
    ("Bruno", "relatorio"): 7, ("Bruno", "coleta"): 3, ("Bruno", "codigo"): 8,
    ("Carla", "relatorio"): 5, ("Carla", "coleta"): 8, ("Carla", "codigo"): 2,
}

# ------------------------------------------------------------- o modelo
m = LpProblem("designacao", LpMinimize)

# TODO 1: uma variavel binaria para cada par (pessoa, tarefa).
#         x[p, t] = 1 significa "a pessoa p fica com a tarefa t".
x = {}
# for p in PESSOAS:
#     for t in TAREFAS:
#         x[p, t] = LpVariable(f"x_{p}_{t}", cat="Binary")

# TODO 2: minimizar o total de horas.
# m += lpSum(...)

# TODO 3: cada pessoa recebe exatamente uma tarefa (uma restricao por pessoa).
# for p in PESSOAS:
#     m += lpSum(...) == 1, f"pessoa_{p}"

# TODO 4: cada tarefa vai para exatamente uma pessoa (uma restricao por tarefa).
# for t in TAREFAS:
#     m += lpSum(...) == 1, f"tarefa_{t}"

# TODO 5: a restricao logica da semana.
#         Se a Ana ficar com o relatorio, entao a Carla nao pode ficar com o codigo.
#         Dica: x["Ana", "relatorio"] + x["Carla", "codigo"] <= 1

# ------------------------------------------------------------- resolver
if not x:
    print("O modelo ainda esta vazio. Complete os TODO acima e rode de novo.")
    raise SystemExit

m.solve()

print("status:", LpStatus[m.status])
print("total de horas:", value(m.objective))
for p in PESSOAS:
    for t in TAREFAS:
        if x[p, t].varValue and x[p, t].varValue > 0.5:
            print(f"  {p} -> {t} ({CUSTO[p, t]} h)")
