from pluck.tasks.simple_task import SimpleTask


def test_task_id():
    def dummy_func():
        pass

    task = SimpleTask("dummy", dummy_func)
    assert task.id == "dummy"


def test_no_dependencies():
    def dummy_func():
        pass

    task = SimpleTask("dummy", dummy_func)
    assert task.dependencies == []


def test_has_dependencies():
    def dummy_func():
        pass

    task = SimpleTask("dummy", dummy_func, ["dummy_dep"])
    assert task.dependencies == ["dummy_dep"]


def test_call():
    def dummy_func(x, y):
        return x * y

    task = SimpleTask("multiply", dummy_func)
    result = task(3, 4)
    assert result == 12


def test_call_arg_order():
    def concat_strings(a, b):
        return a + b

    task = SimpleTask("concat", concat_strings)
    result = task("Hello, ", "World!")
    assert result == "Hello, World!"


def test_call_with_kwargs():
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    task = SimpleTask("greet", greet)
    result = task("Alice", greeting="Hi")
    assert result == "Hi, Alice!"
