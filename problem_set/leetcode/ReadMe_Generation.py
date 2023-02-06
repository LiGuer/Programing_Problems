import os

fo = open("ReadMe.md", 'w')
fo.write("| problem id | tag |\n")
fo.write("| :---: | :---: |\n")

for root, dirs, files in os.walk("./"):
    filesTmp = []

    for file in files:
        if(file[0] < '0' or file[0] > '9'):
            continue
        filesTmp.append(file)
    
    files = filesTmp
    files.sort(key = lambda x : int(x.split(".")[0]))
    
    for file in files:
        if(file[0] < '0' or file[0] > '9'):
            continue

        fi = open(file, 'r', encoding='UTF-8')
        text = fi.read()
        fi.close()

        text = text.split('## ')
        tag = ""
        for t in text:
            if(t[:3] == "Tag"):
                tag = t[3:]
                break

        tag = tag.replace("\n", "")

        fo.write('| ')
        fo.write('[' + file.split('.')[0] + '](' + file + ')' )
        fo.write(' | ')
        fo.write(tag)
        fo.write(' |\n')

