class ContactManager:

    def __init__(self, contacts:dict[str, list[str]]):
        self.contacts = contacts

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            raise ValueError("Errore: il contatto esiste già.")
        self.contacts[name] = phone_numbers
        return {name:phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        elif phone_number in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono esiste già.") 
        for key, value in self.contacts.items():
            if key == contact_name:
                self.contacts[contact_name].append(phone_number)

        return {contact_name:phone_number}
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.") 
        elif phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        for key, value in self.contacts.items():
            if key == contact_name:
                self.contacts[contact_name].remove(phone_number)
        
        return {contact_name:self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.") 
        elif old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        for key, value in self.contacts.items():
            if key == contact_name:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)

        return {contact_name:self.contacts[contact_name]}
    
    def list_contacts(self): 
        return self.contacts.keys()
    
    def list_phone_numbers(self, contact_name: str): 
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str):
        contact_number:list = []
        
        for key, value in self.contacts.items():
            if phone_number in value:
                contact_number.append(key)
            else:
                continue

        if len(contact_number) > 0:
            return contact_number
        else:
            raise ValueError("Nessun contatto trovato con questo numero di telefono.")

c:ContactManager = ContactManager({"a":["1", "2", "3"]})
c.create_contact("b", ["4"])
c.add_phone_number("b", "5")
c.add_phone_number("b", "6")
c.remove_phone_number("b", "6")
c.update_phone_number("b", "4", "7")
print(c.list_contacts())
print(c.list_phone_numbers("b"))
print(c.search_contact_by_phone_number("7"))