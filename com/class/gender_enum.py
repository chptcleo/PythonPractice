
class Gender(object):
    Male = 0
    Female = 1

    
class Student(object):
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


if __name__ == "__main__":
    bart = Student("bart", Gender.Male)
    if bart.gender == Gender.Male:
        print("pass")
    else:
        print("fail")
