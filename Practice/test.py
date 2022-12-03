numbers=[1,2,3,4,5,6,7,8,9]

modified=[]

for num in numbers:
    modified.append(num*2)

print(modified)

prizes=[120,340,560,890,200, 1105]

dbl_prizes=[prize*2 for prize in prizes]

print(dbl_prizes)


squred_nums_even=[]

for num in numbers:
    if(num**2)%2==0:
        squred_nums_even.append(num**2)

print(squred_nums_even)

cubed_nums_even=[num**3 for num in numbers if(num**3)%2==0]

print(cubed_nums_even)