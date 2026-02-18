import subprocess

print("🤖 IA Pessoal Local (Grátis)")
print("Digite 'sair' para encerrar\n")

while True:
    user = input("Você: ")

    if user.lower() == "sair":
        break

    prompt = f"Responda como assistente pessoal, simples e direto: {user}"

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )

    print("IA:", result.stdout)
