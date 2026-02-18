print("🤖 IA Pessoal Iniciada")
print("Digite 'sair' para encerrar\n")

while True:
    user = input("Você: ")

    if user.lower() == "sair":
        print("IA: Até mais 👋")
        break

    resposta = f"IA: Você disse '{user}'. Em breve vou pensar melhor 🙂"
    print(resposta)
