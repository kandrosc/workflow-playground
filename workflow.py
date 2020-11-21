import sys

def check_even(argv):
    try: num = int(argv[1])
    except (IndexError, ValueError) as e: return 1
    if num%2==1: return 1
    return 0

if __name__=="__main__": sys.exit(check_even(sys.argv))
