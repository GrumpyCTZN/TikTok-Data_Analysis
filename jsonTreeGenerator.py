import loadJsonFile as lg
def export_json_tree(data, file_obj):
    if isinstance(data, dict):
        items = list(data.items())
        for i, (key, value) in enumerate(items):
            connector = "├── " if i < len(items) - 1 else "└── "
            line = "│   " + connector + str(key)
            file_obj.write(line + "\n")
            
            # Dive into nested structures
            if isinstance(value, (dict, list)):
                export_json_tree(value, file_obj)
                
    elif isinstance(data, list):
        if len(data) > 0:
            line = "│   " + "└── [List Items]"
            file_obj.write(line + "\n")
            # We look at the first item to show the structure of objects in the list
            export_json_tree(data[0], file_obj)

jsonData=lg.loadFromFile('test.json')

with open(f'json_structure_tree-1.txt', 'w', encoding='utf-8') as out_file:
    out_file.write("ROOT\n")
    export_json_tree(jsonData, out_file) 
