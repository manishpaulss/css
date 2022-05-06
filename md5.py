import hashlib
  
str = "DROGON"
  
result = hashlib.md5(str.encode())
  
print(f"The hexadecimal equivalent of {str} or its md5 hash is : ", end ="")
print(result.hexdigest())