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
