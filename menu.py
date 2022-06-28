import client


def display_menu():
    print("\n\n----------JOSEPH'S BANK----------")
    print('1. Create new account')
    print('2. View client details')
    print('3. Edit client details')
    print('4. For transaction')
    print('5. View costumer list')
    print('6. Exit')


def create_new_account():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    id_num = input('ID number: ')
    bank_balance = int(input('Bank balance: '))
    age = input('Age: ')
    new_client = client.Client(first_name, last_name, id_num, bank_balance, age)
    return new_client


def edit_client():
    print("\n\nwitch detail do you want to edit:")
    print('1. First name')
    print('2. Last name')
    print('3. ID number')
    print('4. Age')
    print('5. Bank balance')
    print('6. Exit')




