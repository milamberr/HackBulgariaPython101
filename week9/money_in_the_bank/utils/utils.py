from utils.exceptions import *


def accepts(*args):
    def accepter(func):
        def decorated(*types):
            for i in range(0, len(types)):
                if type(types[i]) is not args[i]:
                    raise TypeError(f'Argument {i} is not of type {args[i].__name__}')
            return func(*types)
        return decorated
    return accepter


def strong_pass():
    def accepter(func):
        def decorated(username, password):
            if username in password:
                raise PasswordIncludesUsernameError('Password includes username as a substring!')
            if len(password) < 8:
                raise PasswordTooShortError('Password must be at least 8 symbols')
            has_special_char = False
            has_capital_letter = False
            has_number = False
            for char in list(password):
                if char >= '0' and char <= '9':
                    has_number = True
                elif char >= 'A' and char <= 'Z':
                    has_capital_letter = True
                elif char < 'a' or char > 'z':
                    has_special_char = True
            if not has_number or not has_capital_letter or not has_special_char:
                raise PasswordRequiredCharsMissingError('Password must have a capital letter,a number and a special symbol!')
            return func(username, password)
        return decorated
    return accepter


# def change_pass():
#     def accepter(func):
#         def decorated(new_pass, logged_user):
#             