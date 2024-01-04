from create_hiker import create_hiker
from create_equipment import create_equipment
from plan_trip import plan_trip
from database import initialize_database

def main():
    initialize_database()

    while True:
        print("\nHikers Management System\n")
        print("1. Create Hiker Profile")
        print("2. Create Equipment Entry")
        print("3. Plan Trip")
        print("4. Exit")

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

        elif choice == '4':
            print("Exiting Hikers Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
