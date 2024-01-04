from database import Hiker, session


def create_hiker(name, contact_info, emergency_contact):
    new_hiker = Hiker(name=name, contact_info=contact_info, emergency_contact=emergency_contact)
    session.add(new_hiker)
    session.commit()
    print(f"Hiker {name} added successfully.")