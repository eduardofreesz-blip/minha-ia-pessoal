import subprocess
from datetime import datetime

ARQUIVO_MEMORIA = "memoria.txt"

def ler_memoria():
    try:
        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def salvar_memoria(texto):
    with open(ARQUIVO_MEMORIA, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

print("🤖 IA Pessoal com Memória")
print("Digite 'sair' para encerrar\n")

while True:
    usuario = input("Você: ")

    if usuario.lower() == "sair":
        print("IA: Até mais 👋")
        break

    memoria = ler_memoria()

    prompt = f"""
Você é um assistente pessoal.
Responda em português do Brasil.
Seja simples, direto e educado.

MEMÓRIA ANTERIOR:
{memoria}

MENSAGEM ATUAL DO USUÁRIO:
{usuario}
"""

    resposta = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    resposta_texto = resposta.stdout.strip()

    print("IA:", resposta_texto)

    # salva conversa na memória
    salvar_memoria(f"[{datetime.now()}] Usuário: {usuario}")
    salvar_memoria(f"[{datetime.now()}] IA: {resposta_texto}")
