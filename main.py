import menu
import client_manager
import client

client_manager = client_manager.ClientManager()

menu.display_menu()

ask = input('Choose an option')
while ask != "6":
    if ask == "1":
        new_client = menu.create_new_account()
        client_manager.add_client(new_client)
        print('Client added successfully !')
    elif ask == "2":
        tz = input('input the id number of the client: ')
        client2 = client_manager.find_client(tz)
        client2.display_details()
    elif ask == "3":
        tz = input('input the id number of the client: ')
        client1 = client_manager.find_client(tz)
        client1.edit_client()
        client1.display_details()
    elif ask == "4":
        source = input('Enter the ID of the transaction source: ')
        destination = input('Enter the ID of the transaction destination:  ')
        amount = int(input("Enter the amount of the transaction: "))
        client_manager.transaction(source, destination, amount)
    elif ask == "5":
        print(repr(client_manager.client_list))
    menu.display_menu()
    ask = input('Choose an option')

print('bye')
