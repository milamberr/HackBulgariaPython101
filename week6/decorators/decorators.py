from functools import wraps

def accepts(*args):
    def accepter(func):
        def decorated(*types):
            for i in range(0, len(types)):
                if type(types[i]) is not args[i]:
                    raise TypeError(f'Argument {i} is not of type {args[i].__name__}')
            return func(*types)
        return decorated
    return accepter


def encrypt(num):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            result = func(*args)
            result = shift_string_by(result, num)
            return result
        return decorated

    return accepter


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorated(*args):
            from datetime import datetime
            
            func(*args)
            time = datetime.now()
            with open(file_name, 'a') as file:
                file.write(f'Function {func.__name__} was called at {time}\n')

            return func(*args)
        return decorated
    return accepter


def shift_string_by(word, value):
    shifted = ''
    for char in word:
        if char.isalpha():
            if char.islower():
                shifted = f'{shifted}{shift_lower_letter(char, value)}'
            else:
                shifted = f'{shifted}{shift_upper_letter(char, value)}'
        else:
            shifted = f'{shifted}{char}'

    return shifted


def shift_lower_letter(letter, value):
    return chr((ord(letter) - 97 + 2) % 26 + 97)


def shift_upper_letter(letter, value):
    return chr((ord(letter) - 65 + 2) % 26 + 65)


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def say_more(name, age):
    return f'Hello,I am {name} and I am {age} years old'


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


print(get_low())


def performance(file_name):
    def accepter(func):
        def decorated(*args):
            import time
            before_time = time.time()
            func(*args)
            after_time = time.time() - before_time
            with open(file_name, 'a') as file:
                file.write(f'Function {func.__name__} was called and took {after_time:.02} to complete\n')

            return func(*args)
        return decorated
    return accepter


@performance('log.txt')
def something_heavy():
    import time
    
    time.sleep(2)
    return 'I am done'


#print(something_heavy())
