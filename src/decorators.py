from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует вызов функции и ее результат в файл или на консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write("my function OK")
                else:
                    print("my function OK")
                return result
            except Exception as e:
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write(f"my function error:{e}. Input: {args, kwargs}")
                else:
                    print(f"Функция не отрабатывает - введите корректные данные: Ошибка {e}")
                # return f"Функция не отрабатывает - введите корректные данные: Ошибка {e}"
                # return Exception("f"Функция не отрабатывает - введите корректные данные: Ошибка {e}"")
                return func(*args, **kwargs)

        return wrapper

    return decorator


@log(filename="test_log.txt")
# @log(filename="")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
