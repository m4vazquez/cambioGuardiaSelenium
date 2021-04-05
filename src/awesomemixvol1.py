#librerias
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(driver_path, options= options)

#inicializar el navegador
driver.get('http://centralvirtual.iplan.com.ar/Login/')

#realizo el login
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.NAME,
                                       'EnteredUserID')))\
    .send_keys(os.environ['centralVirtualUser'])
#coloco la pass
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'Password'))).send_keys(os.environ['centralVirtualPassword'])
#logueo
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()

#entro a llamadas entrantes
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Llamadas Entrantes'))).click()
#entro a desvio incondicional - encendido
#time.sleep(2)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, '/User/CF/Always/'))).click()

#ver del numero cargado

a = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#forwardedToNumber'))).get_attribute('value')
print (a)

arc = open('guardianesDeLaGalaxia.csv')
guardianesList = []
for i in arc:
    guardianesList = i.split(',')
print (guardianesList)
guardianeslen = (len(guardianesList))
guardian = (guardianesList.index(a))

#veo quien entra de guardia
if guardian == (guardianeslen -1):
    entra=guardianesList[0]
    num=guardianesList[1]
else:
    entra=guardianesList[guardian+1]
    num=guardianesList[guardian+2]
print('Estaba de guardia {}'.format(guardianesList[guardian-1]))
print('Entró de guardia {}, con el numero {}'.format(entra, num))
#print(os.environ['centralVirtualUser'])

#limpio el numero del que entra de guardia
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#forwardedToNumber'))).clear()

#colocar el numero del que entra de guardia
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#forwardedToNumber'))).send_keys(num)

#aceptar
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'ok'))).click()

driver.quit()
