#Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# fine phone number
phoneRegex = re.compile(r'''(
      (\d{3}|\(\d{3}\))?
      (\s|-|\.)?
      (\d{3})
      (\s|-|\.)
      (\d{4})
      (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)

# find email address
emailRegex = re.compile (r'''(
       [a-zA-Z09._%+-]  +
       @
       [a-zA-Z09.-] +
       (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# find urls
# URLs = re.compile (r'''(?:
#       [^\s()<>]
#       |
#       \(([^\s()<>] | (\([^\s()<>]+\)))*\)
#       )+
#       (?:
#       \(([^\s()<>]|(\(([^\s()<>]+\)))*\)
#       |
#       [^\s`!()\[\]{};:'".,<>?«»""'']
#       )
#
# )''')
# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')

phone = re.compile(r'''(
(\d{3}|\d{3}\d)?

)''',re.VERBOSE)