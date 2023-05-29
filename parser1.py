import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--Number1",help="Enter Your first Number")
parser.add_argument("--Number2",help="Enter your 2nd Number")
parser.add_argument("--operation", help="Give your option: either add, or sub, or multiply")

args=parser.parse_args()
####
n1=int(args.Number1)
n2=int(args.Number2)
result=None
if args.operation == "add":
    result= n1 + n2
elif args.operation == "sub":
    result= n1 - n2
elif args.operation == "multiply":
    result = n1 * n2
print(result)