first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print ("The summary is", sum)

i=1
while i<=5:
    print(i * '*')
    i=i+1


numbers = range (5, 10, 2)
for number in range(5):
    print (number)

    todos = []

    while True:
        user_action = input("Type add or show or exit: ")
        user_action = user_action.strip()

        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
            case 'show' | 'display':
                for item in todos:
                    item = item.title()
                    print(item)
            case 'exit':
                break
            case x:
                print("Wrong input!!")

    print("bye")


##Edit function
todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye")
##
todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
            file = open()
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number -1)
        case 'exit':
            break

print("Bye")
##
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number -1)
        case 'exit':
            break

print("Bye")
##01/25
contents = ["123", "kkk", "hello world"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'files/{filename}', 'w')
    file.write(content)

a = ("I am a string" 
     " on my own")
print(a)
##
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break

print("Bye")
##