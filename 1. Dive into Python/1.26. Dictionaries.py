db = dict()
for i in range(3):
    id = int(input()); mt = float(input()); f = float(input())
    db[id] = (mt, f)
id = int(input())
(mt,f)=db[id]
print("%.1f" % ((mt+f)/2))
print(db)