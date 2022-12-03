# from random import shuffle
# def jumble(word):
#     anagram=list[word]
#     shuffle(anagram)
#     return ''.join(anagram)
#
# anagrams=[]
#
# words=['Beef','Mutton','Fish','Pork','chicken','Curry']
#
# for word in words:
#     anagrams.append(jumble(word))

def oddnum(num):

    if(num%2)!=0:
        return num
    else:
        return "Even"

numbers=[1,2,3,4,5,6,7,8,9,10]

odds=[]

for number in numbers:
    odds.append(oddnum(number))


odds2=list(map(oddnum,numbers))
# print(odds2)

def notdivisiblebythree(num):
    return num%3!=0

filter=filter(notdivisiblebythree,numbers)
# print(list(filter))

filter2=[num for num in numbers if(num%3!=0)]
# print(filter2)

salaries=[2000,3000,5000,7000,1000]

withcomm=list(map(lambda n:n*1.033, salaries))

# Lambdas reooaded
interest=[23030,40901,6702,5600]

def computeInterest(salary):
    return salary+salary*0.14

# salaries=[computeInterest(salary) for salary in interest]
salaries=list(map(lambda salary:salary+salary*0.14,salaries))

print(salaries)

numbers=[1,2,3,4,5,6,7,8]
def square(n):
    return n*n

squres=list(map(lambda n:n*n,numbers))
print(squres)