class Student:
    all_name = []
    iq = 100 # Class attribute - global
    def __init__(self, name, mark: float, subject = 0, grade = 0): # Default subject value = 0
        
        print(f"Student's name is {name}") 
        self.name = name
        self.mark = mark
        self.subject = subject
        self.__grade = grade

        
        
        assert mark > 0, f"Mark {mark} is less than 0"
        assert subject >= 0, f"Subject {subject} is less than 0"
        Student.all_name.append(self.name)
    
    @property
    def grade(self):
        return self.__grade
         
    
    def total_mark(self):
        return self.mark*self.subject
    def name_call(self):
        print(f"Student's name is {self.name}") 
    def iq_compare(self):
        return Student.iq*self.mark
    def __repr__(self): # It will run each time will run the instance
        return f'Name {self.name}'
    
    def is_good(num):
        if(num >= 7):
            return True
        else:
            return False
            