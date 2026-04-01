sentence = "This example has five words"
words = sentence.split()

upper_words = []
for i in range(len(words)):
    upper_words.append(words[i].upper())

print(upper_words)

nums = [2, 3, 4, 5]

squares = []
for i in range(len(nums)):
    squares.append(nums[i] * nums[i])

print(squares)

a = [1, 2, 3, 4]
print(a)

a[3] = 0
print(a)
