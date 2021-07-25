import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val', default=None)
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

try:
    def json_write(dict_parser):
        try:
            date = json.load(open("storage_path"))
        except:
            date = []
        with open("storage_path", 'w', encoding='utf-8') as file:
            date.append(dict_parser)
            json.dump(date, file, indent=2)


    if args.key and args.val:
        dict_parser = {args.key: args.val}
        json_write(dict_parser)
        print(dict_parser)
        print('Добавил словарь!')

    elif args.key:
        with open('storage_path', 'r', encoding="utf-8") as f:
            date_json = json.load(f)
            for key in date_json:
                if args.key in key:
                    print(key[args.key], end=', ')
                else:
                    print(None)
except:
    with open("storage_path", 'w', encoding='utf-8') as file:
        json.dump(file)
