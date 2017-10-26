class AddressBook:
    person_list = []
    
    def add(self, person):
        self.person_list.append(person)
    
    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)
    
    def serch(self,keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.lastname + " " + person.firstname)
 
    def import_data(self, file):
        import csv
        import datetime
        
        with open(file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            
            for row in reader:
                p = Person()
                p.lastname = row[0]
                p.firstname = row[1]
                p.mail_address = row[2]
                p.birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                p.tel = row[4]
                
                self.person_list.append(p)
#import datetime
class Person:
    import datetime
    
    firstname = ""
    lastname = ""
    tel = ""
    mail_address = ""
    birthday = datetime.datetime(2000, 1, 1)
    
ab = AddressBook()
ab.import_data("sample100.csv")

print("アドレス帳の人数->" + str(len(ab.person_list)) + "人")

ab.serch("愛")
#ab.add("矢野")
#ab.show_all()
# p = Person()
# p.firstname = "ともき"
# p.lastname = "やの"
# p.tel = "090-1111-2222"

# ab.add(p)

# p2 = Person()
# p2.firstname = "ひろゆき"
# p2.lastname = "はまぐち"
# p2.tel = "090-3333-4444"

# print("---動作確認---")
# ab.add(p2)

# print("アドレス帳の人数->" + str(len(ab.person_list)) + "人")

# print("---一覧表示---")
# ab.show_all()

# print("--検索--")
# ab.serch("ひろゆき")