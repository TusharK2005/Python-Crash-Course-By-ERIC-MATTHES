#Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. 
# Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

# Intentional Error Example
friends = ['Josh', 'Eric', 'Tushar']

# This will produce an IndexError because there is no item at index 5
print(friends[5])  

# Corrected version
print(friends[2])  # Accessing the last valid element "Charlie"