pin = 1111
count = 0

def account():
    account_balance = 100
    withdrawal = int(input('How much would you like to withdraw?'))
    try:
        remaining_balance = account_balance - withdrawal
        if remaining_balance >= 0:
            print('Your remaining_balance is {}'.format(remaining_balance))
            return remaining_balance
        else:
            return "Insufficient funds"
    except:
        raise Exception

while count < 3:
    enter_pin = int(input("Enter your pin: "));
    if enter_pin == pin:
        print("Correct pin")
        account()
        break
    else:
        print("Incorrect pin. Please try again")
        count += 1


