import os

def parseFiles(text):
    text = text.split('## ')
    tag = ""
    for t in text:
        if(t[:3] == "Tag"):
            tag = t
            break

    tag = tag.replace("\n", "")
    tag = tag.split("```")
    tagTmp = []
    for i in range(len(tag)):
        if(i % 2 == 1):
            tagTmp.append(tag[i])
    tag = tagTmp

    return tag


fo = open("ReadMe.md", 'w')
fo.write("# LeedCode\n")

## By problem id
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
        fi = open(file, 'r')
        text = fi.read()
        fi.close()

        tag = parseFiles(text)

        fo.write('| ')
        fo.write('[' + file.split('.')[0] + '](' + file + ')' )
        fo.write(' | ')

        fg = 1
        for t in tag:
            if (fg):
                fo.write("```")
                fg = 0
            else:
                fo.write(", ```")
            fo.write(t)
            fo.write("```")

        fo.write(' |\n')
fo.write('|||\n')
fo.write('\n')

## By problem type
typeSet = ["graph", "linked list"]

for type in typeSet:
    fo.write("## " + type + "\n")
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
            fi = open(file, 'r')
            text = fi.read()
            fi.close()

            tag = parseFiles(text)

            if type not in tag:
                continue

            fo.write('| ')
            fo.write('[' + file.split('.')[0] + '](' + file + ')' )
            fo.write(' | ')

            fg = 1
            for t in tag:
                if (fg):
                    fo.write("```")
                    fg = 0
                else:
                    fo.write(", ```")
                fo.write(t)
                fo.write("```")

            fo.write(' |\n')

    fo.write('|||\n')
    fo.write('\n')

