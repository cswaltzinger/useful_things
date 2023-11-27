from sys import argv as arg
fn = arg[1]
fle = open(fn,"r")

def count_beg(c,str):
    i = 0
    while i < len(str) and c == str[i]:
        i+=1
    return i;
def in_beg(tok,line):
    i = 0
    while line[i] == ' ':
        i+=1
    if (line[i:].split(" "))[0] == tok:
        return True
    else:
        return False

def isFor(line):
    return in_beg("for",line)
def isWhile(line):
    return in_beg("while",line)
def isIf(line):
    return in_beg("if",line)
def isElif(line):
    return in_beg("elif",line)
def isElse(line):
    return in_beg("else:",line)
def backend(str):
    return f'\\End{str[0].upper()+str[1:]}'
def stateLine(line):
    i = 0
    while line[i] == ' ':
        i+=1
    return line[:i] + "\State "+line[i:]

def frontend(str):
    return f'\\{str[0].upper()+str[1:]}'

indents = []
output = ""
tc =0
curNumTabs =-1
def printCit(line):
    print("\n"*10,"==================\n")
    print("\t"*10,"LINE:|",line[:-1],"|\t  ",isElse(line))
    global indents
    global tc
    global output
    global curNumTabs
    print("\t|",tc)
    print("\t|",indents)
    print("\t|",curNumTabs)
    print("============\n",output,"\n============","\n"*10)

for line in fle:
    #print(line[:-1], "\t|",line.split(), "\t",count_beg(" ",line))

    curNumTabs = count_beg(" ",line)
    end = ""
    #printCit(line)
    while (len(indents) > 0) and (curNumTabs < (len(indents))):
        e =backend(indents.pop(-1))
        tc = len(indents)
        output += ("    "*(tc))+f'{e}\n'
    if isFor(line):
        i = line.index("for")
        args = line[i + len("for"):-2]
        output += ('    '*tc )+  f'{frontend("for")}'
        output += "{ " + args+ " }\n"
        tc+=1
        indents.append("for")
    elif isWhile(line):
        i = line.index("while")
        args = line[i + len("while"):-2]
        output += ('    '*tc )+  f'{frontend("while")}'
        output += "{ " + args+ " }\n"
        indents.append("while")
        tc = len(indents)
    elif isIf(line):
        i = line.index("if")
        args = line[i + len("if"):-2]
        output += ('    '*tc )+  f'{frontend("if")}'
        output += "{ " + args+ " }\n"
        indents.append("if")
        tc = len(indents)
    elif "else:" in line :
        output += ('    '*tc )+  "\\Else"
    elif isElif(line):
        i = line.index("elif")
        args = line[i + len("elif"):-2]
        output += ('    '*(tc-1))+  "\\ElsIf"+"{ " + args+ " }\n"
        tc = len(indents)
    else:
        output += stateLine(line)

    #print(output)


print("\\begin{algorithm}\n\tOn input $\\langle args \\rangle$:\n\t\\begin{algorithmic}[1]")
output = output.split("\n")
i=1
for line in output:

    print("\t"*2,line )

print("\t\end{algorithmic}\n\\end{algorithm}")




fle.close()
