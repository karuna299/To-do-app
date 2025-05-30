from toDo import add, clear, todos, remove

def test_add_task():
    """Test adding a task to the to-do list"""
    add("Buy milk")
    assert "Buy milk" in todos

def test_clear():
    """Test celaring the to-do list"""
    add("Buy milk")
    clear()
    assert len(todos) == 0

def test_add1_task():
    """Adding more task in todos"""
    add("Buy Potatoes")
    assert "Buy Potatoes" in todos

def test_add2_task():
    add("Buy coke")
    assert "Buy coke" in todos

def test_clear_task():
    """clear coke from the list""" 
    add("Buy candy")
    remove("Buy coke")
    assert len(todos) == 2
