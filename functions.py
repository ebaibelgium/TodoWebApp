def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of
    to-do items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todos_args, filepath='todos.txt'):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_args)




