import menu


class Client:
    def __init__(self, first_name, last_name, id_num, bank_balance, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id_num = id_num
        self.bank_balance = bank_balance
        self.age = age

    def display_details(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Id number: " + str(self.id_num))
        print("Bank balance: " + str(self.bank_balance))
        print("Age: " + str(self.age))

    def add_money(self, sum_to_add):
        self.bank_balance += sum_to_add

    def remove_money(self, sum_to_remove):
        self.bank_balance -= sum_to_remove

    def edit_client(self):
        menu.edit_client()
        what_to_edit = input('choose an option')
        while what_to_edit != '6':
            if what_to_edit == "1":
                self.first_name = input('What is the new first name of the client? ')
            elif what_to_edit == "2":
                self.last_name = input('What is the new last name of the client? ')
            elif what_to_edit == "3":
                self.id_num = input('What is the new ID number of the client? ')
            elif what_to_edit == "4":
                self.age = input('What is the new age of the client? ')
            elif what_to_edit == "5":
                self.bank_balance = input('What is the new bank balance of the client? ')
            menu.edit_client()
            what_to_edit = input('witch detail do you want to edit:')
