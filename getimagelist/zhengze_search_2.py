import  re

print(re.search(r"c(f|e)", 'cccef'))
print(re.search(r'^fishC', 'fishCawa'))
print(re.search(r'fishC$', 'awfawfishC'))

print(re.findall(r'[a-z]', 'aegaeg3ageea3'))
print(re.findall(r'[^a-z]', 'EAGAEgegeEg'))

print(re.search(r'(FishC){1,43}', 'FishCFishCFishCwafw'))

# 非贪婪模式
s = "<html><title>this is python learn</title></html>"
print(re.findall(r'<.+?>', s))
print(re.search(r'<.+>', s))