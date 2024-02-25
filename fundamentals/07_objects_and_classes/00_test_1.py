from email import Email


def main():
    email = Email('Peter', 'John', 'Hi,John')
    email.send()
    print(email.get_info())


print(__name__)

if __name__ == "__main__":
    main()
