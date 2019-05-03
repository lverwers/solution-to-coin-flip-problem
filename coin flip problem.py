
# coding: utf-8

# In[44]:


#note: n controls how many times the simulation will run
#1,000,000 was used for testing purposes but be aware
#that it will take 5 - 10 minutes to run depending on your
#computer. Use smaller n for less computation time, larger n 
#for greater accuracy. 
import random
hh = 0
ht = 0
tie = 0
c = 0
n = 1000000
while c < n:
    list = []
    x = 0
    while x < 72:
        list.append(random.randint(0,1))
        x+= 1
    a = str(list)
    b = a.find("1, 1")
    list2 = []
    y = 0
    while y < 72:
        list2.append(random.randint(0,1))
        y+= 1
    d = str(list2)
    e = d.find("1, 0")
    if e > b:
        hh+= 1
    elif e < b:
        ht+= 1
    else: 
        tie+= 1
    c+= 1
print("The probabiliity that ht wins is about " +str((ht*(100/n))) +" percent")
print("The probabiliity that hh wins is about " +str((hh)*(100/n)) +" percent")
print("The probabiliity that hh wins is about " +str((tie)*(100/n)) +" percent")


# In[46]:


#note: again, n controls how many times the simulation will run
#1,000,000 was used for testing purposes but be aware
#that it will (again) take 5 - 10 minutes to run depending on your
#computer. Use smaller n for less computation time, larger n 
#for greater accuracy. Use only even numbers for n in this program.
import random
import matplotlib.pyplot as plt
c = 0
list3 = []
list4 = []
n = 1000000
while c < n:
    list = []
    x = 0
    while x < 72:
        list.append(random.randint(0,1))
        x+= 1
    a = str(list)
    b = a.find("1, 1")
    list2 = []
    y = 0
    while y < 72:
        list2.append(random.randint(0,1))
        y+= 1
    d = str(list2)
    e = d.find("1, 0")
    list3.append((b+5)/3)
    list4.append((e+5)/3)
    c+= 1
average = sum(list3)/n
average_2 = sum(list4)/n
#average number of flips for HH
print("The average number of flips for HT is "+str(average))
#average number of flips for HT
print("The average number of flips for HT is "+str(average_2))
list3.sort()
list4.sort()
print("The median for HH is "+str((list3[int(n/2)]+list3[int((n/2)+1)])/2))
print("The median for HT is "+str((list4[int(n/2)]+list4[int((n/2)+1)])/2))  
print("The 25th percentile for HH is "+str((list3[int(n/4)]+list3[int((n/4)+1)])/2))
print("The 25th percentile for HT is "+str((list4[int(n/4)]+list4[int((n/4)+1)])/2))  
print("The 75th percentile for HH is "+str((list3[int((3/4)*n)]+list3[int(((3/4)*n)+1)])/2))
print("The 75th percentile for HT is "+str((list4[int((3/4)*n)]+list4[int(((3/4)*n)+1)])/2))  
list5 = []
for i in range(n):
    list5.append(i/100)
plt.plot(list5, list3, "ro")
plt.plot(list5, list4, "b.")

