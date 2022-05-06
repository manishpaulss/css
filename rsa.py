def gcd(a,b):
    while 1==1:
        temp=a%b
        if temp==0:
            return b
        else:
            a=b
            b=temp
P=101
Q=103
n=P*Q
T=(P-1)*(Q-1)
e=2
while e<T:
    if gcd(e,T)==1:
        break
    else:
        e+=1

msg=32
print(f'MSG={msg}')
cText=pow(msg,e,n)
print(f'cText={cText}')
k=1
while k<n:
    d=(1+(k*T))/e
    if d==int(d):
        break
    else:
        k+=1

dtext=pow(cText,int(d),n)
print(f'dText={dtext}')