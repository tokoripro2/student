class AddressBook:
    person_list = []
    def add(self,person):
        
        self.person_list.append(person)
        
    def list_all(self):
        for p in self.person_list:
            print(p.lastname + " " + p.firstname)
            


class Person:
    firstname = ""
    lastname = ""
    email = ""
    tel = ""
    import datetime
    birthday = datetime.date()