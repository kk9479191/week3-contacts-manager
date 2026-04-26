Contact Management System

Project Description

A Contact Management System built using Python that allows users to store, manage, and organize contact details such as names, phone numbers, and emails.
The system supports CRUD operations (Add, Search, Update, Delete) and stores data using a JSON file.

Project Overview and Objectives

This project aims to:

* Manage contacts efficiently using dictionaries
* Perform CRUD operations
* Implement search with partial matching
* Store data permanently using JSON
* Provide a user-friendly interface

Features

* Add new contacts
* Search contacts (partial match supported)
* Update existing contacts
* Delete contacts with confirmation
* View all contacts
* Automatic save/load using JSON
* Phone and email validation
* Menu-driven interface

Setup and Installation

```bash
# Navigate to project folder
cd week3-contact-manager

# Run the program
python contacts_manager.py
```

Code Structure

The project is modular and uses functions:

* `load_contacts()` → Load data from file
* `save_contacts()` → Save data to file
* `add_contact()` → Add new contact
* `search_contact()` → Search contact
* `update_contact()` → Update contact
* `delete_contact()` → Delete contact
* `display_contacts()` → Show all contacts
* `main()` → Menu controller

Data Structure

python
contacts = {
    "Karan": {
        "phone": "8984596865",
        "email": ""
    },
    "Kajal": {
        "phone": "9555485668",
        "email": ""
    }
}
```

Sample Output

```
--- ALL CONTACTS ---

Name: Karan
Phone: 8984596865
Email: 

Name: Kajal
Phone: 9555485668
Email: 
```

---

Technical Details

* Language: Python
* Data Structure: Dictionary
* Storage: JSON file
* Modules Used: json, os, re

---

Screenshots
output.png


Testing

* Tested with real data (Karan & Kajal)
* Verified all CRUD operations
* Checked file save/load functionality
* Tested invalid inputs

---
Project Structure

```
week3-contact-manager/
│── contacts_manager.py
│── contacts_data.json
│── README.md
```

Conclusion

This project demonstrates the use of Python fundamentals such as functions, dictionaries, file handling, and validation to build a real-world application.

---
# week3-contacts-manager
