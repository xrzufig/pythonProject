task = input('enter task: ')

file = open('tasks.txt', 'a+')
file.write(task)
file.write('\n')
file.close()