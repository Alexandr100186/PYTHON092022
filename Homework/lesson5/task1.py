# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import re

s = "Напишите программу, удаляющую из текста все слова, содержащие абв автобус"
words = re.split('\W+', s)
print(words)
lett = ["а", "б", "в"]

for i in range(len(words)):
    if words[i].find(lett[0]) != -1 and words[i].find(lett[1]) != -1 and words[i].find(lett[2]) != -1:
        words[i] = None

words = [txt for txt in words if txt]
print(*words)
