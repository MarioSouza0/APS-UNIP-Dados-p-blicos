from time import sleep
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    start_urls = ['https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx']

    def start_requests(self):
        # Configurar o driver do Selenium (certifique-se de ter o driver do Chrome ou Firefox instalado)
        self.driver = webdriver.Chrome()

        # Abrir a página
        self.driver.get("https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx")

        # Encontrar o botão "furto de veiculos" por ID
        button = self.driver.find_element(By.ID, "cphBody_btnFurtoVeiculo")

        # Clicar no botão
        button.click()

        # Esperar um pouco para a página carregar
        self.driver.implicitly_wait(5)


        #Para o ano de 2020
        button2020 = self.driver.find_element(By.ID, "cphBody_lkAno20")
        button2020.click()
        self.driver.implicitly_wait(15)

        buttonJaneiro2020 = self.driver.find_element(By.ID, "cphBody_lkMes1")
        buttonJaneiro2020.click()
        self.driver.implicitly_wait(5)

        export_button = self.driver.find_element(By.ID, "cphBody_ExportarBOLink")
        export_button.click()

        buttonFevereiro2020 = self.driver.find_element(By.ID, "cphBody_lkMes2")
        buttonFevereiro2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()
            

        buttonMarco2020 = self.driver.find_element(By.ID, "cphBody_lkMes3")
        buttonMarco2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonAbril2020 = self.driver.find_element(By.ID, "cphBody_lkMes4")
        buttonAbril2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonMaio2020 = self.driver.find_element(By.ID, "cphBody_lkMes5")
        buttonMaio2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()
        
        buttonJunho2020 = self.driver.find_element(By.ID, "cphBody_lkMes6")
        buttonJunho2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonJulho2020 = self.driver.find_element(By.ID, "cphBody_lkMes7")
        buttonJulho2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonAgosto2020 = self.driver.find_element(By.ID, "cphBody_lkMes8")
        buttonAgosto2020.click()
        self.driver.implicitly_wait(5)
        
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        
        export_button.click()

        buttonSetembro2020 = self.driver.find_element(By.ID, "cphBody_lkMes9")
        buttonSetembro2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonOutubro2020 = self.driver.find_element(By.ID, "cphBody_lkMes10")
        buttonOutubro2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonNovembro2020 = self.driver.find_element(By.ID, "cphBody_lkMes11")
        buttonNovembro2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonDezembro2020 = self.driver.find_element(By.ID, "cphBody_lkMes12")
        buttonDezembro2020.click()
        self.driver.implicitly_wait(5)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        #Para o ano de 2021
        button2021 = self.driver.find_element(By.ID, "cphBody_lkAno21")
        button2021.click()
        self.driver.implicitly_wait(15)

        buttonJaneiro2021 = self.driver.find_element(By.ID, "cphBody_lkMes1")
        buttonJaneiro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonFevereiro2021 = self.driver.find_element(By.ID, "cphBody_lkMes2")
        buttonFevereiro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonMarco2021 = self.driver.find_element(By.ID, "cphBody_lkMes3")
        buttonMarco2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonAbril2021 = self.driver.find_element(By.ID, "cphBody_lkMes4")
        buttonAbril2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonMaio2021 = self.driver.find_element(By.ID, "cphBody_lkMes5")
        buttonMaio2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()
        
        buttonJunho2021 = self.driver.find_element(By.ID, "cphBody_lkMes6")
        buttonJunho2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonJulho2021 = self.driver.find_element(By.ID, "cphBody_lkMes7")
        buttonJulho2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonAgosto2021 = self.driver.find_element(By.ID, "cphBody_lkMes8")
        buttonAgosto2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonSetembro2021 = self.driver.find_element(By.ID, "cphBody_lkMes9")
        buttonSetembro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonOutubro2021 = self.driver.find_element(By.ID, "cphBody_lkMes10")
        buttonOutubro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonNovembro2021 = self.driver.find_element(By.ID, "cphBody_lkMes11")
        buttonNovembro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonDezembro2021 = self.driver.find_element(By.ID, "cphBody_lkMes12")
        buttonDezembro2021.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        #Para o ano de 2022
        button2022 = self.driver.find_element(By.ID, "cphBody_lkAno22")
        button2022.click()
        self.driver.implicitly_wait(15)

        buttonJaneiro2022 = self.driver.find_element(By.ID, "cphBody_lkMes1")
        buttonJaneiro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonFevereiro2022 = self.driver.find_element(By.ID, "cphBody_lkMes2")
        buttonFevereiro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonMarco2022 = self.driver.find_element(By.ID, "cphBody_lkMes3")
        buttonMarco2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonAbril2022 = self.driver.find_element(By.ID, "cphBody_lkMes4")
        buttonAbril2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonMaio2022 = self.driver.find_element(By.ID, "cphBody_lkMes5")
        buttonMaio2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()
        
        buttonJunho2022 = self.driver.find_element(By.ID, "cphBody_lkMes6")
        buttonJunho2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonJulho2022 = self.driver.find_element(By.ID, "cphBody_lkMes7")
        buttonJulho2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonAgosto2022 = self.driver.find_element(By.ID, "cphBody_lkMes8")
        buttonAgosto2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonSetembro2022 = self.driver.find_element(By.ID, "cphBody_lkMes9")
        buttonSetembro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonOutubro2022 = self.driver.find_element(By.ID, "cphBody_lkMes10")
        buttonOutubro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()

        buttonNovembro2022 = self.driver.find_element(By.ID, "cphBody_lkMes11")
        buttonNovembro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()


        buttonDezembro2022 = self.driver.find_element(By.ID, "cphBody_lkMes12")
        buttonDezembro2022.click()
        self.driver.implicitly_wait(30)
        export_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphBody_ExportarBOLink")))
        export_button.click()
        
        # Fechar o navegador
        self.driver.quit()

    