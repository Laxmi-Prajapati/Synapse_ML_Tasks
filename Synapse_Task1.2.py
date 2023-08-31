lst = ['0001','0011','0101','1011','1101','1111']

new_lst = [int(binary, 2) for binary in lst]

print("new_lst =",new_lst)

while len(new_lst)>2:
    num1 = min(new_lst)
    new_lst.remove(num1)
    num2 = min(new_lst)
    new_lst.remove(num2)
    new_lst.append(num1+num2)

difference = abs(new_lst[0]-new_lst[1])

print("new_lst =",new_lst)
print ("The least difference between Barbie and Ken:",difference)