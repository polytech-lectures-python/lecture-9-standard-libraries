import re

EMAIL_PATTERN = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


class EmailChecker:
    def __init__(self, pattern):
        self.__valid_email_pattern = pattern
        self.__regex = re.compile(self.__valid_email_pattern)

    def __call__(self, email):
        if self.__regex.fullmatch(email):
            print(f"{email} is a valid email")
        else:
            print(f"{email} is not a valid email")


if __name__ == '__main__':
    email_checker = EmailChecker(EMAIL_PATTERN)

    email_checker("a_b@mail.ru")
    email_checker("a_@yandex.ru")
    email_checker("a-@mail.com")
    email_checker("ab@m.ru")
    email_checker("username@mail.a")
