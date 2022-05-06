p=101
prlist=[]
def checkifpr(num):
    table=[]
    index=1
    while index<p:
        x=pow(num,index,p)
        if x in table:
            return
        else:
            table.append(x)
        index+=1
    prlist.append(num)
    return

for i in range(p):
    checkifpr(i)
    
print(prlist)

g=int(input('Enter any of the following values: '))
A=24
B=32
Encrypted_A=int(pow(g,A,p))
print(f'Encrypted_A={Encrypted_A}')
Encrypted_B=int(pow(g,B,p))
print(f'Encrypted_B={Encrypted_B}')
Secret_At_A=pow(Encrypted_B,A,p)
print(f'Secret_At_A={Secret_At_A}')
Secret_At_B=pow(Encrypted_A,B,p)
print(f'Secret_At_B={Secret_At_B}')
