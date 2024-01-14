import os
import time
import functools


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} секунд.")
        return result

    return wrapper


class CommandPrompt:
    def __init__(self):
        self.current_path = os.getcwd()

    @timing_decorator
    def list_directory(self):
        for item in os.listdir(self.current_path):
            print(item)

    @timing_decorator
    def change_directory(self, path):
        if path == "..":
            self.current_path = os.path.dirname(self.current_path)
        else:
            new_path = os.path.join(self.current_path, path)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                self.current_path = new_path
            else:
                raise Exception("Директория не найдена")


cmd = CommandPrompt()
while True:
    command = input(f"{cmd.current_path}> ")
    if command == "exit":
        break
    elif command == "ls" or command == "dir":
        cmd.list_directory()
    elif command.startswith("cd "):
        _, path = command.split(maxsplit=1)
        try:
            cmd.change_directory(path)
        except Exception as e:
            print(e)