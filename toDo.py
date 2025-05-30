todos = []

def add(task):
    """Add a task to the to-do list"""
    todos.append(task)

def clear():
    """Clear all the tasks from the to-do list"""
    todos.clear()

def remove(task):
    """remove the specified task"""
    todos.remove(task)
