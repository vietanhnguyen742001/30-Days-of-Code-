# Methods of list
# 1. add list element (1 element) .append()
my_lst = [1, 3, 6, 10, -5]
my_lst.append(50)
print(my_lst)
# 2. add elements .extend()
my_lst = [1, 3, 6, 10, -5]
lst_1 = ["anh", "em"]
my_lst.extend(lst_1) 
print(my_lst)
# 3. sort list .sort() or sorted()
my_lst = [1, 3, 6, 10, -5]
my_lst.sort()
print(my_lst) 

new_lst = sorted(my_lst)
print(new_lst) 
# 4. reverse list
my_lst = [1, 3, 6, 10, -5]
my_lst.sort(reverse = True)
print(my_lst) 

my_lst = [1, 3, 6, 10, -5]
my_lst.reverse()
print(my_lst) 

my_lst = [1, 3, 6, 10, -5]
new_lst = my_lst[::-1] # start: stop : step
print(new_lst)

# 5. insert element .insert(index, value)
my_lst = [1, 3, 6, 10, -5]
my_lst.insert(1,100)
print(my_lst)
# 6. delete element del or .remove(ele)
my_lst = [1, 3 ,6, 10, -5]
del my_lst[2]
print(my_lst)

# 7. trả về index đầu tiên của element được khớp .index() (ko có error)
my_lst = [1, 3, 6, 10, -5]
ind = my_lst.index(10)
print(ind)

# 8. pop(index) ko truyền xóa ele cuối
my_lst = [1, 3, 6, 10, -5]
ele = my_lst.pop(3)
print(ele)
print(my_lst)