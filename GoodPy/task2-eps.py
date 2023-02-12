my_string="aioeua"
flag=False
list_string=list(my_string)
i=len(my_string)-1 
while flag == False:
    flag=True
    for count in range(0,i):
        if list_string[count]>list_string[count+1]:
            temp=list_string[count]
            list_string[count]=list_string[count+1]
            list_string[count+1]=temp
            flag=False
    i-=1
# list_string.sort()
print(list_string)