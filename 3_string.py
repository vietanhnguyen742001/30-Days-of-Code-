my_str = "hello"
print(my_str)
print(type(my_str))

# Chiều dài str len()
print(len(my_str))   

# Truy cập đến kí tự => index
# index dương: 0 => len(str)-1
print(my_str[0])
print(my_str[1])
print(my_str[4])

# Slicing for string 
print(my_str[1:4]) # indices: 1,2,3 ( sẽ không lấy 0 và 4)
print(my_str[1:]) # indices: 1,2,3 ( sẽ không lấy 0 )
print(my_str[:-1]) # indices: 1,2,3 ( sẽ không lấy 0 )


