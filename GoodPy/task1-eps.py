def column_num(my_string):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total=0

    for count in range(0,len(my_string)):
        index=0
        while my_string[count] != letters[index] and index <= 26:
            index+=1
        if my_string[count] == letters[index]:
            total=(total*26)+index+1
    print(total)

ans="Y"
while ans == "Y":
    my_string=str(input("enter the string: "))
    column_num(my_string)
    ans=str(input("Do you want to find the column number for another value: "))
