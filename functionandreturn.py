"""Converting seconds into Standard Time (Hours, Minutes, Seconds)"""
#Using user defined Function

def convert_sec(seconds):
    """User Defined Function"""
    hours = seconds // (60 * 60)
    minutes = (seconds - (hours * 60 * 60)) // 60
    sec = seconds - (minutes * 60) - (hours * 60 * 60)
    return(hours,minutes,sec)

givendata = int(input("Enter the time in seconds:\n"))

#result = convert_sec(seconds)
#Since One return value is assigned instead of three it assigned as Tuple (result variable)
#print(f"{seconds} seconds in Standard Time is {result}")

hr, minute, second = convert_sec(givendata)
print(f"\n{givendata} seconds converted as {hr} Hour {minute} minutes {second} seconds")
