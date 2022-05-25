from math import ceil, log, floor
import argparse

# Instantiate Argparse, define arguments and constraints, get arguments and assign them for further usage.

parser = argparse.ArgumentParser()

parser.add_argument('--type', required=True, choices=['annuity', 'diff'], type=str, help='type of payment')
parser.add_argument('--payment', required=False, type=int, help='amount of monthly payment')
parser.add_argument('--principal', required=False, type=int, help='amount of loan principal')
parser.add_argument('--periods', required=False, type=int, help='number of month to repay loan')
parser.add_argument('--interest', required=True, type=float, help='interest rate for loan')

values = parser.parse_args()

_type = values.type
payment = values.payment
principal = values.principal
periods = values.periods
interest = values.interest

list_of_values = [values.type, values.payment, values.principal, values.periods, values.interest]

# definition of functions

# functions for differentiated payments:

def diff_payments(loan_principal, interest_rate, number_of_payments, current_month_of_repayment):
    p = loan_principal
    i = interest_rate / (12 * 100)
    n = number_of_payments
    m = current_month_of_repayment

    return ceil((p / n) + i * (p - ((p * (m - 1)) / n)))


def check_for_overpayment(loan_principal, payments_for_loan):
    if payments_for_loan > loan_principal:
        return payments_for_loan - loan_principal
    else:
        return False


def differentiated_payments(principal, periods, interest):

    number_of_monthly_payments = 1
    payments_done = []

    while number_of_monthly_payments <= periods:
        print(diff_payments(principal, interest, periods, number_of_monthly_payments))
        payments_done.append(diff_payments(principal, interest, periods, number_of_monthly_payments))
        number_of_monthly_payments += 1

    sum_of_payments = sum(payments_done)

    if check_for_overpayment(principal, sum_of_payments) is not False:
        print(f'Overpayment = {check_for_overpayment(principal, sum_of_payments)}')


#  functions for annuity payments:

# functions for calculating the loan principal

def loan_principal(payment, interest, periods):
    i = interest / (12 * 100)
    return floor(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))


def loan_principal_check_overpay(payment, interest, periods):
    i = interest / (12 * 100)
    principal = loan_principal(payment, interest, periods)
    if principal < (payment * periods):
        return (payment * periods) - principal
    else:
        return False


def calculate_principal_with_overpayment(payment, interest, periods):
    print(f'Your loan principal = {loan_principal(payment, interest, periods)}!')
    if loan_principal_check_overpay(payment, interest, periods):
        print(f'Overpayment = {loan_principal_check_overpay(payment, interest, periods)}')


#  functions for calculating the annuity payment (monthly rate)


def monthly_payment(credit, interest, periods):
    i = interest / (12 * 100)
    return ceil(credit * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))


def monthly_checking_overpay(credit, interest, periods):
    total_payment = monthly_payment(credit, interest, periods) * periods
    if total_payment > credit:
        return total_payment - credit
    else:
        return False


def annuity_payment(credit, interest, periods):
    print(f'Your annuity payment = {monthly_payment(credit, interest, periods)}!')
    if monthly_checking_overpay(credit, interest, periods) is not False:
        print(f'Overpayment = {monthly_checking_overpay(credit, interest, periods)}')

#  function calculating the period needed to repay the loan

def number_of_monthly_payments(credit, payment, interest):
    i = interest / (12 * 100)
    return ceil(log((payment / (payment - i * credit)), 1 + i))


def payment_years_month(credit, payment, interest):
    calculated_period = number_of_monthly_payments(credit, payment, interest)
    years = (calculated_period // 12)
    months = (calculated_period % 12)
    if months == 0:
        return (f'It will take {years} years to repay this loan!' if years > 1
                else f'It will take {years} year to repay this loan!')
    if months != 0:
        return (f'It will take {years} year and {months} months to repay this loan!' if years == 1
                else f'It will take {years} years and {months} to repay this loan')


def number_monthly_with_overpay(credit, payment, interest):
    period = number_of_monthly_payments(credit, payment, interest)
    output_time = payment_years_month(credit, payment, interest)
    loan = period * payment
    # print(loan)
    # print(period)
    print(output_time)
    if loan > credit:
        print(f'Overpayment = {loan - credit}')


#  flow control

if _type not in ('diff', 'annuity'):
    print('Incorrect parameters')

if _type == 'diff' and payment is not None:
    print('Incorrect parameters')

if interest == None:
    print('Incorrect parameters')

if len(list_of_values) < 4:
    print("Incorrect parameters")

if interest is not None:
    if interest < 0:
        print("Incorrect Parameters")

if principal is not None:
    if principal < 0:
        print("Incorrect Parameters")

if periods is not None:
    if periods < 0:
        print("Incorrect Parameters")

if payment is not None:
    if payment < 0:
        print("Incorrect Parameters")

if _type == 'diff':

    differentiated_payments(principal, periods, interest)

elif _type == 'annuity':

    if principal and periods and interest and payment is not True:

        annuity_payment(principal, interest, periods)

    if payment and periods and interest and principal is not True:

       calculate_principal_with_overpayment(payment, interest, periods)

    if principal and payment and interest and periods is not True:

        number_monthly_with_overpay(principal, payment, interest)



