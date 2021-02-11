import win32com.client as win32
import os
import os.path
import json
from zipfile import ZipFile
import time
import shutil

def send_scenario(scenarioGUID):
    global mailSigma, currentPath
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    mail.To = mailSigma
    mail.Subject = scenarioGUID
    attachment = currentPath + '\\' + scenarioGUID + ".json"
    mail.Attachments.Add(attachment)
    mail.Send()
    os.remove(currentPath + '\\' + scenarioGUID + ".json")
    
def prep_scenaio(scenarioGUID):

    global currentPath
    scenarioPath = currentPath + "\\scenario"

    for path in os.listdir(scenarioPath):
        if os.path.isdir(scenarioPath + "\\" + path):
            if 'scenario.json' in os.listdir(scenarioPath + "\\" + path):
                oldGUID = path

                with open(scenarioPath +  "\\" + path + "\\scenario.json", "r", encoding="utf-8") as scenario:
                    data = json.loads(scenario.read().replace(oldGUID, scenarioGUID))

                data["scenario"][scenarioGUID]["switched_off"] = False
                data["intent"][scenarioGUID]["enabled"] = True
                

                with open(currentPath + "\\" + scenarioGUID + ".json", "w", encoding="utf-8") as scenario:
                    scenario.write(json.dumps(data, indent=2, ensure_ascii=False))
                    
                shutil.rmtree(currentPath + "\\scenario")
                send_scenario(scenarioGUID)

                    
def unzip(fname):
    with ZipFile(fname, 'r') as zip:
        zip.extractall('scenario')
    os.remove(fname)
    prep_scenaio(fname[:-4])


if __name__ == '__main__':

    mailSigma = ''
    currentPath = os.getcwd()

    while True:
        for fname in os.listdir():
            if fname.endswith('.zip'):
                time.sleep(2.5)
                unzip(fname)