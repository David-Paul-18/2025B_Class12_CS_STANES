#Program 8 - REMOVING LINES CONTAINING 'a'

rfile=open("Self_Discovery.txt","r+")
data=rfile.read()
print("The Original File Content:\n\n",data)
print()
with open("Self_Discovery.txt","w+") as wfile:
    for line in data.splitlines():
        if 'a' not in line:
            wfile.write(line)
            wfile.write("\n")
    wfile.seek(0)
    content=wfile.read()
    print("The file content after removing lines containing 'a':\n\n", content)
