import argparse
import os

print("In script.py")
print("As a data scientist, this is where I use my training code.")

parser = argparse.ArgumentParser("train")

parser.add_argument("--pipeline_arg", type=str, help="pipeline_arg")
# parser.add_argument("--output_train", type=str, help="output_train directory")

args = parser.parse_args()

print("Argument 1: %s" % args.pipeline_arg)
# print("Argument 2: %s" % args.output_train)

# if not (args.output_train is None):
#     os.makedirs(args.output_train, exist_ok=True)
#     print("%s created" % args.output_train)