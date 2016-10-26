import re

file = open("file_to_read.txt", "r")

for line in file:
    matchList = re.findall("[a-zA-Z0-9_\+\.\-]+@[a-zA-Z0-9\_\.]+\.[a-zA-Z]+", line, re.DOTALL)
    if len(matchList) > 0:
        for match in matchList:
            print(match)