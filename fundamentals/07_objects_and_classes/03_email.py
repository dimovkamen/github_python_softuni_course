class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails_list_of_objects = []

while True:
    command = input()
    if command == 'Stop':
        break

    email_info_list = command.split()
    sender_email, receiver_email, content_email = email_info_list
    email = Email(sender_email, receiver_email, content_email)
    emails_list_of_objects.append(email)

indexes_list = list(map(int, input().split(', ')))
#indexes_list = [int(i) for i in input().split(', ')]

for index in indexes_list:
    if 0 <= index < len(emails_list_of_objects):
        emails_list_of_objects[index].send()

for email in emails_list_of_objects:
    print(email.get_info())
