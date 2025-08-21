#Shrinking Guest List: You just found out that your new dinner table won’t
#                      arrive in time for the dinner, and you have space for only two guests.
#   • Start with your program from Exercise 3-6. Add a new line that prints a
#       message saying that you can invite only two people for dinner.
#   • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name
#      from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#   • Print a message to each of the two people still on your list, letting them
#       know they’re still invited.
#   • Use del to remove the last two names from your list, so you have an empty
#       list. Print your list to make sure you actually have an empty list at the endof your program.

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
print(f"Hey {guest[5]}, please come to the dinner at my place on 12.02.22\n")

print("Just found out that the new dinner table won't arrive in time for the table. So can only two people for dinner.\n")





