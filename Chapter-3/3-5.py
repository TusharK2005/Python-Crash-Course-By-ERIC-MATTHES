#Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#       • Start with your program from Exercise 3-4. Add a print() call at the end
#         of your program stating the name of the guest who can’t make it.
#       • Modify your list, replacing the name of the guest who can’t make it with
#         the name of the new person you are inviting.
#       • Print a second set of invitation messages, one for each person who is still
#         in your list.

guest = ['Josh', 'Pedro', 'Tushar']

print(f"Hey {guest[0]}, please come on 12.02.22 ")
print(f"Hey {guest[1]}, please bring ur family too at my place on 12.02.22")
print(f"hey {guest[2]}, please be present at my place on 12.02.22")

print(f"\nSorry, {guest[0]} can't make it to the dinner.\n")

guest[0] = 'Mike'

print(f"Hey {guest[0]}, please come on 12.02.22 ")
print(f"Hey {guest[1]}, please bring ur family too at my place on 12.02.22")
print(f"Hey {guest[2]}, please be present at my place on 12.02.22")