import math
import sys
import argparse

z = 0  # stop sign for insufficient or wrong arguments
few = 0  # flag to stop double incorrect parameters printing in cases where both type is wrong and nr of args too low or both interest not given and nr of args too low


def monthly_payments():
    total_payment = 0
    for m in range(1, n+1):
        dm = (p / n) + i * (p - (p * (m - 1)) / n)
        print(f'Month {m} : payment is {math.ceil(dm)}')
        total_payment += math.ceil(dm)
    print()
    print("Overpayment =", math.floor(total_payment - p))


def principal_amount():
    x = (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    p = a / x
    p = math.floor(p)
    # print(p, "rounded p check test line remove before final submission")   # test line remove before final submission
    print((f"Your loan principal = {p}!".format(p)))
    print("Overpayment =",(a * n - p))
    return p


def annuity_amount():
    a = p * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))
    a = math.ceil(a)
    print(f"Your annuity payment = {a}!".format(a))
    print("Overpayment =",(a * n - p))
    return a


def payments_nr():
    n = math.log((a / (a - i * p)), (1 + i))
    n = math.ceil(n)
    if n == 1:
        print("It will take 1 month to repay this loan!")
    elif 1 < n < 12:
        print(f"It will take {n} months to repay this loan!".format(n))
    elif n == 12:
        print("It will take 1 year to repay this loan!")
    elif n == 13:
        print("It will take 1 year and 1 month to repay this loan!")
    elif 12 < n < 24:
        x = n - 12
        print(f"It will take 1 year and {x} months to repay this loan!".format(x))
    elif n >= 24:
        if 24 % n == 0:
            yrs = int(n / 12)
            print(f"It will take {yrs} years to repay this loan!".format(yrs))
        else:
            yrs = int(n // 12)
            mts = int(n - yrs * 12)
            print(f"It will take {yrs} years and {mts} months to repay this loan!".format(yrs, mts))
    print("Overpayment =",(a * n - p))
    return n


parser = argparse.ArgumentParser(description="This is a loan calculator")
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

# here go stop conditions and parameter letters assignments

if args.type not in ('diff', 'annuity'):
    print("Incorrect parameters")
    z = 1
    few = 1

while True:
    global i
    if args.interest is None:
        print("Incorrect parameters")
        z = 1
        few = 1
        break
    else:
        usury_rate = float(args.interest)
        i = usury_rate / (12 * 100)  # actual interest rate calculate use i in functions
        if i < 0:
            print("Incorrect parameters")
            z = 1
            few = 1
        break

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    z = 1
    few = 1

while len(sys.argv) < 5:
    if few == 0:
        print("Incorrect parameters")
        z = 1
        break
    else:
        break  # if few == 1 then one of earlier checks has set stop sign already

if args.principal is not None:
    p = int(args.principal)
    if p < 0 and z == 0:
        print("Incorrect parameters")
        z = 1 # to prevent double incorrect parameters printout

if args.periods is not None:
    n = int(args.periods)
    if n < 0 and z == 0:
        print("Incorrect parameters")
        z = 1 # to prevent double incorrect parameters printout

if args.payment is not None:
    global a
    a = int(args.payment)
    if a < 0 and z == 0:
        print("Incorrect parameters")
        z = 1 # to prevent double incorrect parameters printout

# stop conditions and parameter letters assignments


if args.type == "diff" and z != 1:
    monthly_payments()

while args.type == "annuity":
    if z == 1:
        break
    elif args.principal is None:  # no principal size is given - calculate principal
        principal_amount()
        break
    elif args.payment is None:  # no annuity payment size is given - calculate annuity payment
        annuity_amount()
        break
    elif args.periods is None:  # no number of payments is given calculate how long to repay
        payments_nr()
        break
