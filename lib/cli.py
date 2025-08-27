#!/usr/bin/env python3

from helpers import (
    show_main_menu, show_owner_menu, show_pet_menu, show_care_menu,
    create_owner, view_all_owners, find_owner_by_id, delete_owner,
    create_pet, view_all_pets, find_pet_by_id, delete_pet,
    create_care_log, view_all_care_logs, find_care_log_by_id, delete_care_log,
    view_relationships, show_pet_stats, show_care_reminders, search_pets_by_name
)

def owner_management():
    while True:
        choice = show_owner_menu()
        if choice == '1':
            create_owner()
        elif choice == '2':
            view_all_owners()
        elif choice == '3':
            find_owner_by_id()
        elif choice == '4':
            delete_owner()
        elif choice == 'b':
            break
        else:
            print(" Invalid option. Please try again.")

def pet_management():
    while True:
        choice = show_pet_menu()
        if choice == '1':
            create_pet()
        elif choice == '2':
            view_all_pets()
        elif choice == '3':
            find_pet_by_id()
        elif choice == '4':
            delete_pet()
        elif choice == 'b':
            break
        else:
            print("Invalid option. Please try again.")

def care_log_management():
    while True:
        choice = show_care_menu()
        if choice == '1':
            create_care_log()
        elif choice == '2':
            view_all_care_logs()
        elif choice == '3':
            find_care_log_by_id()
        elif choice == '4':
            delete_care_log()
        elif choice == 'b':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    print("WELCOME TO PET CARE SCHEDULER!" )
    print("Manage your pets and track their care activities.")
    
    while True:
        choice = show_main_menu()
        
        if choice == '1':
            owner_management()
        elif choice == '2':
            pet_management()
        elif choice == '3':
            care_log_management()
        elif choice == '4':
            view_relationships()
        elif choice == '5':
            show_pet_stats()
        elif choice == '6':
            show_care_reminders()
        elif choice == '7':
            search_pets_by_name()
        elif choice == 'q':
            print(" Thanks for using Pet Care Scheduler!")
            break
        else:
            print(" Invalid option. Please try again.")

if __name__ == "__main__":
    main()
