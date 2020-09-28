import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--show", type=int)

args = parser.parse_args()
print(args.show)
