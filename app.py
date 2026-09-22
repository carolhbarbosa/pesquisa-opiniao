# Pesquisa de opinião - Empresa TudoWEeb
# Autor: Carolina Barbosa

# ---------------------------------------------------------
# Altere este valor para testar o programa:
# ---------------------------------------------------------
NUMERO_DE_ENTREVISTADOS = 50

# Contadores que vão acumular o resultado da pesquisa
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Estrutura de repetição (FOR):
for entrevistado in range(1, NUMERO_DE_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {entrevistado} de {NUMERO_DE_ENTREVISTADOS} ---")

    nome = input("Nome do entrevistado: ")
    idade = int(input("Idade do entrevistado: "))

    opiniao = int(input("Opinião sobre o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    # Estrutura de repetição (WHILE): repete a pergunta enquanto o valor
    # digitado não for 1, 2 ou 3
    while opiniao != 1 and opiniao != 2 and opiniao != 3:
        print("Opção inválida! Digite apenas 1, 2 ou 3.")
        opiniao = int(input("Opinião sobre o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    # Estrutura de decisão: verifica a opinião informada e atualiza o contador correspondente

    match opiniao:
        case 1:
            qtd_excelente += 1
            print(f"Obrigado, {nome}! Resposta registrada como EXCELENTE.")
        case 2:
            qtd_bom += 1
            print(f"Obrigado, {nome}! Resposta registrada como BOM.")
        case 3:
            qtd_ruim += 1
            print(f"Obrigado, {nome}! Resposta registrada como RUIM.")

# Exibição do resultado final da pesquisa
print("\n===== RESULTADO DA PESQUISA DE OPINIÃO =====")
print(f"Total de entrevistados: {NUMERO_DE_ENTREVISTADOS}")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")