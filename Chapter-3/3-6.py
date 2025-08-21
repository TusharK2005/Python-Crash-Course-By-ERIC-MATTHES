# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

#   • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#     call to the end of your program informing people that you found a bigger dinner table.
#   • Use insert() to add one new guest to the beginning of your list.
#   • Use insert() to add one new guest to the middle of your list.
#   • Use append() to add one new guest to the end of your list.
#   • Print a new set of invitation messages, one for each person in your list.

guest = ['Josh', 'Pedro', 'Tushar']

print(f"Hey {guest[0]}, please come on 12.02.22")
print(f"Hey {guest[1]}, please bring your family too at my place on 12.02.22")
print(f"Hey {guest[2]}, please be present at my place on 12.02.22")

print(f"\nSorry, {guest[0]} can't make it to the dinner.\n")

guest[0] = 'Mike'

print(f"Hey {guest[0]}, please come on 12.02.22")
print(f"Hey {guest[1]}, please bring your family too at my place on 12.02.22")
print(f"Hey {guest[2]}, please be present at my place on 12.02.22\n")

print("Hey guys, I found a bigger dinner table.\n")

guest.insert(0, 'Sundar')
guest.insert(2, 'kush')
guest.append('Dan')

print(f"Hey {guest[0]}, you are invited to a special dinner on 12.02.22")
print(f"Hey {guest[1]}, please bring your family to dinner on 12.02.22")
print(f"Hey {guest[2]}, don't miss the dinner party on 12.02.22")
print(f"Hey {guest[3]}, I would love to see you at dinner on 12.02.22")
print(f"Hey {guest[4]}, join us for dinner and fun on 12.02.22")
print(f"Hey {guest[5]}, please come to the dinner at my place on 12.02.22")