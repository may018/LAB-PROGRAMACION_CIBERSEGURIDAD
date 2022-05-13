import base64

s = "Hola a todos!"

b = s.encode("UTF-8")

e = base64.b64encode(b)

s1 = e.decode("UTF-8")

print("Base64 Encoded:", s1)

b1 = s1.encode("UTF-8")

p1= "aG9sYQphCnRvZG9zCiEhCg=="
d = base64.b64decode(p1)

s2 = d.decode("UTF-8")
print(s2)