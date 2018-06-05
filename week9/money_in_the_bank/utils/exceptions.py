class PasswordIncludesUsernameError(Exception):
    pass


class PasswordTooShortError(Exception):
    pass


class PasswordRequiredCharsMissingError(Exception):
    pass