import re
import yaml

def __get_jekyll_front_matter():
    text = ''
    with open('samples/sample-issue.md') as f:
        text = f.read()

    regex = r'^\s*<!--.*\n^---$([\w\W]*)^---$\n-->\s*$'
    result = re.search(regex, text, re.MULTILINE)
    if result is None:
        return
    _front_matter = result.group(1).strip()

    data = yaml.load(_front_matter)
    print(data)
    # {'layout': 'post', 'title': None, 'image': None, 'description': None, 'categories': ['Calculus', 'Math', 'Khan Academy']} categories: [Calculus, Math, Khan Academy]

    text_2 = yaml.dump(data).strip()
    print(text_2)

# Run
__get_jekyll_front_matter()





def _get_title():
    _title = None
    text = ''
    with open('samples/sample-issue.md') as f:
        text = f.read()

    regex = r'^\#\s+(.+)$' 
    matches = re.findall(regex, text, re.MULTILINE) 

    for m in matches:
        _title = m.strip()

    print(_title)

# _get_title()
