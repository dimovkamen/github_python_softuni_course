class Party:
    def __init__(self):
        self.people_list = []


party = Party()

while True:
    name = input()

    if name == 'End':
        break

    party.people_list.append(name)

print(f"Going: {', '.join(party.people_list)}")
print(f"Total: {len(party.people_list)}")
