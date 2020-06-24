task = input('enter task: ')

file = open('tasks.txt', 'w')
file.write(task)
file.close()