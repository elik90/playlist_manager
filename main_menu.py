import sys
import sql_connector

''' 
This script accepts new entries for the playlist aggregation program.
New user data is entered into SQL using sql_connector.py scripts
'''


class User:

    def __init__(self):
        self.menu = '0'
        self.submit = False
        self.user_input = '0'
        self.first_name = None
        self.last_name = None
        self.email = None
        self.address = None
        self.phone = None
        self. dob = None
    
    def update_user_menu(self, menu):
        self.menu = menu
        pass

    def update_user_input(self, user_input):
        self.user_input = user_input
        pass

    def update_user_first_name(self, user_input):
        if all(name.isalpha() for name in user_input.split()):
            self.first_name = user_input.title()
        else:
            print("First name must contain only letters")
            
    def update_user_last_name(self, user_input):
        if all(name.isalpha() for name in user_input.split()):
            self.last_name = user_input.title()
        else:
            print("Last name must contain only letters")
    
    def update_user_email(self, user_input):
        self.email = user_input

    def update_user_address(self, user_input):
        self.address = user_input
    
    def update_user_phone(self, user_input):
        # assert 10 digits
        self.phone = user_input
    
    def update_user_dob(self, user_input):
        self.dob = user_input

    def reset_all_fields(self):
        self.menu = '0'
        self.submit = False
        self.user_input = '0'
        self.first_name = None
        self.last_name = None
        self.email = None
        self.address = None
        self.phone = None
        self. dob = None


def verify_name_input(self, user_input):
    name_elements = user_input.split()
    pass


def prompt_main(user):
    # list options for entering data
    print("Welcome to playlist_aggregator main menu:")
    print("=== Main Menu Options ===")
    print("""
        1. Add a new record 
        2. View/update existing records
        3. Delete a record
        q. Quit
        """)
    user_option = input("Enter a valid option: ")

    if user_option in ['1', '2', '3']:
        user.update_user_menu(user_option)
    elif user_option == 'q':
        user.update_user_menu('0')
    else:
        print("Invalid input")


def prompt_add_record(user):
    print("=== Add Record Menu Options ===")
    print("""
        1. Add a user 
        2. Add a service
        q. Quit
        """)   
    user_option = input("Enter a valid option: ")

    if user_option == '1':
        user.update_user_menu('11')
    elif user_option == '2':
        user.update_user_menu('12')       
    elif user_option == 'q':
        user.update_user_menu('0')
    else:
        print("Invalid input")


def prompt_add_user(connection, user):
    print("=== Current User Values ===")
    print(f"First Name: {user.first_name}")
    print(f"Last Name: {user.last_name}")
    print(f"email: {user.email}")
    print(f"address: {user.address}")
    print(f"phone: {user.phone}")
    print(f"DOB: {user.dob}")
    print("=== Add User Menu Options ===")
    print("""
        1. Edit first name (required)
        2. Edit last name (required)
        3. Edit email
        4. Edit address
        5. Edit phone
        6. Edit DOB
        7. Submit
        8. Clear all 
    """)
    user_option = input("Enter a valid option: ")

    if user_option == '1':
        user_input = input("Enter First Name: ")
        user.update_user_first_name(user_input)

    elif user_option == '2':
        user_input = input("Enter Last Name: ")
        user.update_user_last_name(user_input)

    elif user_option == '3':
        user_input = input("Enter email address: ")
        user.update_user_email(user_input)

    elif user_option == '4':
        user_input = input("Enter address: ")
        user.update_user_address(user_input)

    elif user_option == '5':
        user_input = input("Enter 10-digit phone number (xxx-xxx-xxxx): ")
        user.update_user_phone(user_input)

    elif user_option == '6':
        user_input = input("Enter DOB MM/DD/YY: ")
        user.update_user_dob(user_input)

    elif user_option == '7':
        user_input = input("Submit user records to SQL? Yes(y), No(n): ")
        if user_input == 'y':
            add_user_query = """
            INSERT INTO
            `users` (`first_name`, `last_name`, `email`, `address`, `phone`, `dob`)
            VAlUES
            ( %s, %s, %s, %s, %s, %s)
            """
            values = (user.first_name, user.last_name, user.email, user.address, user.phone, user.dob)
            sql_connector.execute_query(connection, add_user_query, values)
        elif user_input == 'n':
            pass

    elif user_option == '8':
        user_input = input("Reset all fields? Yes(y), No(n): ")
        if user_input == 'y':
            user.reset_all_fields()
            pass
        elif user_input == 'n': 
            pass


if __name__ == "__main__":

    # Initialize user object
    user1 = User()
    sql_connector.check_database_playlist_aggregator_connection()

    connection = sql_connector.create_connection("localhost",
                                                 "root",
                                                 sql_connector.plain_text_encrypted_password,
                                                 "playlist_aggregator")

    while True:
        if user1.menu == '0':
            prompt_main(user1)

        elif user1.menu == '1':
            prompt_add_record(user1)

        elif user1.menu == '2':
            # prompt_view_update_record(user1)
            print("does not exist")
            pass

        elif user1.menu == '3':
            # prompt_delete_record(user1)
            print("does not exist")
            pass

        elif user1.menu == '11':
            prompt_add_user(connection, user1)