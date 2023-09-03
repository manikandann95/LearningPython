'''text file containing current visitors at a hotel. We'll call it, guests.txt. Run the following code to create the file. 
The file will automatically populate with each initial guest's first name on its own line.
'''

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"] # Guests (Only first names are used)

for i in initial_guests:
    guests.write(i + "\n") # Writing file with one line - one guest
    
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line) # Printing each guest names

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a+") as guests: # Append only mode
    for i in new_guests:
        guests.write(i + "\n") # writing in append mode

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

  checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests: # Converting guests from file to list
    for g in guests:
        temp_list.append(g.strip()) # Strip to leave \n in all lines' end

with open("guests.txt", "w") as guests: # creating new file here with w mode
    for name in temp_list:
        if name not in checked_out: # removing checked out guests
            guests.write(name + "\n") # adding remaining guests

with open("guests.txt") as guests:
    for line in guests:
        print(line) # Printing remaining guests list

guests_to_check = ['Bob', 'Andrea'] #Checking whether they are in or out
checked_in = [] # currently in guests

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip()) # strip use while converting file to list (append only works in list)
    for check in guests_to_check:
        if check in checked_in: # If guest in list, check
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))
