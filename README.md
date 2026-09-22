# 📋 Pesquisa de Opinião - TudoWeb

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Tema](https://img.shields.io/badge/tema-estrutura%20de%20repeti%C3%A7%C3%A3o-FFB703?style=for-the-badge&logo=repeat&logoColor=white)

## 🎯 Objetivo

Programa em Python desenvolvido por Carolina Barbosa para a **Agenda 08** do curso Técnico em
Desenvolvimento de Sistemas.

A empresa de marketing TudoWeb precisa realizar uma pesquisa de opinião com seus clientes para
saber o grau de satisfação no atendimento. O programa coleta o nome, a idade e a opinião de cada
entrevistado e, ao final, exibe quantas respostas foram EXCELENTE e quantas foram RUIM.

## 🐍 Linguagem

Python 3.10 ou superior.

## ▶️ Como executar

```bash
python3 pesquisa_opiniao.py
```

O programa vai pedir, para cada entrevistado:
1. Nome
2. Idade
3. Opinião sobre o atendimento (`1` Excelente, `2` Bom ou `3` Ruim)

E ao final exibe o total de respostas EXCELENTE, BOM e RUIM.

## 📐 Regras de negócio

| Opção digitada | Classificação |
|---|---|
| 1 | EXCELENTE |
| 2 | BOM |
| 3 | RUIM |
| Qualquer outro valor | Pergunta é repetida até digitar uma opção válida |

## 🛠️ Tecnologias

- Python (estrutura de repetição `for`, para controlar o número de entrevistados)
- Python (estrutura de repetição `while`, para validar a opinião digitada)
- Python (estrutura de decisão `match/case`)

## 🧪 Testes

O programa foi testado com **10 entrevistados** antes da execução final com os **50 entrevistados** exigidos pela atividade, alterando apenas a variável `NUMERO_DE_ENTREVISTADOS` no início do código.
