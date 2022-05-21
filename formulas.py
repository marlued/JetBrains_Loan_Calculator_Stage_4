from math import ceil, floor
import argparse

# Instantiate Argparse, define arguments and constraints, get arguments and assign them for further usage.

parser = argparse.ArgumentParser()

parser.add_argument('--type', required=True, choices=['annuity', 'diff'], type=str, help='type of payment')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

values = parser.parse_args()

_type = values.type
payment = values.payment
principal = values.principal
periods = values.periods
interest = values.interest

print(_type, payment, principal, periods, interest)

# flow control and error handling








