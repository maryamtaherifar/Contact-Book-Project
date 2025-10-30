from prettytable import PrettyTable


class ContactBook:
    def __init__(self):
        self.__contacts = {}

    def __handle_phone_update(self, name: str, number: str, email: str):
        """ Handles the process of updating an existing contact's phone number or email.

        Asks the user whether they want to replace the existing contact information
        or add the new details alongside the old ones.

        :param name: The name of the contact to update.
        :param number: The new phone number to add or replace.
        :param email: The new email address to add or replace.
        """
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
        """Add a new contact to the contact book.

        If the contact already exists, the user is prompted to replace or add information.

        :param name: The name of the contact.
        :param number: The phone number of the contact. Defaults to None.
        :param email: The email address of the contact. Defaults to None.
        """
        if name not in self.__contacts:
            self.__contacts[name] = {'Phone': {number}, 'email': {email}}
            print('Contact added successfully!')
        else:
            self.__handle_phone_update(name, number, email)

    def get_contact_info(self, name):
        """Display detailed information for a specific contact.

        :param name: The name of the contact to retrieve.
        """
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
        """ Update the contact information of an existing contact.

        If the contact does not exist, prompts the user to create it.

        :param name: The name of the contact to update.
        :param number: The new phone number. Defaults to None.
        :param email: The new email address. Defaults to None.
        """
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
        """Delete a contact from the contact book.

        :param name: The name of the contact to delete.
        """
        try:
            del self.__contacts[name]
            print('Contact deleted successfully!')
        except KeyError:
            print(f"Contact not found!")

    def view_contacts(self):
        """ Display all contacts in a formatted table.

        :return: A PrettyTable object containing all contacts, phone numbers, and emails.
        """
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
