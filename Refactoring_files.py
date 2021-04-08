import tkinter
import tkinter.filedialog
from tkinter.messagebox import askquestion
import os
from os import path
import json
from random import choice


# def path_config():
#     if path.exists("samples\config.txt"):
#         with open('samples\config.txt', 'r') as nlp_path:
#             NLPpath = nlp_path.readline()
#     else:
#         NLPpath = tkinter.filedialog.askdirectory()
#         with open('samples\config.txt', 'w') as nlp_path:
#             nlp_path.write((os.sep).join(NLPpath.split('/')))
#     return (os.sep).join(NLPpath.split('/'))
#

def
def random_phrase():
def file_catch():
    while True:
        for fname in os.listdir():
            if fname.endswith('.json'):
                scenarioGUID = fname[:-5]
                choosenWL = askquestion(title="Найден файл", message=("Загрузить на WL?"))
                if choosenWL == 'yes':
                    scen_word = random_phrase()
                    WL = True
                    load_file(scenarioGUID, WL, scen_word)
                else:
                    load_file(scenarioGUID)


def load_file(scenarioGUID, WL=False, scen_word=''):
    global NLPpath

    with open(scenarioGUID + ".json", "r", encoding="utf-8") as scenario:
        data = json.loads(scenario.read().replace(scenarioGUID,
                                                  scenarioGUID[:11] + "WL_" + scenarioGUID[
                                                                              11:]) if WL else scenario.read())
    if WL:
        scenarioGUID = scenarioGUID[:11] + "WL_" + scenarioGUID[11:]
        intent_name = scenarioGUID + '_intent.json'
        intents_dir = NLPpath + os.sep + os.path.join("intents", "SBERBANK_MESSENGER") + os.sep

        with open("samples\whitelist_req.json", "r", encoding="utf-8") as req:
            whitelist_req = json.load(req)

        data["intent"][scenarioGUID]["classifier"]["samples_positive"] = [scen_word]
        data["intent"][scenarioGUID]["requirement"] = whitelist_req
        # Строка удаления channels
        del data["intent"][scenarioGUID]["channels"]

        with open(intents_dir + intent_name, 'w', encoding="utf-8") as intent:
            intent.write(json.dumps(data["intent"], indent=2, ensure_ascii=False))

    scenarios_dir = NLPpath + os.path.join("scenarios", "SBERBANK_MESSENGER") + os.sep
    forms_dir = NLPpath + os.path.join("forms", "SBERBANK_MESSENGER") + os.sep

    with open("samples\start_node.json", "r", encoding="utf-8") as s_node:
        csi_cont = json.load(s_node)

    scenario_name = scenarioGUID + '_scenario.json'
    form_name = scenarioGUID + '_form.json'

    data['form'][scenarioGUID]["forms"]['start_node']['fields'] = csi_cont
    data['form'][scenarioGUID]["forms"]['start_node']['fields']['success_action_scenario_id']['questions'][1][
        'form'] = scenarioGUID

    with open(scenarios_dir + scenario_name, 'w', encoding="utf-8") as scenario:
        scenario.write(json.dumps(data["scenario"], indent=2, ensure_ascii=False))
    with open(forms_dir + form_name, 'w', encoding="utf-8") as form:
        form.write(json.dumps(data["form"], indent=2, ensure_ascii=False))

    os.remove(scenarioGUID.replace("WL_", "") + '.txt')


if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    NLPpath = r"C:\Users\18411029\Documents\ProjectPython\Sber\sb900-static-rb\references\\"

    file_catch()
