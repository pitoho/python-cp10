task = open('todos.txt')

with open('todos.txt') as task:
    for chore in task:
        print(chore, end='')
