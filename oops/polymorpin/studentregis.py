import uuid


class Student:
    def registration(self):
        self.id = uuid.uuid4().hex[:4]
        self.name = "Abhinav"
        self.pincode = uuid.uuid4().hex[:6]
        self.address = "Rohtak"



class View:
        def Display(self,student):
            print("ID: ",student.id)
            print("Name: ",student.name)
            print("Address: ", student.address)
            print("Pincode: ", student.pincode)

ob1 = Student()
ob1.registration()

ob2 = View()
ob2.Display(ob1)