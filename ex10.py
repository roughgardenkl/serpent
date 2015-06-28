tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
Backslash_cat = "I'm \\ a \\ cat." 

fat_cat = """
I'll do a list: 
\t* Cat Food 
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persion_cat
print Backslash_cat
print fat_cat

red_cat = "\'I'm in quotes!\'"
green_cat = "\f What on earth does\nformfeed mean?"

print red_cat
print green_cat

while True: 
	for i in ["/","-","\\","|"]:
		print "%s\r" % i,
