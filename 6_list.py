# tạo list trống 
# empty_lst = list ()
# print(empty_lst)

my_lst = [12 , 3.5 ,"string", [5, 7]]
print(len(my_lst))

#index dương
print(my_lst[1])
#index âm
print(my_lst[-1])

my_lst = [12 , 3.5 ,"string", [5, 7]]
print(my_lst[1:]) # lấy phần tử thứ 2 đến phần tử cuối cùng 
print(my_lst[:-1]) # lấy phần tử đâu tiên đến phần tử -2  

for x in my_lst:
    print(x)

lst_1 = [1, 4.5 , 10 ]
lst_2 = ["anh", "em" ]
concat_lst = lst_1 + lst_2

print(concat_lst)


lst_1 = [1, 4.5 , 10 ]
lst_1[1] = "anh"

print(lst_1)