''''
Exemplo de como enviar uma msg no whatsapp
 Msg = EnviarMsgWhatsapp.EnviarMsg()
 Msg.encontar_contato("Nome contato")
 Msg.escrever_msg("escrever msg ")
 Msg.escrever_msg("escrever msg  ")
 Msg.escrever_msg("escrever msg ")
 Msg.enviar_msg() ## Enviar a msg


'''


import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EnviarMsg:


    def __init__(self):
        print("Carregando o site do whatsappWeb...")
        dir_path = os.getcwd()  ##pega local de onde esta executando o script
        #print(dir_path)
        profile = os.path.join(dir_path, "profile", "wpp")  ##cria as pastas para armazenar os cookies
        #print(profile)
        options = Options()
        #print(options)
        options.add_argument(r"user-data-dir={}".format(profile))

        self.driver = webdriver.Chrome(options=options)
        self.url_whatsapp_web = "https://web.whatsapp.com/"
        self.driver.get(self.url_whatsapp_web)

        self.botao_buscar_contato_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        self.local_onde_escreve_msg_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
        self.botao_enviar_msg_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'


        while len(self.driver.find_elements(By.ID, 'side' )) < 1:## ESPERAR O WHATSSAP CARREGAR.
            time.sleep(1)

    def encontar_contato(self, nome_do_contato = "teste" ):
        self.primeiro_num = nome_do_contato
        time.sleep(2)


        ### Encontre o elemento de pesquisa do whatsapp
        element = self.driver.find_element(By.XPATH, self.botao_buscar_contato_xpath)
        ### Digita o contato na pesquisa do whatsapp
        element.send_keys(self.primeiro_num)
        ### aperta o ENTER
        element.send_keys(Keys.ENTER)
        ### Aguarde 1segundo.
        time.sleep(1)
        print("Enviando a msg solicitada!!")
        print("Loading...")

    def escrever_msg(self, texto_1 = "msg testando"):
        print("Escrevendo msg...")
        self.texto_1 = texto_1
        element = self.driver.find_element(By.XPATH, self.local_onde_escreve_msg_xpath)
        element.send_keys(self.texto_1)
        webdriver.ActionChains(self.driver).key_down(Keys.ALT).send_keys(Keys.ENTER).perform()

    def pular_linha_msg(self):
        print("pulando uma linha...")
        webdriver.ActionChains(self.driver).key_down(Keys.ALT).send_keys(Keys.ENTER).perform()
        
    def enviar_msg(self):

        #element.send_keys(Keys.ENTER)  ## Apertar ENTER
        self.driver.find_element(By.XPATH, self.botao_enviar_msg_xpath).click()
        print("Msg enviada com sucesso!!")
       
    def fechar_msg(self):
        time.sleep(5)
        self.driver.close()