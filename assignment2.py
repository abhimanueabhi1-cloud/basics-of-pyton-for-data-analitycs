agelist=[24,25,26,27,28]
namelist=['abhi','mirek','vipi','praveen','kasia']
namelist.append ('yazhini')
print (namelist)
agelist.insert(2, 30) 
print(agelist)
namelist.remove('yazhini')
agelist.pop()
print(agelist)
agelist.extend([29,30,26])
print (agelist)
agelist.sort(reverse=True)
print (agelist)
print(min(agelist))
print(max(agelist))
print(sum(agelist))
print(namelist[1])
print(namelist[-1])
print(namelist[2:4])
print(namelist[::-1])
studentmark = {'abhi': 99, 'mirek': 97, 'vipi': 98, 'praveen': 99, 'kasia': 99}
print(studentmark)
print(studentmark['abhi'])
print(studentmark['kasia'])
studentmark['janvi']=80
studentmark.update({'abhi':82})
print(studentmark)
print(studentmark.keys())
print(studentmark.values())
print(studentmark.items())
myset={'a','e','i','o','u','a','a','i'}
print(myset)
myset.add('s')
print(myset)
set1={1, 3, 5, 7, 9}
set2={2, 3, 5, 8, 10}
print(set1.union(set2))
print(set1.intersection(set2))
score = int(input("Enter your score (0 to 10): "))
if score > 7 and score <= 10:
    print('above_avg')
elif score >= 4 and score <= 7:
    print('avgg')
else:
    print('belowavg')
    score = int(input("Enter your score (0 to 10): "))

if 0 <= score <= 10:
    if score > 7:
        print("Performance_Category:Above Average")
        print("Excellent_work_Keepitup.")
    elif 4 <= score <= 7:
        print("Performance_Category: Average")
else:
    print("Need to Improve your performance, consistent practice will lead to better results")
