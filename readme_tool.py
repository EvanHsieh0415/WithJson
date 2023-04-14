import re

title_regex_compile = re.compile(r'(\#+) (\*\*.+\*\*)(?:<a id="(.+)"></a>)?')

with open('./Readme_TW.md', encoding='utf8') as file_ref:
    file_lines = file_ref.read().splitlines()

for index, line in enumerate(file_lines):
    if match_object:=re.match(title_regex_compile, line):
        groups = match_object.group
        id = f' id=\"{groups(3)}\"' if groups(3) else ''
        level = len(groups(1))
        print(replaced_string:=f'<h{level}{id}>{groups(2)}</h{level}>')
        file_lines[index] = replaced_string

with open('./Readme_TW.edited.md', 'w', encoding='utf8') as file_ref:
    file_ref.write('\n'.join(file_lines))