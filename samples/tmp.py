import re
import yaml

_front_matter = None
text_issue = ''
with open('samples/sample-issue.md') as f:
    text_issue = f.read()

regex = r'^\s*<!--.*\n^---$([\w\W]*)^---$\n-->\s*$'
matches = re.findall(regex, text_issue, re.MULTILINE) 

for m in matches:
    _front_matter = m.strip()

print(_front_matter)


_title = None
text_title = ''
with open('samples/sample-issue.md') as f:
    text_title = f.read()

regex = r'^\#\s+(.+)$' 
matches = re.findall(regex, text_title, re.MULTILINE) 

for m in matches:
    _title = m.strip()

print(_title)
