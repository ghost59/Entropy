import json 
from datetime import datetime
def display(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data["budget"]



def load_case(file_path, input): 
    with open(file_path, 'r') as f:
        data = json.load(f)
    data["budget"] += input
    print(data["budget"])
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

#load_case("D:\mara\Entropy\entropy.json", 300)


def burn(file_path, burn):
    with open(file_path, 'r+') as f:
        data = json.load(f)
    data['budget'] -= burn
    with open(file_path,'w') as f:
        json.dump(data,f, indent=4)
    print(data['budget'])

#burn("D:\mara\Entropy\entropy.json", 300)




