import collections

string = "Hey there whats up"
frequencies = collections.Counter(string)
count = {}

print(frequencies.items())

for key, value in frequencies.items():

    if value > 1:
        count[key] = value

print(count)


str = "buddy"

value = {}

for char in str:
    count = str.count(char)
    value[char] = count

print(value)
print(value.values())
print(max(zip(value.values(), value.keys()))[1])
