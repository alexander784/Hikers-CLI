from database import Hiker, Trip, session

def plan_trip(trip_name, hikers):
    new_trip = Trip(trip_name=trip_name)
    
    session.add(new_trip)

    for hiker_id in hikers:
        hiker = session.query(Hiker).get(hiker_id)
        new_trip.hikers.append(hiker)

    session.commit()
    print(f"Trip {trip_name} planned successfully.")