p = "24 pt pT"
print(p.upper())
print(p.lower())
print(p.replace("pt","ne"))
print(p.lower().replace("pt","ne"))
index = p.index("p")
print(index)
index = p.index("p",index+1)
print("index2: ", index)
print("find: ",p.find("p"))

# find는 없을 경우 -1 반환
# index는 없을 경우 Error 발생

print("count: " , p.count("p"))