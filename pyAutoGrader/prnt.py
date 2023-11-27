import sys
class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def plred(str,str2=""):
    print(f"{col.FAIL}{str}{col.ENDC}{str2}",file=sys.stderr)
def plgreen(str,str2=""):
    print(f"{col.OKGREEN}{str}{col.ENDC}{str2}")

def plblue(str,str2=""):
    print(f"{col.OKBLUE}{str}{col.ENDC}{str2}")

