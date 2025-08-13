contact = {} # empty dic to store key value

#add 
contact_name = input("enter your contact name").strip() #user to enter his detail
phone =  input("enter your number").strip()
if contact_name in contact:
    print(f"{contact_name} is found in contact list")
else:
    contact[contact_name] = phone 
    print("succefully added ")

    # delete 
contact_delete = input("enter contact u want to delete").strip()
if contact_delete in contact: 
    del contact[contact_delete]
    print(f"{contact_delete} is succesfully deleted ")
else:
    print("contact not found")
    
    contact_access = input("contact u want to access")
    if contact_access in contact:
        print(contact[contact_access])
    else: 
        print(f"{contact_acess} was not found ")
    

