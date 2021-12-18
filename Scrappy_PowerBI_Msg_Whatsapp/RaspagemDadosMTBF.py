import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class RaspagemDadosMTBF:

    def __init__(self):
        print("Iniciando o programa para raspagem de dados no site do PowerBI ;)")
        dir_path = os.getcwd()  ##pega local de onde esta executando o script
        #print(dir_path)
        profile = os.path.join(dir_path, "profile", "wpp")  ##cria as pastas para armazenar os cookies
        #print(profile)
        options = Options()
        #print(options)
        options.add_argument(r"user-data-dir={}".format(profile))
        self.driver = webdriver.Chrome(options=options)
        self.site_powerbi_principal = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection7257dff8a8fca8c3da58?language=en-US"
        self.site_powerbi_atualizacao = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/list?language=en-US"

        self.site_powerbi_MTBF_alternativo = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection974209e42a256ee1c120?language=en-US"
        self.site_powerbi_falha_alternativo = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection12baad1a75257afa2189?language=en-US"

        self.driver.get(self.site_powerbi_principal)

        print("Carregando a página Principal do PowerBI.")
        print("Loading...")
        time.sleep(25)


    def raspagem_dados_MTBF(self):
        print("Colhendo dados de MTBF...")

        try:
            self.driver.find_element(By.XPATH, '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[3]').click()
            time.sleep(7)

        except:
            self.driver.get(self.site_powerbi_MTBF_alternativo)
            time.sleep(20)

        try:
            self.MTBF_PT = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[2]').text
        except:
            self.MTBF_PT = 0.00
        try:
            self.MTBF_RTG = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[5]').text
        except:
            self.MTBF_RTG = 0.00
        try:
            self.MTBF_CT = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[7]').text
        except:
            self.MTBF_CT = 0.00
        try:
            self.MTBF_RS = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[9]').text
        except:
            self.MTBF_RS = 0.00
        try:
            self.MTBF_EV = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[10]').text
        except:
            self.MTBF_EV = 0.00
        print("Raspagem de dados MTBF concluído!!.")

    def raspagem_dados_qtdade_falhas(self):

        print("Colhendo dados quantidades de falhas...")

        try:
            self.driver.find_element(By.XPATH,'//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[7]').click()

            time.sleep(7)
        except:
            self.driver.get(self.site_powerbi_falha_alternativo)
            time.sleep(20)

        try:
            self.Qtde_Falhas_STS = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[12]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[2]').text
        except:
            self.Qtde_Falhas_STS = 0.00
        try:
            self.Qtde_Falhas_RTG = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[12]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[5]').text
        except:
            self.Qtde_Falhas_RTG = 0.00
        try:
            self.Qtde_Falhas_CT = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[12]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[7]').text
        except:
            self.Qtde_Falhas_CT = 0.00
        try:
            self.Qtde_Falhas_RS = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[12]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[9]').text
        except:
            self.Qtde_Falhas_RS = 0.00
        try:
            self.Qtde_Falhas_EV = self.driver.find_element(By.XPATH,
            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[12]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[10]').text
        except:
            self.Qtde_Falhas_EV = 0.00
        print("Raspagem de dados quantidade de falhas concluído!!.")

    def raspagem_dados_atualizacao(self):
        self.driver.get(self.site_powerbi_atualizacao)
        print("Colhendo dados da atualização.")
        time.sleep(10)
        self.Ultima_Atualizacao = self.driver.find_element(By.XPATH,
                                                           '//*[@id="artifactContentList"]/div[1]/div[3]/div[5]').text

    def fechar_browser(self):
        print("Fechando navegador. Bye!!")
        time.sleep(5)
        self.driver.close()



