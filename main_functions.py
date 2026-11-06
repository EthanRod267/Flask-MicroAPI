import json

# A function to save a json document to a file
def save_json(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file)
        print(f"File {filename} was successfully saved")


# A function to load a json document from a file
# python received data as a dictionary
def read_from_file(filename):
    with open(filename, 'r') as read_file:
        received_data = json.load(read_file)
        print(f"File{filename} was successfully loaded")
        return received_data