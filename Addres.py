class AddressBook:
    person_list = []
    def add(self,person):
        
        self.person_list.append(person)
        
    def list_all(self):
        for p in self.person_list:
            print(p.lastname + " " + p.firstname)
    
    def list_all(self, person):
        for p in self.person_list:
            print(p.lastname + " " + p.firstname)
    
    def search(self,k):
        for p in self.person_list:
            k in p.firstname or k in p.lastname:
                print(p.lastname + " " + p.firstname)
            


class Person:
    firstname = ""
    lastname = ""
    email = ""
    tel = ""
    import datetime
    birthday = datetime.date()
    
AddressBook abook = AddressBook()
Person yumoto = Person()
yumoto.firstname = "みちたか"
yumoto.lastname = "ゆもと"
abook.add(yumoto)

Person tokuda = Person()
tokuda.firstname = "あおい"
Person.lastname = "とくだ"
