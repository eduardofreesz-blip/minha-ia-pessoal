import subprocess

print("🤖 IA Pessoal Iniciada")
print("Digite 'sair' para encerrar\n")

while True:
    usuario = input("Você: ")

    if usuario.lower() == "sair":
        print("IA: Até mais 👋")
        break

    prompt = f"""
Você é um assistente pessoal.
Responda sempre em português do Brasil.
Seja claro, educado e direto.
Use linguagem simples, como WhatsApp.

Pergunta do usuário:
{usuario}
"""

    resposta = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    print("IA:", resposta.stdout)
