import json

scenario_path = r'Replace/текст.json'
# form_path =
replace_elements = ["  ", "] (", "]\n(", " <br>", "<br> ", '<br>"', '\n"']

# with open(scenario_path, "r", encoding = "utf-8") as file:
#     text_files = json.load(file)
#     for text in text_files:
#         for e in replace_elements:
#             if text.find(e):
#                 text = text.replace("  ", " ")
#                 text = text.replace("] (", "](")
#                 text = text.replace("]\n(", "](")
#                 text = text.replace("<br> ", "<br>")
#                 text = text.replace("<br> ", "<br>")
#                 text = text.replace(" <br>", "<br>")
#                 text = text.replace('<br>"', '"')
#                 text = text.replace('\n"', '"')
#             else:
#                 print('false')

with open(scenario_path, "r", encoding="utf-8") as file:
    text_files = json.load(file)
    object_path = text_files['members'][1]['secretIdentity']
    # print(object_path)
    with open(scenario_path, "w", encoding="utf-8") as file_write:
        for text in text_files:
            text.replace("] (", "](")
            # text.replace("]\n(", "](")
            # text.replace("<br> ", "<br>")
            # text.replace("<br> ", "<br>")
            # text.replace(" <br>", "<br>")
            # text.replace('<br>"', '"')
            # text.replace('\n"', '"')
            json.dump(text, file_write, indent=4)
