# Create open dictionary
the_dict = {}

#User input
string = input("Enter a string: ").lower()
string = string.split()

# Add key to dictionary and assign value to that particular string.
for key in string:
    if key in the_dict:
        the_dict[key] +=1
    else:
        the_dict[key] = 1

# Loop for printing
for string in sorted(the_dict):
    print("{:<12} : {}".format(string, str(the_dict[string])))


