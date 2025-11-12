file=open("reny.txt","w")
file.write=("hello there :)\n nanni undeyyyyy\nthanks")
file.close()
list=[]
file=open("reny.txt","r")
list=[line.strip() for line in file ]
file.close()
print(list)
