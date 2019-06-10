a = "Shut up you fool"

print(a[3])
print(a[5:11])
print(a[:11])
print(a[5:])
print("\n")

b = "   Kya h be tujhe   "
c = "yyyyyy yo yyyy"

print(end=str(len(a)))
print("   ", end=str(len(b)))
print("\n")

print(b.strip())
print(b.lstrip())
print(b.rstrip())
print(c.strip("y"))
print("\n")

print(a.lower())
print(a.upper())
print("\n")

print(a.replace("S", "K"))
print(a.replace("Shut", "Zip"))
print(a.replace("u", "i"))
print(a.replace("u", "i", 2))
print(a.replace(a[2], "i"))
print(a.replace(a[2], a[3]))
print("\n")

print(a.split())
print(a.split("u"))
print(a.rsplit("u"))
print(a.split("u", 2))
print(a.rsplit("u", 2))
print(a.split("u", 0))
print("\n")

d = "Shutupyoufool"
e = "1Shutupyoufool"
f = "Hello!\nAre you #1?"

print(a.isalpha())
print(d.isalpha())
print(a.isalnum())
print(d.isalnum())
print(e.isidentifier())
print(d.isidentifier())
print(f.isprintable())
print(e.isprintable())
print("\n")

print(d.center(20))
print(d.center(20, "_"))
print("\n")

g = "shut up you fool"
h = "    shut up you fool     "

print(g.capitalize())
print(h.capitalize())
print("\n")

print(g.count("u"))
print(g.count("u", 2, 5))
print(g.count("u", 2, 6))
print("\n")

print(g.find("up", 2, 7))
print(g.rfind("up", 2, 10))     # Searches from end to front but prints the index from front
print(g.find("your"))
print(g.rfind("your"))
print("\n")

print(g.index("up", 2, 7))
print(g.rindex("up", 2, 10))    # Searches from end to front but prints the index from front
# print(g.index("your"))    # prints an exception - substring not found
# print(g.rindex("your"))   # prints an exception - substring not found
print("\n")

i = "shut up"
j = "_"
k = "__"

print(j.join(i))
print("+".join(i))
print("+".join(j))
print("+".join(k))
print("\n")

print(a.partition("u"))
print(a.rpartition("u"))
print(a.partition("i"))
print(a.rpartition("i"))
print("\n")
