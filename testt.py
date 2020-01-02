tag1 = {'domain': ['domain', 'gender', 'age'],
        'gender': ['domain', 'gender', 'age'],
        'age': ['domain', 'gender', 'age']}
tags=[]
# tags=[(tag, label)for tag, label in tag1]
for tag,label in tag1.items():
    # print(item)
    tags.append((tag, label))
print(tags)