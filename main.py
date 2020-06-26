#import'ing usefull stuff
from tkinter import *
import sys

#appending window
#root = Tk()

#functions#functions#functions#functions#functions#functions
#print tasks
def printTask():
    f = open('toDO.txt', 'r')
    print(open('toDO.txt', 'r').read())
    f.close()
#asking do you want to delete
def decisionToDelete():
    if choice == 'yes':
        file = open('toDO.txt', 'r')
        lines = file.readlines()
        file.close()
        which = int(input('Which task do you want to delete?: '))
        del lines[which - 1]
        new_file = open('toDO.txt', 'w+')
        for line in lines:
            new_file.write(line)
    elif choice == '3':
        deleteEveryTask()
    else:
        sys.exit
# deletes every task
def deleteEveryTask():
    file = open('toDO.txt', 'r')
    lines = file.readlines()
    file.close()
    del lines[:25]
    new_file = open('toDO.txt', 'w+')
    for line in lines:
        new_file.write(line)
    printTask
#asking if you want to add new task
def addNewTask():
    decision = input('do you want to enter new task?: ')
    if decision == 'yes':
        task = input('enter task: ')

        #opening toDO.txt
        file = open('toDO.txt', 'a+')
        file.write(task)
        file.write('\n')    
        file.close()
    else:
        print('ok, there are your current tasks')

addNewTask()

#printing current tasks
printTask()


#choice of deleting tasks
choice = str(input('Do you want to delete task or all tasks(type 3)?: '))
#making choice upper to be easier for input
choice.upper
#choice of deleting file
decisionToDelete()

print('there are your tasks: ')
printTask()
print('goodbye!')

#root.mainloop()