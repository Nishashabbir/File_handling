
# Create a system:
# File: students.txt
# Each line:
# Name,Marks
# Example:
# Ali,85
# Sara,90
# Program must:
# Read file
# Parse data
# Print students with marks > 80


# try 1 
# with open("student.txt" , "r" , encoding="utf-8") as f : 
#     # data=f.read() #this is what causing problem becuase data is in character by character , we should apply the loop , on the f directly 
#     for line in f : #we will simply go with this 
#         line=line.strip()
#         if not line : 
#             continue
#         name , marks = line.split(" ,")  #this is the main line it takes the line 'nisha , 19' , it splits it into two assigns the two varibels , nisha goes to name and 19 goes to marks , but the data that we split is in string , not an integer but to apply our logic , we need the data to be in integer so we further converted it ,  
#         marks=int(marks)
#         if marks>18:
#             print(f" {name} : {marks }")

# we assigned two variables by splitting the line 


   
# string methods split() and join()

# words=["Ali" , "19"]
# result= "".join(words)
# print(result)


# text= "Ali85"
# print(text.split())


# Q-2 
# Image copier
# or 
# basic image viewer in Python
# or even 
# convert image to grayscale (fun one)

# What it does
# Reads an image file (binary mode)
# Copies it into a new file
# Creates an exact duplicate of the image

#  Basically: you are manually cloning an image
# we already did this 



# Q-3
# copying and writing the whole folder 

# Reads all images from a folder
# Copies them into another folder
# Keeps original names
# Works for multiple files at once


import os 

# source_folder="images"
# dest_folder="images_backup"

# # create the dest_folder if doesn't exist
# if not os.path.exists(dest_folder):  
#     os.mkdir(dest_folder)
#     # now we want to see all the images file of this folder 
# for file_name in os.listdir(source_folder):
#     if file_name.endswith((".jpeg" , ".webp" ,".jpg" , ".png" )): #remember to use tuple inside this endswith method 
#         source_path=os.path.join(source_folder , file_name)
#         dest_path=os.path.join(dest_folder , file_name)
#         # now we have two paths to use , to read from one and write to anyone else 
#         with open(source_path , "rb") as f:
#             data=f.read()
#         with open(dest_path , "wb") as f:
#             f.write(data)
#             print(f"copied : {file_name}")

# print(" all the files have been copied successfully! ")
            

# try again 

#  Q-3
# copying and writing the whole folder 

# Reads all images from a folder
# Copies them into another folder
# Keeps original names
# Works for multiple files at once



# copy the folder and write ,it means we have to read from one and write in the other , read should exist as a source and the one we want to write in should either  exist or we should create one 

source_folder="images"
dest_folder="images_backup" 

if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)
for file_name in os.listdir(source_folder): #we can loop through a list , not a folder directly so listdir was used 
    # now we want to know each image file in the folder , obviously we can't remember their names but we know their extensions so we can do this 
    if file_name.endswith((".webp" , ".jpg" , ".jpeg" , ".png")):
        # now we will create their file path 
        source_path=os.path.join(source_folder , file_name)
        dest_path=os.path.join(dest_folder , file_name)
        with open(source_path, "rb") as f:
            data=f.read()
        with open(dest_path , "wb") as f:
            f.write(data)
            print(f"copied :{file_name} ")

print(f"All the files have been copied successfuly , backup ready")

# actually we opened and copied using the file paths , we didn't open a folder and paste the files in it but why we used folders because we had to create the file path folder+filename that's why we did that , for every file to be copied , so we stayed in the loop 



# open file => open 
# close file , better use with open as it automatically closes it as well 
# read file , open in "r " mode and read binary with rb
# writefile , write for binary wb
# check if path exists , os.path.exists for current folder and give path r"c\" for other folders as well 
# os.mkdir for creating folder 
# os.listdir for listing all the files in that folder 
# copy image read from one and copy to other , in  bytes 
# to view the file , os.startfile to view or pillow library use image module to open image as well as show image 
# to create the path with folder and file name ,use python's join method 
# endswith is used to know the ending characters of string 
# when you are reading the binary file , it will be so many  bytes so remember to use slicing for just few bites [:40]