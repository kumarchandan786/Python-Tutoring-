import argparse
x= argparse.ArgumentParser()
x.add_argument('--nam', type=str, required=True)
##PARSE the argument##
args= x.parse_args()
print("Hello,", args.nam)

