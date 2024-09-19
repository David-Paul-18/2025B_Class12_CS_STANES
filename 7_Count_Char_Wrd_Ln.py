#Program 7 - COUNTING CHARACTERS, WORDS AND LINES

file=open("Quotes.txt","w+")
file.write('''1. A state of mind that sees God in everything is evidence of growth in grace and a thankful heart.
2. What comes into our minds when we think about God is the most important thing about us.
3. God never hurries. There are no deadlines against which he must work.
Only to know this is to quiet our spirits and relax our nerves.
4. It is doubtful whether God can bless a man greatly until He has hurt him deeply.
5. The reason why many are still troubled, still seeking, still making little forward progress is because
they haven't yet come to the end of themselves.
We're still trying to give orders, and interfering with God's work within us.''')

file.seek(0)
data=file.read()
num_of_char=len(data)
num_of_words=len(data.split())
num_of_lines=len(data.splitlines())
print("Number of characters is:",num_of_char)
print("Number of words is:",num_of_words)
print("Number of lines is:",num_of_lines)
file.close()
