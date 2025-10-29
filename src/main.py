from prettytable import PrettyTable


class ContactBook:
    def __init__(self):
        self.__contacts = {}

    def __handle_phone_update(self, name, number: str, email: str):
        info = self.__contacts[name]

        while True:
            decision = input('Would you like to replace the information or add to exist?\nR/A? (q to quit) ').strip().lower()
            if decision not in {'q', 'r', 'a'}:
                print('Invalid input!')
                continue
            elif decision == 'q':
                print('Operation canceled.')
                break
            elif decision == 'r':
                info['email'] = {email}
                info['Phone'] = {number}
                break
            elif decision == 'a':
                if info['Phone'] == {None}:
                    info['Phone'] = {number}
                else:
                    info['Phone'].add(number)

                if info['email'] == {None}:
                    info['email'] = {email}
                else:
                    info['email'].add(email)
                break
        print('Contact updated successfully!')

    def add_contact(self, name: str, number: str = None, email: str = None):
        if name not in self.__contacts:
            self.__contacts[name] = {'Phone': {number}, 'email': {email}}
            print('Contact added successfully!')
        else:
            self.__handle_phone_update(name, number, email)

    def get_contact_info(self, name):
        if name in self.__contacts:
            info = self.__contacts[name]
            print(f"- {name}:")
            if info['Phone']:
                print(f"\tPhone: {', '.join([i for i in info['Phone'] if i])}")
            if info['email']:
                print(f"\tEmail: {', '.join([i for i in info['email'] if i])}")
            return
        print(f'Contact not found!')

    def update_contact(self, name: str, number: str = None, email: str = None):
        if name not in self.__contacts:
            while True:
                decision = input(f'Contact not found!\nWould you like to create the contact? y/n? ').strip().lower()
                if decision not in {'y', 'n'}:
                    print('Invalid input!')
                    continue
                elif decision == 'y':
                    return self.add_contact(name, number, email)
                elif decision == 'n':
                    return

        self.__handle_phone_update(name, number, email)

    def delete_contact(self, name):
        try:
            del self.__contacts[name]
            print('Contact deleted successfully!')
        except KeyError:
            print(f"Contact not found!")

    def view_contacts(self):
        table = PrettyTable()
        table.field_names = ['Name', 'Phone', 'Email']
        table.padding_width = 2
        for name, info in self.__contacts.items():
            if info['Phone']:
                phone = ', '.join(info['Phone'])
            else:
                phone = ''
            if info['email']:
                email = ', '.join(info['email'])
            else:
                email = ''
            table.add_row([name, phone, email])
        return table
