import re
import yaml

def __get_jekyll_front_matter():
    _front_matter = None
    text_issue = ''
    with open('samples/sample-issue.md') as f:
        text_issue = f.read()

    regex = r'^\s*<!--.*\n^---$([\w\W]*)^---$\n-->\s*$'
    matches = re.findall(regex, text_issue, re.MULTILINE) 
    for m in matches:
        _front_matter = m.strip()

    obj_front_matter = yaml.load(_front_matter)
    print(obj_front_matter)
    # {'layout': 'post', 'title': None, 'image': None, 'description': None, 'categories': ['Calculus', 'Math', 'Khan Academy']} categories: [Calculus, Math, Khan Academy]

    _yml_front_matter = yaml.dump(obj_front_matter)
    print(_yml_front_matter)

# Run
__get_jekyll_front_matter()





def _get_title():
    _title = None
    text_title = ''
    with open('samples/sample-issue.md') as f:
        text_title = f.read()

    regex = r'^\#\s+(.+)$' 
    matches = re.findall(regex, text_title, re.MULTILINE) 

    for m in matches:
        _title = m.strip()

    print(_title)

# _get_title()
