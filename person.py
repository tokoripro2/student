class Person:
    age = 22
    def greet(self):
        print("こんにちは")
    def self_introduction(self):
        print('自己紹介をしたいと思います。')
        print('私の年齢は、')
        print(self.age)
        print('歳です。')
 
psn = Person()
print(psn.age)
psn.greet()
psn.self_introduction()
