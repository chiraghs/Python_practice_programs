import re
import operator

fh = open(r"/home/chiraghs/Downloads/b_read_on.txt","r")
r = fh.read().rstrip().split("\n")
m = re.findall('[0-9]+',r[0])
fh.close()
#print(m[1])
library=[]
sum=0
for i in range(0,int(m[1])):
    library.append(re.findall('[0-9]+',r[2+2*i]))



librardict_books={}
librardict_signup={}
librardict_bookperday={}


for i in range(int(m[1])):
        librardict_books[i]=int(library[i][1])
        librardict_signup[i]=int(library[i][1])
        librardict_bookperday[i]=int(library[i][1])

        #sum+=int(library[i][1])
        sorted_books = dict( sorted(librardict_signup.items(), key=operator.itemgetter(1)))
        sorted_signup= dict( sorted(librardict_signup.items(), key=operator.itemgetter(1)))
        sorted_booksperday = dict( sorted(librardict_signup.items(), key=operator.itemgetter(1)))


#print(sorted_books)      
#print(sorted_booksperday)      
#print(sorted_signup)      
 
sm = 0
Num_of_library= 0
library_signup_days=[]
library_index=[]
library_Total_books=[]
for v in sorted_signup.keys():
    sm += sorted_signup[v]
    library_Total_books.append(int(m[2])-sm)
    library_signup_days.append(sorted_signup[v])
    library_index.append(v)
    Num_of_library+=1
    if sm>=int(m[2]):break

#print(Num_of_library)
#print(library_index)
#print(library_signup_days)
#print(library_Total_books)

#list_books=[]
#for i in range(Num_of_library):
    #list_books.append(i*1000)
score = 0
print(Num_of_library)
for i in range(Num_of_library):
    if(i == Num_of_library-1):break
    print(library_index[i]," ",library_Total_books[i])
    for j in range(library_Total_books[i]):
        print(library_index[i]*1000+j ,end=" ")
        score += 1
    print()

#fa = open(r"G:\Hashcode\readon.txt","a+")
#fa.write(str(Num_of_library)+"\n")

#for i in range(Num_of_library):
    #if(i == Num_of_library-1):break
    #fa.write(str(library_index[i])+" "+str(library_Total_books[i])+'\n')
    #for j in range(library_Total_books[i]):
        #fa.write(str((library_index[i]*1000+j))+" ")
    #fa.write('\n')
#fa.close()