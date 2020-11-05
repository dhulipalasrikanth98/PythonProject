import argparse
import sys
def calc(args):
    if args.o=='add':
        return args.x+args.y
    elif args.o=='sub':
        return args.x-args.y
    elif args.o=='mul':
        return args.x*args.y
    elif args.o=='div':
        return args.x/args.y

if __name__ == "__main__":
    s=argparse.ArgumentParser()
    s.add_argument('--x',default=1.0,type=float,help="Visit srikanth for further help")
    s.add_argument('--y',default=1.0,type=float,help="Visit srikanth for further help")
    s.add_argument('--o',default="add",help="Visit srikanth for further help")
    args=s.parse_args()
    sys.stdout.write(str(calc(args)))