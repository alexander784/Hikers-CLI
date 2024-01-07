from create_hiker import create_hiker
from create_equipment import create_equipment
from plan_trip import plan_trip
from database import initialize_database
from Create_account import create_account

def main():
    initialize_database()

    while True:
        print("\nHikers Management System\n")
        print("1. Create Hiker Profile")
        print("2. Create Equipment Entry")
        print("3. Plan Trip")
        print("4. Create Account")
        print("5. Exit")

        choice = input("Enter your choice (1-4): ")


        if choice == '1':
            name = input("Enter hiker's name: ")
            contact_info = input("Enter contact information: ")
            emergency_contact = input("Enter emergency contact: ")
            create_hiker(name, contact_info, emergency_contact)

        elif choice == '2':
            name = input("Enter equipment name: ")
            condition = input("Enter equipment condition: ")
            create_equipment(name, condition)

        elif choice == '3':
            trip_name = input("Enter trip name: ")
            hikers = [int(id) for id in input("Enter hiker IDs (comma-separated): ").split(',')]
            plan_trip(trip_name, hikers)

            # Add Create Account
        elif choice == '4':
            username = input("Enter username: ")
            password = input("Enter password: ")
            create_account(username, password)
            print("Account created successfully.")
            

        elif choice == '5':
            print("Exiting Hikers Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
