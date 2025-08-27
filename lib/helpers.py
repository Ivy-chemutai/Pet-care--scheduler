from db.models import Owner, Pet, CareLog, session
from datetime import datetime

def validate_pet_age(age_str):
    if not age_str:
        return None
    age = int(age_str)
    if age < 0 or age > 30:
        raise ValueError("Pet age must be between 0-30 years")
    return age

def validate_email(email):
    if '@' not in email or '.' not in email:
        raise ValueError("Please enter a valid email address")
    return email

def show_main_menu():
    print("Pet Care Scheduler")
    print("1. Owner Management")
    print("2. Pet Management") 
    print("3. Care Log Management")
    print("4. View Relationships")
    print("5. Pet Statistics")
    print("6. Care Reminders")
    print("7. Search Pets")
    print("q. Quit")
    return input("Choose an option: ").strip()

def show_owner_menu():
    print("Owner Management")
    print("1. Create Owner")
    print("2. View All Owners")
    print("3. Find Owner by ID")
    print("4. Delete Owner")
    print("b. Back to Main Menu")
    return input("Choose an option: ").strip()

def create_owner():
    try:
        name = input("Enter owner name: ").strip()
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        
        email = input("Enter owner email: ").strip()
        email = validate_email(email)
        
        owner = Owner.create(name, email)
        print(f" Created owner: {owner.name}")
    except Exception as e:
        print(f" Error: {e}")

def view_all_owners():
    owners = Owner.get_all()
    if not owners:
        print("No owners found.")
        return
    print(" All Owners:")
    for owner in owners:
        pets = session.query(Pet).filter(Pet.owner_id == owner.id).all()
        pet_count = len(pets)
        print(f"ID: {owner.id} | {owner.name} | {owner.email} | Pets: {pet_count}")

def find_owner_by_id():
    try:
        owner_id = int(input("Enter owner ID: "))
        owner = Owner.find_by_id(owner_id)
        if owner:
            pets = session.query(Pet).filter(Pet.owner_id == owner.id).all()
            print(f"Found: {owner.name} ({owner.email})")
            if pets:
                print("Their pets:")
                for pet in pets:
                    print(f"  - {pet.name} ({pet.species})")
        else:
            print("Owner not found.")
    except ValueError:
        print(" Please enter a valid ID number.")

def delete_owner():
    try:
        owner_id = int(input("Enter owner ID to delete: "))
        owner = Owner.find_by_id(owner_id)
        if owner:
            owner.delete()
            print(f" Deleted owner: {owner.name}")
        else:
            print("Owner not found.")
    except ValueError:
        print(" Please enter a valid ID number.")

def show_pet_menu():
    print(" Pet Management")
    print("1. Create Pet")
    print("2. View All Pets")
    print("3. Find Pet by ID")
    print("4. Delete Pet")
    print("b. Back to Main Menu")
    return input("Choose an option: ").strip()

def create_pet():
    try:
        owners = Owner.get_all()
        if not owners:
            print(" No owners found. Create an owner first.")
            return
        
        print("Available owners:")
        for owner in owners:
            print(f"ID: {owner.id} | {owner.name}")
        
        name = input("Enter pet name: ").strip()
        if len(name) < 1:
            raise ValueError("Pet name cannot be empty")
        
        species = input("Enter species: ").strip()
        breed = input("Enter breed (optional): ").strip() or None
        age_input = input("Enter age (optional): ").strip()
        age = validate_pet_age(age_input) if age_input else None
        owner_id = int(input("Enter owner ID: "))
        
        pet = Pet.create(name, species, breed, age, owner_id)
        print(f" Created pet: {pet.name}")
    except Exception as e:
        print(f" Error: {e}")

def view_all_pets():
    pets = Pet.get_all()
    if not pets:
        print("No pets found.")
        return
    print(" All Pets:")
    for pet in pets:
        owner = session.query(Owner).filter(Owner.id == pet.owner_id).first()
        owner_name = owner.name if owner else "No owner"
        care_logs = session.query(CareLog).filter(CareLog.pet_id == pet.id).all()
        care_count = len(care_logs)
        print(f"ID: {pet.id} | {pet.name} | {pet.species} | Owner: {owner_name} | Care logs: {care_count}")

def find_pet_by_id():
    try:
        pet_id = int(input("Enter pet ID: "))
        pet = Pet.find_by_id(pet_id)
        if pet:
            owner = session.query(Owner).filter(Owner.id == pet.owner_id).first()
            care_logs = session.query(CareLog).filter(CareLog.pet_id == pet.id).all()
            print(f"Found: {pet.name} ({pet.species}, {pet.breed})")
            print(f"Owner: {owner.name if owner else 'No owner'}")
            if care_logs:
                print("Recent care activities:")
                for log in care_logs[-3:]:
                    print(f"  - {log.activity}: {log.notes}")
        else:
            print("Pet not found.")
    except ValueError:
        print(" Please enter a valid ID number.")

def delete_pet():
    try:
        pet_id = int(input("Enter pet ID to delete: "))
        pet = Pet.find_by_id(pet_id)
        if pet:
            pet.delete()
            print(f" Deleted pet: {pet.name}")
        else:
            print("Pet not found.")
    except ValueError:
        print("Please enter a valid ID number.")

def show_care_menu():
    print(" Care Log Management")
    print("1. Create Care Log")
    print("2. View All Care Logs")
    print("3. Find Care Log by ID")
    print("4. Delete Care Log")
    print("b. Back to Main Menu")
    return input("Choose an option: ").strip()

def create_care_log():
    try:
        pets = Pet.get_all()
        if not pets:
            print(" No pets found. Create a pet first.")
            return
        
        print("Available pets:")
        for pet in pets:
            print(f"ID: {pet.id} | {pet.name} ({pet.species})")
        
        activities = ['feeding', 'walking', 'grooming', 'vet_visit', 'medication', 'play']
        print(f"Available activities: {', '.join(activities)}")
        
        activity = input("Enter activity: ").strip()
        if activity not in activities:
            print(f" Warning: '{activity}' is not a standard activity")
        
        notes = input("Enter notes (optional): ").strip() or None
        pet_id = int(input("Enter pet ID: "))
        
        care_log = CareLog.create(activity, notes, pet_id)
        print(f" Created care log: {care_log.activity}")
    except Exception as e:
        print(f" Error: {e}")

def view_all_care_logs():
    logs = CareLog.get_all()
    if not logs:
        print("No care logs found.")
        return
    print(" All Care Logs:")
    for log in logs:
        pet = session.query(Pet).filter(Pet.id == log.pet_id).first()
        pet_name = pet.name if pet else "Unknown pet"
        print(f"ID: {log.id} | {log.activity} | Pet: {pet_name} | {log.timestamp.strftime('%Y-%m-%d %H:%M')}")

def find_care_log_by_id():
    try:
        log_id = int(input("Enter care log ID: "))
        log = CareLog.find_by_id(log_id)
        if log:
            pet = session.query(Pet).filter(Pet.id == log.pet_id).first()
            print(f"Found: {log.activity} for {pet.name if pet else 'Unknown pet'}")
            print(f"Notes: {log.notes}")
            print(f"Time: {log.timestamp}")
        else:
            print("Care log not found.")
    except ValueError:
        print(" Please enter a valid ID number.")

def delete_care_log():
    try:
        log_id = int(input("Enter care log ID to delete: "))
        log = CareLog.find_by_id(log_id)
        if log:
            log.delete()
            print(f" Deleted care log: {log.activity}")
        else:
            print("Care log not found.")
    except ValueError:
        print("Please enter a valid ID number.")

def view_relationships():
    print(" Relationship Overview")
    owners = Owner.get_all()
    for owner in owners:
        pets = session.query(Pet).filter(Pet.owner_id == owner.id).all()
        print(f" {owner.name}:")
        if pets:
            for pet in pets:
                care_logs = session.query(CareLog).filter(CareLog.pet_id == pet.id).all()
                print(f"   {pet.name} ({pet.species})")
                if care_logs:
                    recent_logs = care_logs[-2:]
                    for log in recent_logs:
                        print(f"     {log.activity} - {log.timestamp.strftime('%m/%d')}")
        else:
            print("  No pets")

def show_pet_stats():
    pets = Pet.get_all()
    if not pets:
        print("No pets to analyze.")
        return
    
    species_count = {}
    total_age = 0
    age_count = 0
    
    for pet in pets:
        species_count[pet.species] = species_count.get(pet.species, 0) + 1
        if pet.age:
            total_age += pet.age
            age_count += 1
    
    print(" Pet Statistics:")
    print(f"Total pets: {len(pets)}")
    print("Species breakdown:")
    for species, count in species_count.items():
        print(f"  {species}: {count}")
    
    if age_count > 0:
        avg_age = total_age / age_count
        print(f"Average pet age: {avg_age:.1f} years")
    
    logs = CareLog.get_all()
    if logs:
        activity_count = {}
        for log in logs:
            activity_count[log.activity] = activity_count.get(log.activity, 0) + 1
        
        print("Most common activities:")
        sorted_activities = sorted(activity_count.items(), key=lambda x: x[1], reverse=True)
        for activity, count in sorted_activities[:3]:
            print(f"  {activity}: {count} times")

def show_care_reminders():
    print(" Care Reminders:")
    pets = Pet.get_all()
    
    if not pets:
        print("No pets to check.")
        return
    
    for pet in pets:
        recent_logs = session.query(CareLog).filter(
            CareLog.pet_id == pet.id
        ).order_by(CareLog.timestamp.desc()).limit(5).all()
        
        if not recent_logs:
            print(f" {pet.name} needs initial care logging")
        else:
            last_feeding = None
            last_walking = None
            
            for log in recent_logs:
                if log.activity == 'feeding' and not last_feeding:
                    last_feeding = log.timestamp
                elif log.activity == 'walking' and not last_walking:
                    last_walking = log.timestamp
            
            if last_feeding:
                hours_since = (datetime.now() - last_feeding).total_seconds() / 3600
                if hours_since > 12:
                    print(f" {pet.name} may need feeding (last fed {hours_since:.0f}h ago)")
            
            if last_walking and pet.species.lower() == 'dog':
                hours_since = (datetime.now() - last_walking).total_seconds() / 3600
                if hours_since > 8:
                    print(f"🚶 {pet.name} may need walking (last walked {hours_since:.0f}h ago)")

def search_pets_by_name():
    search_term = input("Enter pet name to search: ").strip().lower()
    if not search_term:
        print("Please enter a search term.")
        return
    
    pets = Pet.get_all()
    matches = [pet for pet in pets if search_term in pet.name.lower()]
    
    if matches:
        print(f" Found {len(matches)} pet(s):")
        for pet in matches:
            owner = session.query(Owner).filter(Owner.id == pet.owner_id).first()
            care_count = len(session.query(CareLog).filter(CareLog.pet_id == pet.id).all())
            print(f"  {pet.name} ({pet.species}) - Owner: {owner.name if owner else 'Unknown'} - Care logs: {care_count}")
    else:
        print("No pets found with that name.")
