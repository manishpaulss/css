text='meet me at the park'
key='1023'
def encrypt(text,key):
    row,col=(4,4)
    #To create matrix 
    arr=[['0']*row for _ in range(row)]
    #to join the text
    text=''.join(text.split())
    index=0
    #fill column with text
    for i in range(len(arr)):
        for j in range(len(arr)):
            if index==len(text):
                break
            else:
                arr[i][j]=text[index]
                index+=1
    encryption=''
    #use key to find the encrypted letters
    for num in key:
        num=int(num)
        for j in range(row):
            if arr[j][num]=='0':
                break
            else:
                encryption+=arr[j][num]
    print(encryption)


encrypt(text, key)