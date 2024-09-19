#Program 9 - WORDS SEPARATOR '#'

w_fle=open("Python.txt","w")
w_fle.write('''This is Data File Handling. Two Data Files are Text File and Binary File.''')
w_fle.flush()
with open("Python.txt","r") as r_fle:
    sent=r_fle.read()
    print("Original File Content:")
    print(sent)
    print("Words separated by '#':")
    for loop in range(len(sent)):
        if sent[loop].isspace():
            print('#',end='')
        else:
            print(sent[loop],end='')
