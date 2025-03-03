# Định nghĩa 
# Khởi tạo dictionary 
name_age = {"Min": 5, "Na": 6, "Bống" : 10} # Min, Na, Bống là key , còn 5,6,10 là value
# Tạo dictionary rỗng 
# name_age = dict()
# name_age = {}
# Truy cập 
print(name_age["Na"])

name_age = {"Min": 5, "Na": 6, "Bống" : 10} # Min, Na, Bống là key , còn 5,6,10 là value
name_age["Bống"]=12
print(name_age)

name_age = {"Min": 5, "Na": 6, "Bống" : 10} # Min, Na, Bống là key , còn 5,6,10 là value
name_age["Nam"]=30
print(name_age)

# Duyệt qua các phần tử dictionary 
# keys 
name_age = {"Min": 5, "Na": 6, "Bống" : 10} # Min, Na, Bống là key , còn 5,6,10 là value
for k in name_age:
    print(k)
for k in name_age.keys():
    print(k)

for k in name_age.values():
    print(k)

name_age = {"Min": 5, "Na": 6, "Bống" : 10} # Min, Na, Bống là key , còn 5,6,10 là value
for k,v in name_age.items():
    print(k,v)
