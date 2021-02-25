from selenium import webdriver
from datetime import datetime, timedelta
import time
import os
import logging

#SORRY FOR ALL THE COMMENTS, MY LEADER WANTED ME TO ADD THEM AND I THINK IT WAS A GOOD IDEA TO LEAVE IT LIKE THIS FOR YOU TO SEE :)

# Creating a variable of the current date
ifiledate = datetime.today()
# Creating a variable of the current date with 2 days less
# If the date is 2020-12-18 the variable will be 2020-12-16
sfiledate = datetime.today() - timedelta(days=3)
# Creating format of the logging messages
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)

###############################
# SETTING UP AND OPENING CHROME#
###############################
# Configuring GoogleChrome to be headless and creating a variable with the download folder
options = webdriver.ChromeOptions()
options.add_argument("headless")
download_path = r'C:\Users\PATH'
# Creating a variable with the chromerdrive.exe so the script can use it
# Changing the configuration of the browser
# Changing the downloads folder to the folder below
browser = webdriver.Chrome(executable_path=r'C:\Users\PATH\chromedriver.exe', options=options)
browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
command_result = browser.execute("send_command", params)
# Open Chrome and go to the portal
logging.warning('Opening the browser, going to the portal and closing a pop up...')
browser.get('http://webpage.com/directory/')

#######
#LOGIN#
#######
# Closing the pop up "Comunicado a Proveedores"
browser.find_element_by_xpath('//*[@id="mostrarmodal"]/div/div/div[3]/a').click()
# Creating variables for username and password login fields
username = browser.find_element_by_xpath('//*[@id="T1"]')
password = browser.find_element_by_xpath('//*[@id="T2"]')
# Filling the username and password fields with the current credentials
logging.warning('Login in...')
username.send_keys('user')
password.send_keys('12345')
# Click on "Ingresar"
browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/form/table/tbody/tr[6]/td/input').click()
# Click on "He leido y acepto el aviso"
browser.find_element_by_xpath('//*[@id="aceptar_condiciones"]').click()
# Click on "Continuar"
browser.find_element_by_xpath('//*[@id="aceptar_condiciones"]').click()
logging.warning('Login successful!')

#############
##INVENTORY##
#############
logging.warning('Downloading inventory file for date ' + ifiledate.date().strftime('%Y-%m-%d') + '...')
# Click on "Existencias"
browser.find_element_by_xpath('//*[@id="content"]/tbody/tr[2]/td/table/tbody/tr[1]/td/ul/li[1]/a').click()
# Click on "Buscar"
browser.find_element_by_xpath('//*[@id="buscarExistencias"]').click()
# Click on "Exportar"
browser.find_element_by_xpath('//*[@id="exportar"]').click()
# Waiting for 30 seconds so we can make sure our download has been completed before renaming it :)
time.sleep(30)
logging.warning('File download successful!')
# Renaming de file
logging.warning('Renaming file...')
os.rename(r'C:\Users\PATHWITHCURRENTFILENAME', r'C:\Users\PATHWITHNEWFILENAME' + ifiledate.date().strftime('%Y%m%d') + ".xls")

#########
##SALES##
#########
logging.warning('Downloading sales file for date ' + sfiledate.date().strftime('%Y-%m-%d') + '...')
# Click on "Ventas"
browser.find_element_by_xpath('//*[@id="content"]/tbody/tr[2]/td/table/tbody/tr[1]/td/ul/li[2]/a').click()
# Calendar section
# Creating variables for "Fecha de:" and "a" fields which basically are the date range
fecha1 = browser.find_element_by_xpath('//*[@id="formFechade"]')
fecha2 = browser.find_element_by_xpath('//*[@id="formFechaa"]')
# Clearing the date fields and inserting the date we want using our filedate variable anf writing it in the format we want
fecha1.clear()
fecha1.send_keys(sfiledate.date().strftime('%d-%m-%Y'))
fecha2.clear()
fecha2.send_keys(sfiledate.date().strftime('%d-%m-%Y'))
time.sleep(1)
# Minimizing calendar
browser.find_element_by_xpath('//*[@id="content"]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/form[1]/div/img[2]').click()
# Click on "Buscar"
browser.find_element_by_xpath('//*[@id="buscarVentas"]').click()
# Click on "Exportar"
browser.find_element_by_xpath('//*[@id="exportar"]').click()
# Waiting for 10 seconds so we can make sure our download has been completed before renaming it :)
time.sleep(15)
logging.warning('File download successful!')
# Renaming de file
logging.warning('Renaming file...')
os.rename(r'C:\Users\PATHWITHCURRENTFILENAME', r'C:\Users\PATHWITHNEWFILENAME' + sfiledate.date().strftime('%Y%m%d') + ".xls")

logging.warning('Files were downloaded successfully!')
logging.warning('Exiting...')
# Closing the browser
browser.quit()
