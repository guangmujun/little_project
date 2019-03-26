'''简洁的表达式'''

#快速构建字典
dict1 = dict(zip('abcd',range(4)))
print(dict1)

#更新字典
options = {'code':'utf-8'}
dict1.update(options)
print(dict1)

#return结合条件判断
def test(m):
    return 'a' if m==1 else 'b'
print(test(1))
print(test(2))

#推导列表生成字典
list1 = ((1,'a'),(2,'b'))
print({x[0]:x[1] for x in list1})
print({x:y for x in range(4) for y in range(10)})