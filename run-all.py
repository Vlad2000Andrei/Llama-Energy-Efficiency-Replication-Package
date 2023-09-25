from sys import argv
from os import system, path
from time import time

if not len(argv) >= 3:
    print("Incorrect number of arguments")
    exit(-1)

promptfile = argv[1]
modeldir = argv[2]

with open(promptfile) as file:
    lines = [line for line in file]

total = len(lines)
current = 1

for line in lines:
    [language, prompt] = line.split(maxsplit=1)
    print(f"########### Generating Answer {current}/{total}.")
    cmd = f"./run-instruction.sh {modeldir} {language.strip()} \"{prompt.strip()}\""

    if (argv[3] == "-f"):
        if not path.isdir("./answers"):
            system("mkdir ./answers/")
        filename = f"./answers/{int(time())}-{language}-prompt-{current}.md"
        cmd = f"touch {filename}; {cmd} > {filename}"

    print(f"Executing: '{cmd}'")
    system(cmd)
    current += 1