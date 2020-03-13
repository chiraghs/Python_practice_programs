#lists are variables that store multiple values

users=['hi','chiz','jon','stark','tony','jaime']
print(users[1])
print(users[1:3])
print(users[2:])

#append,   insert,  delete an element
users.append('New item')
users.insert(0,"First_item")
users.insert(3,"item")
print(users.index('jon'))
users.pop(1)
print(users)


#multiple values
zeros=['0'*5]
print(zeros)
print(len(zeros))

zeros_n_time=['0']*5
print(zeros_n_time)
print(len(zeros_n_time))


#unpacking -values of lists to individual variables
items=['laptop',"Phone","watch",'TV']
a,b,c,d=items

print(b)
print(c)

a,b,*other=items
print(a)
print(other)
