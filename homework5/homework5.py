# 2 Homework 1 + 2 Review 
#2.1 Vocabulary Review 
#Git is the actual tool used while GitHub is the overall website. 
#The terminal is where the command line is found, the command line is where you can actually execute what you want to do.
#Local repository is private and on your own computor while a remote repository is a copy of your project on a platform that can be shared.
#Version control is when you manage changes of your files over time.
#The staging area is the area between the working directory and the repository. 
#git add adds the file content from working directory into the staging area 
#git commit saves the changes in the staging area.
#git push sends the file content from staging area to the repository. 
#git status shoes the current state of the repositorys working directory and staging area.
#git pull gets changes from a repository into the current branch.
#pwd prints the path of the current directory youre in.
#ls shows the files stored in the directory. 
#cd lets you change directorys. 
#nano allows you to edit text in a file in a terminal. 
#touch allows you to create a coding file. 
#mv allows you to move files to a different directory.
#rm allows you to remove/delete files.
#cat is used to read text files. 

#2.2 A directory tree
#pwd
#ls
#cd homework then cp ~/python_decal/brianna_repo/homework.py ~python_decal/judy_decal/homework
#cd .. then cd brianna_repo
#code . 
#git add git commit git push
#Judy pushed before saving new changes to her local repository. git pull origin main to fix. 
#Depends what directory you are in. Assuming youre in homework, cd ../../.. then cd Recent

#3 Homework 3 review 
#3.1 data types
def checkDataType(x):
    y = type(x)
    s = str(y)
    return s 
print(checkDataType(5))
#3.2 conditionals
def evenOrOdd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
print(evenOrOdd(5))
#4 Loops
def sumWithLoops(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total

#5 Homework 4 Review 
#5.1 lists 
def duplicateList(x):
    lst = []
    for i in range (len(x)):
        lst.append(x[i])
        lst.append(x[i])
    return lst
print(duplicateList([1, 2, 3, 4, 5]))
#5.2 debugging 
def square(num):
    return num * num
# : was missing from the function name.

#Running the code 
print(sumWithLoops([1, 2, 3, 4, 5]))

