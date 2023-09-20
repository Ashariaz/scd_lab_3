from statistics import mean

#Task 1
list=[]
for i in range(5):
    list1=int(input("Enter:"))
    list.append(list1)
print(sum(list))
print(mean(list))


#Task 2

print("List after reverse : ", list[::-1])


#task 3

maximum=max(list)
minimum=min(list)
print("Maximum Number", maximum)
print("Minimum Number", minimum)
