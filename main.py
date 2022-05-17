import argparse
import math


def checker(type_input):
    """Checks if input of type matches the valid alternatives"""
    alternative = str(type_input)
    if alternative != "annuity" or alternative != "diff":
        raise argparse.ArgumentTypeError('Incorrect parameters')
    return alternative


parser = argparse.ArgumentParser(description='Loan Calculator with different options')

parser.add_argument('--type', required=True, choices=["annuity", "diff"], type=checker)
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('-- interest')

args = parser.parse_args()

calculation = [args.type, args.principal, args.periods, args.interest]
