class students:

    def __init__(self,studentid,studentname):
        self.__studentid=studentid
        self.__studentname=studentname

    # def setid(self,studentid):
    #     self.__studentid=studentid

    # def setname(self,studentname):
    #     self.__studentname=studentname

    def displaycontent(self):
        print("the name of the student is: ", self.__studentname)
        print("the id of this student is: ", self.__studentid)

#inserting and outputting values in array using class of students
# mydata=[]
# mydata.append(students(1001, "mustansir"))
# print(mydata[0].studentid)

class subjects(students):

    
    def __init__(self,studentid,studentname,subject1,subject2,subject3):
        super().__init__(studentid,studentname)
        self.__subject1=subject1
        self.__subject2=subject2
        self.__subject3=subject3
        

    # def setsubjects(self,s1,s2,s3):
    #     self.__subject1=s1
    #     self.__subject2=s2
    #     self.__subject3=s3

    def displaycontent(self):

        super().displaycontent()
        print(self.__subject1)
        print(self.__subject2)
        print(self.__subject3)


sub=subjects(1001,"mustansir","math","physics","cs")
sub.displaycontent()