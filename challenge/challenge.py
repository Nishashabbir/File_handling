
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

source_folder="images"
dest_folder="images_backup"

# create the dest folder if doesn't exist
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)
    # now we want to see all the images file of this folder 
for file_name in os.listdir(source_folder):
    if file_name.endswith(".jpeg" , ".webmp" ,".jpj" , ".png" ):
        source_path=os.path.join(source_folder , file_name)
        dest_path=os.path.join(dest_folder , file_name)
        # now we have two paths to use , to read from one and write to anyone else 
        with open(source_path , "r") as f:
            data=f.read()
        with open(dest_path , "w") as f:
            f.write(data)
            print(f"copied : {file_name}")

print(" all the files have been copied successfully! ")
            

