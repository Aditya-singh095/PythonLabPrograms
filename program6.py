# Dynamic Phonebook and Contact Directory Manager

phonebook = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    phonebook[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\n--- Contacts ---")

    for name, details in phonebook.items():
        print(f"Name : {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print()


def search_contact():
    keyword = input("Enter name to search: ").lower()

    # List comprehension for dynamic lookup
    matches = [
        name for name in phonebook.keys()
        if keyword in name.lower()
    ]

    if matches:
        print("\nMatching contacts:")
        for name in matches:
            print(name, "->", phonebook[name])
    else:
        print("No contacts found.")


def update_contact():
    name = input("Enter name to update: ")

    if name not in phonebook:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")

    phonebook[name]["phone"] = phone
    phonebook[name]["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def show_phone_numbers():
    print("\n--- Phone Numbers ---")

    # Using dictionary values()
    for details in phonebook.values():
        print(details["phone"])


def main():
    while True:
        print("\n===== Phonebook =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Show Phone Numbers")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            show_phone_numbers()

        elif choice == "7":
            print("Exiting phonebook...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
