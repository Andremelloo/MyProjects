import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
#class RaspagemDadosPowerBi:
#def raspagem_dados_disponibilidade(self):
#def raspagem_dados_confibilidade(self):
#def raspagem_dados_mttr(self):
#def raspagem_dados_atualizacao(self):
#def site_custo(self):
#def raspagem_dados_custos_fixos(self):
#def fechar_browser(self)



"""


class RaspagemDadosPowerBi:

    def __init__(self):
        print("Iniciando o programa para raspagem de dados no site do PowerBI ;)")
        dir_path = os.getcwd()  ##pega local de onde esta executando o script
        # print(dir_path)
        profile = os.path.join(dir_path, "profile", "wpp")  ##cria as pastas para armazenar os cookies
        # print(profile)
        options = Options()
        # print(options)
        options.add_argument(r"user-data-dir={}".format(profile))
        self.driver = webdriver.Chrome(options=options)

        self.site_powerbi_principal = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection7257dff8a8fca8c3da58?language=en-US"
        self.site_powerbi_custo = "https://app.powerbi.com/groups/afa1f3a4-6aea-429e-8d73-75ca1177185e/reports/9b3a79f0-e3e4-45b2-ba18-09062b92c335/ReportSectionb20670f43de411d1128b?language=en-US"
        self.site_powerbi_atualizacao_principal = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/list?language=en-US"
        self.site_powerbi_atualizacao_custo = "https://app.powerbi.com/groups/afa1f3a4-6aea-429e-8d73-75ca1177185e/list?language=en-US"

        self.site_powerbi_disponibilidade_alternativo = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection7257dff8a8fca8c3da58?language=en-US"
        self.site_powerbi_confiabiliade_alternativo = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSection10fa909f4edeb0cd4eb8?language=en-US"
        self.site_powerbi_MTTR_alternativo = "https://app.powerbi.com/groups/5131fe96-a1b6-4a68-856c-e1899835f992/reports/6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8/ReportSectionffbe9908e270b4376b64?language=en-US"
        self.site_powerbi_custo_alternativo = "https://app.powerbi.com/groups/afa1f3a4-6aea-429e-8d73-75ca1177185e/reports/9b3a79f0-e3e4-45b2-ba18-09062b92c335/ReportSection883bd1e3a81db5aeae6c?language=en-US"

        self.botao_disponibilidade_xpath = '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[1]'
        self.botao_confiabilidade_xpath = '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[2]'
        self.botao_mttr_xpath = '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[4]'
        self.dados_dis_conf_mttr_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[14]/transform/div/div[3]/div/visual-modern/div'

        self.driver.get(self.site_powerbi_principal)

        print("Carregando a página Principal do PowerBI.")
        print("Loading...")
        time.sleep(15)

    def raspagem_dados_disponibilidade(self):

        print("Colhendo dados de Disponibilidade...")
        try:
            self.driver.find_element(By.XPATH,
                                     self.botao_disponibilidade_xpath).click()
            time.sleep(3)
        except:
            self.driver.get(self.site_powerbi_disponibilidade_alternativo)
            time.sleep(20)

        time.sleep(2)
        self.valores_disp = self.driver.find_element(By.XPATH,
                                                     self.dados_dis_conf_mttr_xpath).text

        self.dados_valores_disp = self.valores_disp.split("\n")

        while len(self.dados_valores_disp) < 33:
            time.sleep(1)
            # if len(self.dados_valores) == 34:

        self.Disp_PT = self.dados_valores_disp[22].strip()
        self.Disp_RTG = self.dados_valores_disp[24].strip()
        self.Disp_RS = self.dados_valores_disp[26].strip()
        self.Disp_EV = self.dados_valores_disp[27].strip()
        self.Disp_CT = self.dados_valores_disp[25].strip()
        self.Disp_EPP = self.dados_valores_disp[28].strip()
        self.Disp_CF = self.dados_valores_disp[33].strip()

        print("Raspagem de dados Disponibilidade concluído!!.")

    def raspagem_dados_confibilidade(self):

        print("Colhendo dados de Confiabilidade...")
        try:
            self.driver.find_element(By.XPATH,
                                     self.botao_confiabilidade_xpath).click()
            time.sleep(3)

        except:
            self.driver.get(self.site_powerbi_confiabiliade_alternativo)
            time.sleep(20)

        time.sleep(2)
        self.valores_conf = self.driver.find_element(By.XPATH,
                                                     self.dados_dis_conf_mttr_xpath).text

        self.dados_valores_conf = self.valores_conf.split("\n")

        while len(self.dados_valores_conf) < 33:
            print(len(self.dados_valores_conf))
            time.sleep(1)

        self.Conf_STS = self.dados_valores_conf[22].strip()
        self.Conf_RTG = self.dados_valores_conf[24].strip()
        self.Conf_RS = self.dados_valores_conf[26].strip()
        self.Conf_EV = self.dados_valores_conf[27].strip()
        self.Conf_CT = self.dados_valores_conf[25].strip()
        self.Conf_EPP = self.dados_valores_conf[28].strip()
        self.Conf_FC = self.dados_valores_conf[33].strip()

        print("Raspagem de dados Confiabilidade concluído!!!.")

    def raspagem_dados_mttr(self):

        print("Colhendo dados de MTTR...")

        try:
            self.driver.find_element(By.XPATH,
                                     self.botao_mttr_xpath).click()
            time.sleep(3)
        except:
            self.driver.get(self.site_powerbi_MTTR_alternativo)
            time.sleep(15)

        time.sleep(2)
        self.valores_mttr = self.driver.find_element(By.XPATH,
                                                     self.dados_dis_conf_mttr_xpath).text

        self.dados_valores_mttr = self.valores_mttr.split("\n")

        while len(self.dados_valores_mttr) < 26:
            time.sleep(1)

        self.MTTR_STS = self.driver.find_element(By.XPATH,
                                                 '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[14]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[2]').text
        self.MTTR_RTG = self.driver.find_element(By.XPATH,
                                                 '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[14]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div/div/div[6]').text

        print("Raspagem de dados MTTR concluído!!!.")

    def raspagem_dados_atualizacao(self):
        print("Colhendo dados da atualização.")
        self.driver.get(self.site_powerbi_atualizacao_principal)

        time.sleep(6)

        self.Ultima_Atualizacao_Principal = self.driver.find_element(By.XPATH,
                                                                     '//*[@id="artifactContentList"]/div[1]/div[3]/div[5]').text

        self.driver.get(self.site_powerbi_atualizacao_custo)
        time.sleep(6)
        self.Ultima_Atualizacao_Custo = self.driver.find_element(By.XPATH,
                                                                 '//*[@id="artifactContentList"]/div[1]/div[3]/div[5]').text

    def site_custo(self):
        print("Carregando a página de custos do PowerBi.")
        print("Loading...")
        self.driver.get(self.site_powerbi_custo)
        time.sleep(15)

    def raspagem_dados_custos_fixos(self):

        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="content"]/report/exploration-container/div/exploration-fluent-navigation/section/mat-list/ul/li[2]').click()

            time.sleep(5)
        except:
            self.driver.get(self.site_powerbi_custo_alternativo)
            time.sleep(20)

        try:
            self.Custo_RTG_Atual = self.driver.find_element(By.XPATH,
                                                            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[13]').text
        except:
            self.Custo_RTG_Atual = 0.00
        try:
            self.Custo_RTG_Serv_Atua = self.driver.find_element(By.XPATH,
                                                                '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[12]').text
        except:
            self.Custo_RTG_Serv_Atua = 0.00
        try:
            self.Custo_STS_Atual = self.driver.find_element(By.XPATH,
                                                            '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[15]').text
        except:
            self.Custo_STS_Atual = 0.00
        try:
            self.Custo_STS_Serv_Atua = self.driver.find_element(By.XPATH,
                                                                '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[14]').text
        except:
            self.Custo_STS_Serv_Atua = 0.00
        try:
            self.Custo_RS_Atual = self.driver.find_element(By.XPATH,
                                                           '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[11]').text
        except:
            self.Custo_RS_Atual = 0.00
        try:
            self.Custo_RS_Serv_Atua = self.driver.find_element(By.XPATH,
                                                               '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[10]').text
        except:
            self.Custo_RS_Serv_Atua = 0.00
        try:
            self.Custo_EV_Atual = self.driver.find_element(By.XPATH,
                                                           '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[5]').text
        except:
            self.Custo_EV_Atual = 0.00
        try:
            self.Custo_EV_Serv_Atua = self.driver.find_element(By.XPATH,
                                                               '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[4]').text
        except:
            self.Custo_EV_Serv_Atua = 0.00
        try:
            self.Custo_TT_Atual = self.driver.find_element(By.XPATH,
                                                           '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[17]').text
        except:
            self.Custo_TT_Atual = 0.00
        try:
            self.Custo_TT_Serv_Atua = self.driver.find_element(By.XPATH,
                                                               '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[16]').text
        except:
            self.Custo_TT_Serv_Atua = 0.00
        try:
            self.Custo_Gasto_Total_mes = self.driver.find_element(By.XPATH,
                                                                  '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[5]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[6]/div/div/div[1]/div').text
        except:
            self.Custo_Gasto_Total_mes = 0.00
        print("Raspagem de dados Custos Fixos concluído!!!.")

    def fechar_browser(self):
        print("Fechando navegador. Bye!!")
        time.sleep(5)
        self.driver.close()



