def convert_sec(seconds):
    hr = seconds // (60  * 60)
    minutes = (seconds - (hr * 60 * 60)) // 60
    sec = seconds - (minutes * 60) - (hr * 60 * 60)
    return(hr, minutes, sec)
s = input("Enter Seconds: ")
a = convert_sec(int(s))
print(a)
