from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Abra o Chrome controlado pelo Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Vá para o WhatsApp Web
driver.get("https://web.whatsapp.com/")

print("Escaneie o QR code no WhatsApp Web e depois pressione Enter")
input()

# Nome do contato ou grupo
contato = "Eduardo"  # coloque o nome exato do contato
mensagem = "Olá! Teste da minha IA."

# Procura o chat pelo nome
chat = driver.find_element(By.XPATH, f'//span[@title="{contato}"]')
chat.click()

# Envia a mensagem
caixa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
caixa.send_keys(mensagem + Keys.ENTER)

print("Mensagem enviada com sucesso!")
