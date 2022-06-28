from client import Client
import menu


class ClientManager:
    def __init__(self):
        self.client_list = []

    def add_client(self, client_to_add):
        self.client_list.append(client_to_add)

    def find_client(self, tz):
        for i in self.client_list:
            if tz == i.id_num:
                return i

    def transaction(self, source, destination, amount):
        source_client = self.find_client(source)
        destination_client = self.find_client(destination)
        source_client.remove_money(amount)
        destination_client.add_money(amount)