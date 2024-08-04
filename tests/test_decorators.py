import os

from src.decorators import log, my_function


def test_log_different_types_str(capsys):
    # Проверка ошибки: missing 2 required positional arguments: 'x' and 'y'.
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function("a", "b")
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out


def test_1():
    my_function(10, 1)
    log_file = os.path.join(os.path.dirname(__file__), "test_log.txt")
    with open(log_file, "r") as file:
        log_test = file.read()
        assert log_test == "my function OK"
