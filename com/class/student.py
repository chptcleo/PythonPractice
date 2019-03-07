class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print("%s gets %s" %(self.__name, self.__score))

        
if __name__ == "__main__":
    kobe = Student("kobe", 98)
    james = Student("james", 97)
    
    kobe.print_score()
    kobe.age = 41
    print(kobe.age)
    print(james.age)
