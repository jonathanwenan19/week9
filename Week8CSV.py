file=None
with open('data.csv','r') as x:
    file= x.read()
result={}
for line in range(1,len(file.split('\n'))):
    data= file.split('\n')[line].split(',')
    print(data)
    counter=0
    steps=0
    if data[0]!="NA":
        counter+=int(data[0])
        steps+=1
    else:
        steps+=1
        data[0]= 0
print(line)
print(steps)
print(counter)
