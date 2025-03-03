# Tuple trong Python 
# 1. Tạo tuple 
tuple_1 = ("a", 3)
print(tuple_1)
print(type(tuple_1))

tuple_1 = ("a",) # nhớ 1 phần tử thì thêm dấu phẩy ,
print(tuple_1)
print(type(tuple_1))

# Duyệt qua các phần tử của tuple 
tuple_1 = ("a", 3 , 4 , "b")
print(f"Chiều dài của tuple: {len(tuple_1)}")

for item in tuple_1:
    print(item)

print(tuple_1[1])

# 3. Cộng các tuples
tuple_1 = ("a", 3 , 4 , "b")
tuple_2 = ("a32", 30 , 4 , "b")

new_tuple = tuple_1 + tuple_2
print(f"New tuple: {new_tuple}")

tuple_1 = ("a", 3 , 4 , "b")
list_1 = list(tuple_1)
list_1.append("hello")
new_tuple_1 = tuple(list_1)
print(f" new_tuple: {new_tuple_1}")

# xoá phần tử 
tuple_1 = ("a", 3 , 4 , "b")
list_1 = list(tuple_1)
list_1.remove(4)
new_tuple_2 = tuple(list_1)
print(f" new_tuple: {new_tuple_2}")

tuple_1  = ("a", 3, 4 , "b", "a")

print(tuple_1.count(4))
print(tuple_1.index("b"))

tuple_1  = ("a", 3, 4 , "b", "a")
tuple_2  = ("a", 3, 4 , "b", "a")

print("ID of tuple_1: {id(tuple_1)}")
print("ID of tuple_2: {id(tuple_2)}")
