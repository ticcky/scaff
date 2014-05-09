import argparse

parser = argparse.ArgumentParser()
parser.add_argument("param1")
parser.add_argument("--arg1")
parser.add_argument("--bool_arg1", action='store_true', default=False)
args = parser.parse_args()
