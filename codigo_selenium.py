from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

# abrir navegador
navegador = webdriver.Chrome()

# acesssar um site
navegador.get("https://www.hashtagtreinamentos.com/")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar o elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde")


# clicar em um elemento
botao_verde.click()

lista_botoes = navegador.find_elements("class name", "header_titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

# selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# navegar para outra página
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# escrever em um campo formulario

navegador.find_element("id", "firstname").send_keys("Deywid")
navegador.find_element("id", "email").send_keys("deywid2005@gmail.com")
navegador.find_element("id", "phone").send_keys("31998984437")


botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

# dar scroll ( centralizar um elemento na tel
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         botao_quero_clicar)
# opcao 1 - espera manual
time.sleep(3)

# opção 2 - espera dninamica

espera = WebDriverWait(navegador, 10)
# espera até que o elemento esteja clicável
espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()

# tempo de tela aberta
time.sleep(10)
