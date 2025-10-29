import json

'''returns the text contents of a file
@param
    filename: str
        name of file to read from
@returns: str
    The entire file
'''
def get_text(filename) -> str:
    with open(filename, 'r') as fpt:
        return fpt.read()

''' returns the python object from a json file
@param
    filename: str
        name of json file to read from
@returns: dict
    python dictionary from file
'''
def get_json_dictionary(filename) -> {}:
    with open(filename, 'r') as fpt:
        return json.load(fpt)

''' Creates new file with given filename and content
@param
    filename: str
        The name of the new file
    text: str
        The contents of the new file
@returns: None
'''
def create_new_file(filename, text) -> None:
    with open(filename, 'w') as fpt:
        fpt.write(text)
    return None
        
def main() -> None:
    FILENAME = 'news.txt'
    NEW_FILENAME = 'fake_news.txt'
    JSON_FILENAME = 'subs.json'

    text = get_text(FILENAME)
    subtitutions = get_json_dictionary(JSON_FILENAME)

    for k, v in subtitutions.items():
        text = text.replace(k, v)

    create_new_file(NEW_FILENAME, text)

if __name__ == '__main__':
    main()
