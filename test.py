string = "240*480~iuaFSHISAFIUAHSFIABSIFdsong"

h = int(string[:string.index('*')])
w = int(string[string.index('*')+1:string.index('~')])

print(h)
print(w)

string = string[string.index('~')+1:]
print(string)