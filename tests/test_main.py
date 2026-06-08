from test_python_release.main import greet

def test_greet():
    assert greet("Test") == "Hello, Test!"
