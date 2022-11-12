import string
Blacklist = string.punctuation + "aáeéiíoóöőuúüű"
Lines = []

with open("hazi.txt",'r') as File:
    for line in File:
        if not (line == '' or line == '\n'):
            newLine = []
            for word in line.strip().split(" "):
                newWord = ''
                for char in word:
                    if not (char in Blacklist or char in Blacklist.upper()):
                        newWord += char
                if not newWord == '':
                    newLine.append(newWord)
            Lines.append(" ".join(newLine))

with open("Eredmeny","w") as File:
    File.write("\n".join(Lines))