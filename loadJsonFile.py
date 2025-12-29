import json

def loadFromFile(filename='user_data_tiktok.json',enc='utf-8'):
    try:
        with open(filename,'r',encoding=enc) as file:
            data =json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could nott decode JSON from the file {filename}.")
        return None