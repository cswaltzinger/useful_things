from sys import argv as args
import subprocess
import os 
import sys
import json
import shlex
from prnt import * 
data = None 
tests = None 
if len(args) != 3:
    print(f"USAGE: python3 grade.py [GRADE_FILE] [GRADE_DIRECTORY]")
    exit(1)

THE_CWD = args[2]
try:
    f = open(args[1])
    data = json.load(f)
    f.close()
    tests = data["tests"]
except Exception as e :
    print(e)
    exit(1)


totalPoints = 0
givenPoints = 0 
SHOULD_EXIT=False 
#clean = "make clean"
passed_tests = []
failed_tests = []
cwd = os.getcwd()
THE_CWD=f"{cwd}/{THE_CWD}"

def clean():
    run = "make clean"
    run = "clear"
    try:
        result = subprocess.run(
            run, 
            #shlex.split(run),
            executable = '/bin/bash',
            env=os.environ.copy(),
            cwd=THE_CWD,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return result.returncode, result.stdout
    except UnicodeDecodeError:
        return 255, "Couldn't decode, non-text output detected!"
SHOULD_SPLIT=False

def setup(test):
    run = test["setup"]
    timeout = test["timeout"]
    if run == "":
        return 0, "nothing to run ", 0 
    try:
        
        result = subprocess.run(
            run if False else shlex.split(run),
            executable = '/bin/bash',
            env=os.environ.copy(),
            cwd=THE_CWD,
            shell=True,
            stdout=subprocess.PIPE,
            #stderr=subprocess.STDOUT,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except UnicodeDecodeError:
        return 255, "Couldn't decode, non-text output detected!", 255

def run(test):
    run = test["run"]
    input = test["input"]
    timeout = test["timeout"]
    #print(timeout)
    if run == "":
        return 0, "nothing to run "
    try:
        result = subprocess.run(
            run if SHOULD_SPLIT else shlex.split(run),
            executable = '/bin/bash',
            env=os.environ.copy(),
            cwd=THE_CWD,
            input=input,
            shell=True,
            stdout=subprocess.PIPE,
            #stderr=subprocess.STDOUT,
            stderr=subprocess.PIPE,
            timeout=timeout,
            universal_newlines=True
        )
        
        return result.returncode, result.stdout, result.stderr
    except UnicodeDecodeError:
        return 255, "Couldn't decode, non-text output detected!",255
    except subprocess.TimeoutExpired:
        return 255, "Program timed out ",255

def pout(name,code,expout,output, eerr,running ="",points=0):
    #sep = '_' *  int(os.get_terminal_size()[0] )
    def isin(eout,out,eerr):
        #print(f"{eout},{out},{eerr}|")
        if eout == "":
            return True
        #print(f"[{out}] ==> [{eout}] [{eerr}]")
        for item in eout:
            #print("\t",item)
            if not item in out:
                if not (eerr and  item in eerr):
                    return False 
        return True
    
    print("--------------------------------")

    
    if code == 0 and isin(expout,output,eerr):
        plgreen("SUCCESS",f'[{name}] ({code}) : [{running}]')
        return True
    else :
        plred("FAILURE",f'[{name}] ({code}) : [{running}]')
        lines = output.split("\n")
        for line in lines:
            print(f'\t{line}',file=sys.stderr)
        return False




totalPoints=0
pointsGained =0
i = 0 
potentialPoints =0 
for test in tests: 
    #clean()
    output = test["output"]
    comparison = test["comparison"]
    points = test["points"]
    if points == None:
        points = 0
    
    name = test["name"]
    if "Answers to Problem" in name in test["run"]:
        plblue("SKIPPING/MANUALLY GRADING ",f'[{name}]]')
        potentialPoints += points
        continue
    totalPoints += points 
    
    code, pgoutput, err = setup(test )

    if code != 0:
        plred("SETUP FAILURE",f'[{name}] [{test["setup"]}] -> [{test["run"]}] ')
        print(err)
        continue
    
    #print(f"runnning {i}")
    code, pgoutput, pgerr = run(test)
    
    # print("out   ",pgoutput)
    # print("err   ",pgerr)
    # print("code",code)
    if pout(name,code,output,pgoutput,pgerr,test["run"]):
        pointsGained+=points
    i+=1

print(f"{pointsGained}/{totalPoints} ==> {int((pointsGained/(totalPoints*1.0))*100)}%")
