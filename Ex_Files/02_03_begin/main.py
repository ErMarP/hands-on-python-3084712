NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]
Pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = Pares[::-1]
EVERY_OTHER = Pares[3::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(EVERY_OTHER)
print(REVERSE)
