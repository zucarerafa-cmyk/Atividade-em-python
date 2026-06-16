saboresDePizza = ["Calabresa", "Brócolis", "Frango com catupiry", "Mussarela"]
votos = [0, 0, 0, 0]
votosValidos = 0
votosInvalidos = 0
numero = -1 
escolha = input("Menu de Opções: \n 0: Sair \n 1: Calabresa \n 2: Mussarela \n 3: Frango \n 4: Marguerita \n Escolha uma opção :")

while True:
    print("Vote no seu sabor favorito")

    for i in range(len(saboresDePizza)):
        print(f"{i + 1} - {saboresDePizza[i]}")

    print("0 - Encerrar votação")

    numero = int(input("Digite o número do seu voto: "))

    if numero == 0:
        print("Encerrando sua votação")
        break

    elif 1 <= numero <= len(saboresDePizza):
        posicao = numero - 1
        votos[posicao] += 1
        votosValidos += 1
        print("Voto registrado em", saboresDePizza[posicao])

    else:
        print("Voto inválido, opção não é aceita")
        votosInvalidos += 1
print("\nAPURAÇÃO DOS VOTOS")

for i in range(len(saboresDePizza)):
    print(f"{saboresDePizza[i]}: {votos[i]} voto(s)")

print(f"\nTotal de votos válidos: {votosValidos}")
print(f"Total de votos inválidos: {votosInvalidos}")

maiorVoto = votos[0]
vencedor = saboresDePizza[0]

for i in range(1, len(votos)):
    if votos[i] > maiorVoto:
        maiorVoto = votos[i]
        vencedor = saboresDePizza[i]

print(f"\nOpção vencedora: {vencedor}")
print(f"Quantidade de votos: {maiorVoto}")        