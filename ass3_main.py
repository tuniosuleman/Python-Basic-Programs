from datetime import date
import datetime
import functools
from functools import reduce
import json

My_Dict = {
        'person_1': {'name': ' Abdul Rafay', 'age': 22, 'Interests': ['football,cricket'],
                     'amount_deposited': [24000, 26000]},
        'person_2': {'name': 'Nancy James', 'age': 23, 'Interests': ['baseball,cricket'],
                     'amount_deposited': [24000, 27000]},
        'person_3': {'name': 'Selena Gomez', 'age': 26, 'Interests': ['baseball,table tennis'],
                     'amount_deposited': [24000, 28000]}
}

def chars_with_exceptions(tuple_chars):
    alphabets = [chr(i)  for i in range(97, 123) if i not in tuple_chars]
    return tuple(alphabets)

def from_a_to_g_char(from_a, _to_g):
    alphabets = [chr(i)  for i in range(from_a, _to_g) ]
    return tuple(alphabets)

def main_keys(dict):
    persons = dict.keys()
    return persons
def names_of_dic(dict):
    dict_names = [My_Dict[person]['name'].strip() for person in main_keys(dict)]
    return dict_names
    
Names_dict = names_of_dic(My_Dict)
func_Mr_Ms = lambda x: 'Mr. ' + x if str(x).lower().startswith(from_a_to_g_char(97, 104)) else 'Ms. ' + x
Mr_Ms_concatenated = list(map(func_Mr_Ms, Names_dict))

tuple_chars = (107, 109, 115)  # k, m, s characters respectively
func_remove = lambda x:str(x.split(' ')[1])[0].lower().startswith(chars_with_exceptions(tuple_chars))
names_filtered = list(filter(func_remove, Mr_Ms_concatenated))

#adding  Mr_Ms_concatenated names , year and amount deposited...
current_year = date.today().year
Index = 0
list_of_persons = main_keys(My_Dict)

for person in list_of_persons:
    if Index == 2:
        del My_Dict[person]
        break
    elif str(My_Dict[person]['name']).strip().split(' ')[0][0].lower() == str(names_filtered[Index]).split(' ')[1][0].lower():
        My_Dict[person]['name'] = names_filtered[Index]
        My_Dict[person]['Year'] = current_year - int(My_Dict[person]['age']) -1
        My_Dict[person]['amount_deposited'] = reduce(lambda x,y:x+y, My_Dict[person]['amount_deposited'])
    Index +=1

#updating dictionary...
updated_dic = {}
updated_dic["current_Date"] = datetime.datetime.now().strftime('%d-%b-%Y')
updated_dic["Data"] = My_Dict

#writing dictionary to json
with open("names.json", "w") as json_file:
    json.dump(updated_dic, json_file)
