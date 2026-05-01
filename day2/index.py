
# log system :
# def log(msg):
#     with open("test.txt" , "a") as f:
#         f.write(msg + "\n" )
#     print("done")

# log("A function was called and i was written here ")

# now we don't have to write the code  lines for each files to open , we will just call the function and things will fall in place 

# using a better way 
# from datetime  import datetime


# def log(msg):
#     with open("test.txt" , "a") as f :
#         f.write(f"at {datetime.now} : {msg}")
#     print("\nProcess done")

# log("Program started!\n")
# log("Program tw warr gya !")



# now lets understand the binary mode //////////////////////////////

# #1- read binary 
# with open("model.png" , "rb") as f :
#     data=f.read()
#     print(data[:50]) #this will just print the first 50 bytes

# rb is read binary file mode , and it just reads the raw bytes 0 , 1 
# so the printed data will also be a raw byte form data 

# 2-write binary 
# you can also copy  the file wb => write binary 
# with open("model.png" , "rb") as f:
#     data=f.read()
#     # print(data[:20]) #20 otherwise it will read huge data 
# with open("copy.png" , "wb") as f:
#     f.write(data)
#     print("done")
    # wowww , here you literally wrote the binary code in the file and the image was copied hahahaha


# NOTE : here in this code  :     print(data)
# read only can print the raw data in the form of bytes , it can not display image in the terminal 
# terminal can only print the text and characters , not the images 

# Final clean version (best practice)/////////////////
# with open("model.png", "rb") as src, open("copy.png", "wb") as dst:
#     dst.write(src.read())


# How to actually VIEW the image//////////////////////
# Option 1: Open with system viewer (simple)


# import os 
# os.startfile("model.png")
# now the operating system will open your file and the image will be displayed with system viewer , 
# wonderfullllllllllllllllllllll girlllllllllllllllllllllllll wow 

# pillow library of python 
# from PIL import Image  #for that you have to install the PIL as pip install pillow 

# img = Image.open("image.jpg")
# img.show()



# both practises
# import os 
# os.startfile("model.png")

# from pil import image
# i=image.open("filename")
# i.show() #now this code will work in the terminal 


# Encoding (Advanced but Important)//////////////////////////////
# with open("guide.txt", "r", encoding="utf-8") as f:

# # Avoid weird character errors.

# # only one thing is extra that third parameter will be encoding  utf-8 to avoid weired characters 

with open("guide.txt" , "r" , encoding="utf-8") as f:
    print(f.read())

