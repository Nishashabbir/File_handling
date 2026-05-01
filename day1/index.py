

#1- opening a file 
# f=open("guide.txt" , "r")
# print(f) #here the file content will not be printed as  you are printing the file object, not the contents of the file. That’s why you see something

# you can open any file in any folder by giving this path as well
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())



# 2- READING A FILE 
# you can also read just the specified characters of the file 
# with open("demofile.txt") as f:
#   print(f.read(5))

# read one line of the file 
# with open("demofile.txt") as f:
#   print(f.readline())

# By calling readline() two times, you can read the two first lines:

# if file has multiple lines , you can loop through those files as well 
# Loop through the file line by line:

# with open("demofile.txt") as f:
#   for x in f:
#     print(x)


# # create a new file with specific name , if already present then throws the errors 
# Create a new file called "myfile.txt":

# f = open("myfile.txt", "x")

# read all 
# f=open("test.txt" , "r")
# data=f.read()
# print(data)
# f.close()

# note : Most text files today use UTF-8, so do this:
# with open("guide.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     print(data)

# # read line 
# data=f.readline()
# print(data)

# now read all the lines as a list 
# data=f.readlines()
# print(data)
# f.close() #remember always close the file otherwise memory resources leak 

# better and professional way is this 

# with open("test.txt" , "r") as f :
#     data=f.read()
    ## print(f.read()) or directly you can print the content here 

# print(data)

# with open method automatically closes the file , it is safer and cleaner method 


# 3-WRITING A FILE 

# with open("test.txt" , "w") as f:
#     data=f.write("Hello")
# # it does NOT return the text — it returns the number of characters

# print(data) #5

# # if you want to see the text of  the file  you wrote then  you have to read it 
# with open("test.txt" , "r") as f:
#     print(f.read()) #so now it gives hello 

# Note: the "w " in the write file overwrites , means it removes the older content of the file 

# 4- APPEND MODE 

# with open("test.txt" , "a") as f:
#     f.write("\n My name is Nisha ") #now this will append in the file , everytime when you run this 

# with open("test.txt" , "r") as f:
#     print(f.read())

# writing multiple lines 

# list=["My name is Nisha\n" , "I am a CS student \n" , "I am a web developer\n" "I am a cloud engineer\n"]

# with open("test.txt" , "w") as f:
#     # data=f.write(list)
#     data=f.writelines(list) #this will be used for writing  multiple lines 

# with open("test.txt", "r") as f:
#     print(f.read())


# you can also loop through this 
# with open("test.txt" , "r") as f:
#     for line in f:
#         print(line.strip())
# this reads line by line , used in the larger files 


# cursor in the file 

# with open("test.txt" , "r") as f:
#     print(f.read()) #this will print the content of the file 
#     print(f.read()) #this will print nothing , just empty 

# why?? 
# the reason is there is a cursor in the file that tracks the content , when you read() the entire file , the cursor reaches the end and then there is nothing to read , so it returns empty second time but if you want to read in the loop , there is a fix that you can use 


# fix : 
# with open("test.txt" , "r") as f:
#     print(f.read()) 
#     f.seek(0) #will start reading from the beginning 
#     f.seek(5) #this will start reading from the 5th character 
#     print(f.tell()) #now it will tell at which character or index is it ? 
#     print(f.read())

# now both the read lines will print the same content 

# seek() is used to move cursor to specific position and index , if index is 0 , it moves to the start and you can also use other indices 

# you can also know where you are at the current poistion 
#  print(f.tell()) cursor is  telling where is it 


# check if the file exists in the current folder ////////////////////////

import os 
# print(os.path.exists("test.txt"))  #it will print TRue 
# print(os.path.exists("data.txt"))  #False 

# Note: It just checks this file only in the current folder , day1 , not anywhere 

# you can also check the current folder or directroy 

# print(os.getcwd())  #getcurrentworking directory getcwd
# C:\Users\User\Desktop\File_handling\day1 this is the output showing folder history 


# if the file exists in another folder use the full path  //////////////////////

# check if this file is in that folder path 

# print(os.path.exists("C:\\Users\\User\\Desktop\\File_handling\\day1\\day0\\tell.txt "))

# so this is True


# if os.path.exists("tests.txt"):

#     with open("tests.txt" , "r") as f:
#         print(f.read())
# else:
#     print("file not found")

# it will open the file if exists otherwise else statement 


# better way is to use pathlib 
from pathlib import Path

# print(Path("test.txt") .exists()) #True 

# if Path("C:\\Users\\User\\Desktop\\File_handling\\day1\\day0\\tell.txt").exists():
#     with open("tell.txt", "r") as f:
#         print(f.read())
# else:
#     print("file not found ")

# mistak: here you were trying to find the file in another folder but opening a file in the current folder , that's wrong 

# try2
# filepath="C:\\Users\\User\\Desktop\\File_handling\\day1\\day0\\tell.txt"
# filepath=Path("C:\\Users\\User\\Desktop\\File_handling\\day1\\day0\\tell.txt")

# if filepath.exists():
#     with open(filepath, "r") as f: 
#         print(f.read())
# else:
#     print("file not found ")

# mistake: here you didn't use path first from pathlib so directly you can't use .exists on it 
   
    # try3 
# from pathlib import Path

# file_path = Path(r"C:\Users\User\Desktop\File_handling\day1\day0\tell.txt")
# note: r"C" this r is used for raw string , we don't need to double the backslash anymore with this 

# # print(file_path.exists())  # True

# if file_path.exists():
#     with open(file_path, "r") as f:
#         print(f.read())
#         f.seek(0) #it resets 
#         print(f.read())
        
# else:
#     print("file not found")


# os.path.exists 
# Path(filename).exists #better way 


# now doing this all with exception handling  //////////// 

# filepath=Path(r"C:\Users\User\Desktop\File_handling\day1\day0\tells.txt")
# try:
#     if filepath.exists():
#           with open(filepath, "w") as f:
#                print(f.write(" HI , I am handling the exceptions"))
#           with open(filepath, "r") as f:
#                print(f.read())
#     else:
#         print("not found")  #if you don't write this statement , nothing prints 

# except FileNotFoundError as e: #this will only trigger if naturally an error occur but we already confiremed if path exists or not 
#      print("file not found " , e)
          
        # try2 
# from pathlib import Path

# filepath = Path(r"C:\Users\User\Desktop\File_handling\day1\day0\tells.txt")

# try:
#     if filepath.exists():
#         with open(filepath", "w") as f:
#             f.write("HI, I am handling the exceptions")

#         with open(filepath, "r") as f:
#             print(f.read())
#     else:
#         print("File does not exist:", filepath)

# except Exception as e:
#     print("Unexpected error:", e)



# # simple example : 
# a=10
# if a==11:
#      print("yes ")

# we just said if this condition proves then print yes otherwise don't do anything , so no error and program doesn't crash 


# solution ;
# recommended use  simple 
# here python will read this file , but wait the file doesn't even exists , so what..? now python will throw an error and then this error will be handled by except statement unlike before where the error was not even thrown so except was not triggered as we already confirm if file exists then do that othewise python doesn't know what to do m so it never threw an error there  
# try:
#     with open(filepath, "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("File not found")


# deleting a file /////////////////////////
# to delte a file you need to load an os module 
# os.remove("demofile.txt")

# Check if file exists, then delete it:

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# #   to delte the folder 
# os.rmdir("foldername") #only when the folder is empty 



# and if not empty use shutil method 
# import shutil
# shutil.rmtree("demo_folder")
# removing the file that exists 
os.remove("demo.txt") #gone 

    