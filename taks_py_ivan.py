#!/usr/bin/python3
import argparse
from datetime import datetime
import os
import json
import taskspy_conf

path_to_txt_file = taskspy_conf.PATH_TO_FILE
file_name = "TASKS_DATA.json"

parse = argparse.ArgumentParser()
parse.add_argument("-a", "--dodaj", help="Dodaj zadatak")
parse.add_argument("-d", "--izbrisi", help="Izbrisi zadatak")
parse.add_argument("-l", "--lista", help="Izlistaj sve zadatke", action="store_true")
# parse.add_argument("-p", "--stampa", help="Print fajl")
parse.add_argument("-c", "--provera", help="Proverite podesavanja", action="store_true")

args = parse.parse_args()

def check_if_file_exists():
    """
    Check if path to file is setup correctly
    """
    try:
        if file_name in os.listdir(path_to_txt_file):
            return True
        else:
            with open(os.path.join(path_to_txt_file, file_name), "a") as f:
                json.dump({}, f)
            return True
    except:
        return False
def ocitaj_json():
    with open(os.path.join(path_to_txt_file, file_name), "r") as ff:
        old_data = json.load(ff)
    return old_data

def napravi_json(old_data):
    with open(os.path.join(path_to_txt_file, file_name), "w") as f:
        json.dump(old_data, f)


def dodaj_zadatak(zadatak):
    cur_time = datetime.now()
    old_data = ocitaj_json()
    index = int(list(old_data.keys())[-1]) + 1
    old_data[index]={"zadatak":zadatak, "vreme":str(cur_time)}
    napravi_json(old_data)

def izbrisi_zadatak(id_zadatka):
    old_data = ocitaj_json()
    del old_data[id_zadatka]
    napravi_json(old_data)


if args.dodaj:
    dodaj_zadatak(args.dodaj)
    print(f"Zadatak {args.dodaj} dodat")
elif args.izbrisi:
    izbrisi_zadatak(args.izbrisi)
    print("Izbrisi zadatak")
elif args.lista:
    data = ocitaj_json()
    for x in data:
        print(f"{x}, {data[x]['zadatak']}, {data[x]['vreme']}")
elif args.provera:
    print(check_if_file_exists())
else:
    print("Molimo pokrenite komandu add_test.py -h za pomoc oko opcija")


def add_task(task):
    pass
