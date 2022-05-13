import base64 
  
  
file = open('mystery_img1.txt', 'rb') 
byte = file.read() 
file.close() 
  
decodeit = open('mystery_img.jpeg', 'wb') 
decodeit.write(base64.b64decode((byte))) 
decodeit.close() 


with open("FCFM.PNG", "rb") as image2string: 
    converted_string = base64.b64encode(image2string.read()) 
print(converted_string) 
  
with open('fcfm.txt', "wb") as file: 
    file.write(converted_string)