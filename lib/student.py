class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")
# this gets pytest 1-2 to pass: 
# Class Student in student.py says a brief greeting. - assert '' == "Hey there! I...earn stuff.\n"
# Class Student in student.py respectfully tries to get the teacher's attention. .

class ChattyStudent(Student):

    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        for x in range (0,10):
            super().raise_hand()
# this gets pytest 2-4to pass using super: 
# Class ChattyStudent in student.py says a brief greeting, then tries to spoil a TV show. F                                           [ 75%]
# Class ChattyStudent in student.py respectfully tries to get the teacher's attention ten times. F 
