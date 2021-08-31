import time
f1=open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\documents\fsprojt1.txt", errors='ignore')
cr=0
cont=f1.read()
co=cont.split("\n")
for i in co:
    if i:
        cr+=1
print("number of lines:",cr)        
print("INDEXING STARTED")
c=0
start=time.time()
with open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\documents\fsprojt1.txt") as pack:
    with open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\index\index 1.txt","w") as index:
        count=0
        f=pack.read()
        s=f.replace("\n","")
        for line in s.split(" "):
            stri=line[:]
            index.write(stri+" ")
            c=str(count)
            index.write(c+"\n")
            count=len(line)+count
end=time.time()
print("Indexing Completed in",end-start,"seconds")
 
with open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\documents\fsprojt1.txt") as main:
    with open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\index\index 1.txt","r") as index:
        lines=main.readlines()
        search = input("Enter the word to be searched:") 
        start2 = time.time () 
        for line in index:
            if search in line:
                print("The line is here in index file"+ line)
                line1 = line.split(" ") 
                loc = line1[1].split() 
                locate = int(loc[0]) 
                x = main.seek(locate) 
                y = main.readlines(locate) 
                result= [ind for ind in y if search in ind] 
                result1= result[0].split(' ') 

                c=1
                for m1 in main.readlines():
                     l = m1.split(" ") 
                     loc1 = line1[1].split()
                locate1 = int(loc[0]) 
                x1 = main.seek(locate1) 
                y1 = main.readlines(locate1) 
                for n in y1:
                    if search in n:
                        str1=" "
                        n1=n.split(" ")
                        print(str1.join(n1)) 
if c==1:
    end1=time.time()
    print("Searching completed in:",end1-start2,"seconds")
                             
    ques=input("Do you want to modify Y/N:")
    if ques=='Y' or ques=='y':
        f1=open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\documents\fsprojt1.txt", errors='ignore')
        data=f1.read()
        f2=input("Enter the word to be replaced:")
        f3=input("Replace with:")
        start3=time.time()
        replaced_value=data.replace(f2,f3)
        f1=open(r"C:\Users\deepika\Downloads\File-Structures-master (1)\File-Structures-master\documents\fsprojt1.txt","wt")
        f1.write(replaced_value)
        end3=time.time()
        print("Replaced Successfully in",end3-start3,"seconds")
        f1.close()
    else:
        print("Done with the program")
else:
    print("search is unsuccesfull")