from math import ceil, log

principal = 500000
interest = 7.8
periods = 8

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


differentiated_payments(principal, periods, interest)

#  functions for annuity payments:


def monthly_payment(credit, interest, periods):
    return ceil(credit * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))


def number_of_monthly_payments(credit, payment, interest):
    return ceil(log((payment / (payment - interest * credit)), 1 + interest))


def loan_principal(payment, i, periods):
    return payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))


def nominal_interest_rate(interest):
    return interest / (12 * 100)


# flow control for annuity payments

# if user_input == "a":
#     loan_principal = float(input('Enter the loan principal: '))
#     number_of_periods = int(input('Enter the number of periods: '))
#     loan_interest = float(input('Enter the loan interest: '))
#
#     i = nominal_interest_rate(loan_interest)
#     pay_per_month = monthly_payment(loan_principal, i, number_of_periods)
#     print(f'Your monthly payment = {pay_per_month}!')
#
# if user_input == "p":
#     annuity_payment = float(input('Enter the annuity payment: '))
#     number_of_periods = int(input('Enter the number of periods: '))
#     loan_interest = float(input('Enter the loan interest: '))
#
#     i = nominal_interest_rate(loan_interest)
#     loan = round(loan_principal(annuity_payment, i, number_of_periods))
#     print(f'Your loan principal = {loan}!')
#
# if user_input == "n":
#     loan_principal = float(input('Enter the loan principal: '))
#     monthly_payment = float(input('Enter the monthly payment: '))
#     loan_interest = float(input('Enter the loan interest: '))
#
#     i = nominal_interest_rate(loan_interest)
#
#     calculated_period = number_of_monthly_payments(loan_principal, monthly_payment, i)
#
#     years = (calculated_period // 12)
#     months = (calculated_period % 12)
#
#     print(f'It will take {years} years and {months} months to repay this loan!')