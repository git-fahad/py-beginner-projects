import re


text_string = '''
####Random wall of multi line text ####

His critique culminated in a 
substantial tome, al-Radd 'ald al-Mantiqiyyin, one of the most devastating
attacks ever levelled against the logic upheld by the early Greeks, the later 
commentators, and their Muslim followers.

###numbers###

673y209874r89832-e903

###Special chars####

#@$%!*)!@*^#%@*#&(@#)

6867.23.3434

###test###

%#^&75767hyugi2vgdhu232786&*(guhi)

cat 
mat
bat
tat

Mr. Tom
Mr Smith
Mrs. Teddy
Ms June
Mr. T
'''
pattern = re.compile(r'\d\d\d[yr][28]')
matches = pattern.finditer(text_string)

for match in matches:
    print(match)

# Finding a range
pattern = re.compile(r'[1-6]')
matches = pattern.finditer(text_string)

for match in matches:
    print(match)


# NOT the character
pattern = re.compile(r'[^a]')
matches = pattern.finditer(text_string)

for match in matches:
    print(match)

pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_string)

for match in matches:
    print(match)

# Quantifiers
    
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*')
matches = pattern.finditer(text_string)

for match in matches:
    print(match)

