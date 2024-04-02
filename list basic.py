university = ["su" , "du","nsu"]

print(university)
print(university[:])
print(university[2])
print(university[0:2])

print("Total length : " , len(university))

university[1] = "BUBT"
print(university)
university.insert(1,"BUET")
print(university)
university.append("DIU")
print(university)

print(type(university))

num = [1, 2,3]
university.extend(num)

print(university)

