var1=input("Enter the name1:").lower( )
var2=input("Enter the name2:").lower( )
var1=var1.replace(" ","")
var2=var2.replace(" ","")

for i in var1:
    for j in var2:
        if i==j:
            var1=var1.replace(i,"",1)
            var2=var2.replace(j,"",1)
            break
count=len(var1+var2)

if count>0:
    lst=["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
    while len(lst)>1:
        c=count%len(lst)
        s_index=c-1
        if s_index>=0:
            left=lst[:s_index]
            right=lst[s_index+1:]
            lst=right+left
        else:
            lst=lst[:len(lst)-1]
print("Here is your relationship:",lst[0])

