from time import time
from datetime import datetime
from time import sleep
from time import time
from contextlib import contextmanager


class Performance:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.curr_time = datetime.now()
        self.time_started = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_ended = time()
        execution_time = self.time_ended - self.time_started
        log = f'{self.curr_time}. Execution time: {execution_time}\n'
        self.file_handler = open(self.filename, "a")
        self.file_handler.write(str(log))
        self.file_handler.close()


@contextmanager
def context_manager(filename):
    try:
        curr_time = datetime.now()
        time_started = time()

        yield

        time_ended = time()
        execution_time = time_ended - time_started
        log = f'{curr_time}. Execution time: {execution_time}\n'
        file_handler = open(filename, "a")
        file_handler.write(str(log))
        file_handler.close()
    except:
        pass


@contextmanager
def assertRaises(err, msg=None):
    try:
        yield
    except Exception as exc:
        if type(exc) is type(err):
            print(f'{err} expected but {type(exc)} raised.')
        elif msg is not None and msg != str(err):
            print(f'"{msg}" message expected but "{str(exc)}" message received')
        else:
            return True



class AssertRaises:
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exception != exc_type and\
            (self.msg is None or self.msg == exc_val):
            print(f'{exc_type.__name__} with message {exc_val} raised!\n')
            print(f'{exc_tb}')

        return True

def main():
    with assertRaises(TypeError) as log:
        raise TypeError


if __name__ == '__main__':
    main()
