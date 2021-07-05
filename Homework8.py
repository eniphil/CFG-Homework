account_balance = 100

def account(account_balance):


    withdrawal = int(input('How much would you like to withdraw?'))

    remaining_balance = account_balance - withdrawal

    if remaining_balance >= 0:

        print('Your remaining_balance is {}'.format(remaining_balance))

    else:
        raise Exception

pin = 1111

count = 0

while True:
    enter_pin = int(input("Enter your pin: "));
    if (enter_pin) == pin:
        print("Correct pin")
        print("Access granted")

        try:
            with open('pin.txt', 'a+') as new_text:
                new_text.write('Members pin is {}'.format(enter_pin))
                print('You have now been registered. Please keep your pin safe\n')
        except:
            print('Please try again')
        account(account_balance)

        break
    print("Incorrect pin. Please try again")
    count += 1
    if count == 3:
        print("Incorrect pin entered three times, system locked")
        break