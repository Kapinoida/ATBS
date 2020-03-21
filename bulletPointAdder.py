#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)) :    # loops through all the indexes in lines
    lines[i] = '* ' + lines[i]  # add a star to each string_to_bytes
text = '\n'.join(lines)

pyperclip.copy(text)