#import'ing usefull stuff
from tkinter import *

#appending window
#root = Tk()

def printTask():
    f = open('toDO.txt', 'r')
    print(open('toDO.txt', 'r').read())
    f.close()

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
        print('')

def deleteEveryTask():
    file = open('toDO.txt', 'r')
    lines = file.readlines()
    file.close()
    del lines[:25]
    new_file = open('toDO.txt', 'w+')
    for line in lines:
        new_file.write(line)
    printTask


#entering task
task = input('enter task: ')

#opening toDO.txt
file = open('toDO.txt', 'a+')
file.write(task)
file.write('\n')    
file.close()

#choice of deleting tasks
choice = str(input('Do you want to delete task or all tasks(type 3)?: '))
#making choice upper to be easier for input
choice.upper
#print current file
printTask()
file.close()

#choice of deleting file
decisionToDelete()

print('there are your tasks: ')
printTask()
print('goodbye!')

#root.mainloop()