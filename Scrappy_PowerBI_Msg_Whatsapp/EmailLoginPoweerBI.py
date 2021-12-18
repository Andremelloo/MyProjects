import Secret
import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# secret = Secret.email_senha() ## somente para nao aparecer as senha no codigo
# secret.password  ## usando a senha secreta
# secret.email  ## usando email secreto
# 
# start = LoginEmailPowerBi(secret.email, secret.password)
# start.login_email_powerbi()



class LoginEmailPowerBi:
    print("Iniciando o Programar de fazer login no Email no site do PowerBi")
    def __init__(self, email, senha):
        dir_path = os.getcwd()  ##pega local de onde esta executando o script
        #print(dir_path)
        profile = os.path.join(dir_path, "profile", "wpp")  ##cria as pastas para armazenar os cookies
        #print(profile)
        options = Options()
        #print(options)
        options.add_argument(r"user-data-dir={}".format(profile))
        self.driver = webdriver.Chrome(options=options)
        
        self.Url_Link_Powerbi_Disponibilidade = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=871c010f-5e61-4fb1-83ac-98610a7e9110&response_type=code%20id_token&scope=openid%20profile%20offline_access&state=OpenIdConnect.AuthenticationProperties%3DXNpuhpNJVqETiH_zt8fyPPMa-yyULvrDLdLZET3KLJkYAe8xUvLBsn3A_ZBmmxlDXyeyHjpRVey8MhiY6d88Qt1cFXoXepuggloD7sTaHvkJ7ojmOaTtQYLk-OQ1oA7pHuU8ygjLIaLlsyYHiTnK-J-7W77OLXhgTmxxC7I6tbdahPCza2C-8HNvQ-UcIG9q_kTefrYVo-wdKBLfsmXb9bbgDjvw-x0VRkjJSl_70wcd30vh_uECO770x4jcTY-6c3dbrZSQZsnJZG-cMebs8lhsCHVIfDvnEJJZZ-lhLGF_Uk7q7p8pWNnGtZeJxV1H_tWXRnC4zn1qEM5woBO8lH9OfRFwomX9oUgPNUtFQGA4Aydq_M6o9LjEE59-NtHzchaHYQTwES8ZIkqM6YW8CoUsjrxC4Mk_ztFmDn-wCRc&response_mode=form_post&nonce=637698681742808826.MGU4NmMxYjYtNmJjZC00MjJhLWJkMjctZjk1OWJmMDM0YzQ0MDkxODUwNjYtYjJiMi00MjUwLWI3MWYtZGEzMTI1YzdkOWQx&site_id=500453&redirect_uri=https%3A%2F%2Fapp.powerbi.com%2Fgroups%2F5131fe96-a1b6-4a68-856c-e1899835f992%2Freports%2F6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8%2FReportSection7257dff8a8fca8c3da58%3Flanguage%3Den-US&post_logout_redirect_uri=https%3A%2F%2Fapp.powerbi.com%2Fgroups%2F5131fe96-a1b6-4a68-856c-e1899835f992%2Freports%2F6b3c5f6c-b98b-48aa-87d2-ce5dc400fee8%2FReportSection7257dff8a8fca8c3da58%3Flanguage%3Den-US&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&nux=1&msafed=0&x-client-SKU=ID_NET461&x-client-ver=5.6.0.0"
        self.email = email
        self.senha = senha

    def login_email_powerbi(self):
        print("Entrando no site do PowerBi e fazendo login.")
        print("Loading...")
        self.driver.get(self.Url_Link_Powerbi_Disponibilidade)

        time.sleep(10)

        self.driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(self.email)  ## localizar um elemento na pagina pelo ID
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(self.senha) ## clica no botao
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()  ## clica no botao
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        print("Login no email OK!!")

        time.sleep(20)



