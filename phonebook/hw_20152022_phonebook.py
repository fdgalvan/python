


phonebook = {} #global variable





def searchName():
    print(f'''
Search Contacts
======================
''')
    name = input('Search for a name >> ')
    
    if name in phonebook:
        print(f'{name} {phonebook[name]}')
    else:
        print('contact not found')

def addContact():
    name = input('Enter a name >> ')
    phoneNumber = input('Enter a phone number >> ')
    
    phonebook[name] = phoneNumber

def deleteContact():
    print(f'''
Delete Contact
====================
''')
    name = input('Insert a name to delete >> ')
    
    if name in phonebook:
        del phonebook[name]
    else:
        print('No contact to delete')

def listAllEntries():
    print(f'''
Phonebook Contacts
====================          
''')
    
    for name, phonenumber in phonebook.items():
        print(f'{name}\t\t{phonenumber}')


def menu():
    selection = int(input("""
Electronic Phonebook
====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Exit                     

"""))
    return selection


endProgram = False #does not end the program

while not endProgram:
    
    selection = menu()
    
    if selection == 1:
        searchName()
    elif selection == 2:
        addContact()
    elif selection == 3: 
        deleteContact()
    elif selection == 4:
        listAllEntries()
    elif selection == 5:
        endProgram = True #means user has selected to end the program