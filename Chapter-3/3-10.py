#Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

everything = ['everest', 'ganga', 'india', 'west bengal', 'kolkata', 'bengali', 'tushar', 'python']


print(f" - The tallest mountain in the the world is the Mt.{everything[0].title()}\n") # Use of .title()

everything.append('dugra puja')
print("\n 1.",everything)
print(f"\n{everything[8].title()} is the biggest festival of {everything[3].title()}.") # Use of .append()

everything.insert(7, 'kirtunia')
print("\n 2.",everything)
print(f"\n - My name is {everything[6].title()} {everything[7].title()}.") # Use of .insert()

del everything[8]
print("\n - Removed the word 'python'", everything, "from the list") # use of del()

message = everything.pop(2)
print(f"\n - I am a citizen of {message.title()}.") # Use of pop()

everything.append('python')
print("\n 3.",everything)
everything.remove('python')
print("\n 4.", everything)
print("\n - I have added the element 'python' just to use the .remove() on it.") # Use of .remove()

print("\n 5.", everything) 
print("\n - Alphabetical (using sorted):", sorted(everything)) # Use of temporary sorted()

print("\n - Reverse alphabetical (using sorted):", sorted(everything, reverse=True)) # Use of temporary reverse_sorted()
print("\n 6.", everything)

everything.reverse()
print("\n - List after reverse():", everything) # Use of .reverse()

everything.sort()
print("\n - List after sort() in alphabetical order:", everything) # Use of permanent .sort()

everything.sort(reverse=True)
print("\n - List after sort() in reverse alphabetical order:", everything) # Use of permanent .sort(reverse=True)

print("\n - The the length of the list is: ", len(everything), "\n") # use of len()









