import hashlib
  
str = "DROGON"
result = hashlib.sha1(str.encode())
print(f"The hexadecimal equivalent of {str} or its sha1 hash is : ", end ="")
print(result.hexdigest())
