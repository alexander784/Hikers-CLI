from database import Equipment, session

def create_equipment(name, condition):
    new_equipment = Equipment(name=name, condition=condition)
    session.add(new_equipment)
    session.commit()
    print(f"Equipment {name} added successfully.")