import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ==========================
# Memória da IA
# ==========================
PASTA_MEMORIA = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "MinhaIA")
os.makedirs(PASTA_MEMORIA, exist_ok=True)
ARQUIVO_MEMORIA = os.path.join(PASTA_MEMORIA, "memoria.txt")

def ler_memoria():
    if not os.path.exists(ARQUIVO_MEMORIA):
        return ""
    with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
        return f.read()

def salvar_memoria(texto):
    with open(ARQUIVO_MEMORIA, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def gerar_resposta(usuario):
    memoria = ler_memoria()
    usuario_lower = usuario.lower()
    
    if "meu nome é" in usuario_lower:
        nome = usuario.split("é")[-1].strip()
        salvar_memoria(f"Nome do usuário: {nome}")
        return f"Prazer, {nome}! Vou lembrar do seu nome 🙂"
    elif "qual é meu nome" in usuario_lower:
        return "Isso é o que lembro de você:\n" + memoria
    else:
        return "Entendi. Pode continuar."

# ==========================
# WhatsApp Web
# ==========================
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")
print("📱 Escaneie o QR code do WhatsApp Web e depois pressione Enter no PowerShell...")
input()

# Nome do contato ou grupo (igual aparece no WhatsApp)
contato = input("Digite o nome do contato ou grupo do WhatsApp: ")

# Abre o chat do contato
chat = driver.find_element(By.XPATH, f'//span[@title="{contato}"]')
chat.click()
time.sleep(1)

print("🤖 IA conectada ao WhatsApp! Digite suas mensagens no PowerShell.")

while True:
    usuario = input("Você (PowerShell): ")
    if usuario.lower() == "sair":
        print("IA: Até mais 👋")
        break

    resposta_da_ia = gerar_resposta(usuario)

    # Envia a resposta para o WhatsApp
    caixa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    caixa.send_keys(resposta_da_ia + Keys.ENTER)

    print("IA enviada para WhatsApp:", resposta_da_ia)
    salvar_memoria(f"Usuário: {usuario}")
    salvar_memoria(f"IA: {resposta_da_ia}")
