from selenium import webdriver
import time

Documents= ["pdf","doc","docx","csv","xls","xlsx","txt","rtf","odt","ppt","pptx","pptm","xml","klm"]
Databases = [ "php", "sql", "sqlite", "pdb", "idb", "cdb","sis", "odb"]
Softwares = ["env", "cfg", "conf","config","cfm","log","inf"]

dataConfig = ["Documents", "documents","databases", "Databases", "Softwares", "softwares"]
govLink=(input("[+] Please enter any Philipppine Government Website: "))
scanConfig = (input("[+] Choose and type one set of data to scan (Documents, Databases, Softwares): "))
if scanConfig not in dataConfig:
    print("Invalid input. Please try again. ")
    exit()
keyWord = (input("[+] Enter a keyword (Press Enter if there is no specific keyword): "))

print("")
print("===============================")
print("Opening Google Chrome...")
print("===============================")
print("")

time.sleep(2)

browser = webdriver.Chrome('/home/kali/Downloads/chromedriver')

if scanConfig in "Documentsdocuments":
    for i in range(len(Documents)):
        elements = browser.execute_script('''window.open("http://google.com/search?q=site%3A'''+str(govLink)+'''+filetype%3A'''+str(Documents[i])+'''+%22'''+str(keyWord)+'''%22", "_blank")''')
elif scanConfig in "Databasesdatabases":
    for i in range(len(Databases)):
        elements = browser.execute_script('''window.open("http://google.com/search?q=site%3A'''+str(govLink)+'''+filetype%3A'''+str(Databases[i])+'''+%22'''+str(keyWord)+'''%22", "_blank")''')
elif scanConfig in "Sofwaressoftwares":
    for i in range(len(Softwares)):
        elements = browser.execute_script('''window.open("http://google.com/search?q=site%3A'''+str(govLink)+'''+filetype%3A'''+str(Databases[i])+'''+%22'''+str(keyWord)+'''%22", "_blank")''')
