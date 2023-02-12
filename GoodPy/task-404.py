oldfile_array=["","","","","","","","","",""]
new_array=["","","","","","","","","",""]


def read_highscores():
    oldfile = open("Highscore.txt","r")
    for count in range(0,10):
        oldfile_array[count]=oldfile.readline()[:-1]
        oldfile_array[count]+= " " + oldfile.readline()[:-1]
    oldfile.close()

def output_highscores():
    global oldfile_array
    for count in range(0,10):
        print(oldfile_array[count])

name= str(input("enter the name: "))
score= str(input("enter the score: "))
while int(score) < 1 or int(score) > 11000:
    score= str(input("enter the score: "))


def update_list(name,score):
    global oldfile_array,new_array
    new_array=oldfile_array
    index=9

    while int(score) > int(new_array[index][4:]) and index!=-1:
        index-=1
            
    if index!=9:
        index+=1
        temp= new_array[index]
        new_array[index]=name + " " + score
        for i in range(index,9):
            temp2=temp
            temp=new_array[i+1]
            new_array[i+1]=temp2

    return new_array

def write_file():
    global new_array
    newfile=open("newfile.txt","w")
    for count in range(0,10):
        newfile.write(new_array[count] + "\n")
    newfile.close()

read_highscores()
output_highscores()
print(update_list(name,score))
write_file()
