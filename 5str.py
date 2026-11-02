s = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("Replaced string:", s.replace(old, new))

print("Reversed string:", s[::-1])

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("Character frequency:")
for ch in set(s):
    print(ch, ":", s.count(ch))

print("Word frequency:")
words = s.split()
for word in set(words):
    print(word, ":", words.count(word))