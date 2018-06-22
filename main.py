import argparse
from classes.bot import Bot

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

Bot()
