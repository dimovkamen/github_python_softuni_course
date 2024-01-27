number = int(input())
numbers_list = []
# count_positives = []
# sum_of_negatives = []

positives = []
negatives = []

for _ in range(number):
    number_input = int(input())
    if number_input >= 0:
        positives.append(number_input)
    else:
        negatives.append(number_input)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
