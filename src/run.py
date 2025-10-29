from main import ContactBook


def run():
    book = ContactBook()

    print('Welcome to contact book application!')

    while True:
        print('\n')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. View a Contact Info')
        print('4. View All Contacts')
        print('5. Delete Contact')
        print('6. Quit')
        print('\n')

        user_choice = input('Please choose an option: ').strip()

        if user_choice not in set('123456'):
            print('Invalid input!')
            continue

        elif user_choice == '6':
            with open('../contact_book.txt', 'w') as f:
                f.write(book.view_contacts().get_string())
            print('Thank you for using this application!')
            print("You can see your contacts in 'contact_book.txt' file.")
            break

        elif user_choice == '1':
            name = input('Enter contact name: ')
            if name.strip() == '':
                print('Name cannot be empty!')
                continue
            number = input('Enter contact phone: ')
            email = input('Enter contact email: ')
            book.add_contact(name, number, email)

        elif user_choice == '2':
            name = input('Enter contact name: ')
            if name.strip() == '':
                print('Name cannot be empty!')
                continue
            number = input('Enter contact phone: ')
            email = input('Enter contact email: ')
            book.update_contact(name, number, email)

        elif user_choice == '3':
            name = input('Enter contact name: ')
            book.get_contact_info(name)

        elif user_choice == '4':
            print(book.view_contacts().get_string())

        elif user_choice == '5':
            name = input('Enter contact name: ')
            book.delete_contact(name)

if __name__ == '__main__':
    run()
