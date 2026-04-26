import json
import os
import re

FILE_NAME = "contacts_data.json"

# ================= LOAD & SAVE =================
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# ================= VALIDATION =================
def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return len(digits) >= 10 and len(digits) <= 15

def validate_email(email):
    if email == "":
        return True
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# ================= FUNCTIONS =================
def add_contact(contacts):
    print("\n--- ADD CONTACT ---")

    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return

    if name in contacts:
        print("⚠️ Contact already exists!")
        return

    phone = input("Enter Phone: ").strip()
    if not validate_phone(phone):
        print("❌ Invalid phone number!")
        return

    email = input("Enter Email (optional): ").strip()
    if not validate_email(email):
        print("❌ Invalid email!")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("✅ Contact Added Successfully!")

def search_contact(contacts):
    print("\n--- SEARCH CONTACT ---")

    term = input("Enter name: ").lower()
    found = False

    for name, info in contacts.items():
        if term in name.lower():
            print("\n------------------")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            found = True

    if not found:
        print("❌ No contact found!")

def update_contact(contacts):
    print("\n--- UPDATE CONTACT ---")

    name = input("Enter name: ").strip()

    if name not in contacts:
        print("❌ Contact not found!")
        return

    phone = input("Enter new phone: ").strip()
    if not validate_phone(phone):
        print("❌ Invalid phone!")
        return

    email = input("Enter new email: ").strip()
    if not validate_email(email):
        print("❌ Invalid email!")
        return

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    save_contacts(contacts)
    print("✅ Contact Updated!")

def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")

    name = input("Enter name: ").strip()

    if name not in contacts:
        print("❌ Contact not found!")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == 'y':
        del contacts[name]
        save_contacts(contacts)
        print("✅ Contact Deleted!")
    else:
        print("Cancelled.")

def display_contacts(contacts):
    print("\n--- ALL CONTACTS ---")

    if not contacts:
        print("No contacts available.")
        return

    for name, info in contacts.items():
        print("\n------------------")
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

# ================= MAIN MENU =================
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            print("💾 Saving & Exiting...")
            save_contacts(contacts)
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()