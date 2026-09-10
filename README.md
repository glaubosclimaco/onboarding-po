# Trilha de entrada em Pesquisa Operacional

Material de onboarding para alunos de **iniciação científica** que vão começar a
pesquisar otimização e nunca viram programação linear.

Quatro semanas, cerca de 8 horas por semana, tudo em português, com Python e PuLP.

**Site da trilha:** https://glaubosclimaco.github.io/onboarding-po/

Laboratório MODAL, Departamento de Computação, UFMA (São Luís).

## O que tem aqui

| Arquivo | O que é |
| --- | --- |
| `index.html` | A trilha completa, uma página só. É o que o GitHub Pages publica. |
| `exemplos/01_marcenaria.py` | Exemplo resolvido da Semana 2, pronto para rodar. |
| `exemplos/02_mochila.py` | Esqueleto da mochila 0-1 da Semana 3, com TODO para o aluno completar. |
| `exemplos/03_designacao.py` | Esqueleto da designação da Semana 3, com a restrição lógica. |

## Como o aluno usa

1. Abre o site e segue semana a semana. As tarefas têm caixas de marcar, e o
   navegador guarda o progresso no próprio dispositivo.
2. Instala o necessário: `pip install pulp pandas matplotlib`.
3. Roda o exemplo para conferir que o ambiente está de pé:

```bash
python exemplos/01_marcenaria.py
# status: Optimal
# lucro otimo: 36.0
```

4. Completa os esqueletos da Semana 3 nos arquivos `02_` e `03_`.

## Estrutura da trilha

- **Semana 1**: do problema em português ao modelo matemático.
- **Semana 2**: do papel para o computador, resolver e interpretar com PuLP.
- **Semana 3**: decisões do tipo sim ou não, variáveis binárias.
- **Semana 4**: problemas clássicos e o limite do computador.
- **Depois**: escolher um artigo com o orientador e estudá-lo a fundo.

Em cada semana, os vídeos são para assistir e os textos são material de apoio,
de leitura opcional. As tarefas são pequenas e a última de cada lista fecha a
entrega da semana.

## Como atualizar

O site é um único arquivo HTML, sem dependências nem build. Edite `index.html`,
faça commit na branch `main` e o GitHub Pages republica sozinho em cerca de um
minuto.

## Licença

Material sob [CC BY 4.0](LICENSE): pode copiar, adaptar e usar em outras
disciplinas, desde que cite a autoria.
