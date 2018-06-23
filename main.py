import argparse
from classes.bot import Bot

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m",
    "--mode",
    help="please put your choice mode cli or http (default = cli)",
    type=str,
    default='cli'
)
args = parser.parse_args()
Bot(args.mode)
