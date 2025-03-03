# nối chuỗi 
str_1 = "anh "
str_2 = "yeu em"
concat_str = str_1 + str_2
print(concat_str)

# Duyệt qua các kí tự trong string 
my_str = "hello"

for ch in my_str:
    print(ch)

# kiểm tra chuỗi con có nằm trong chuỗi không?
my_str = "hello anh em "
if " anh " in my_str:
    print("ok")
else : 
    print("No")

# Methods 
my_str = "hello anh em "
print(my_str.upper()) # in hoa 
print(my_str.lower())   # in thuong

# string is immutable in python 
my_str = "hello anh em "
#my_str[1] "E"
my_str= "hEllo anh em "
print(my_str)