'''使用heapq库排序和filter查询'''

#输出list中最小或者最大的几位
import heapq

nums = [10,2,9,100,80]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

students = [{'name':'aaa','score':100,'height':189},
            {'name':'bbb','score':56,'height':169},
            {'name':'ccc','score':98,'height':182}]
print(heapq.nsmallest(2,students,key = lambda x:x['height']))

#查询
#查询列表中是否存在某个字段
list1 = ['to_pickle','to_records','to_sparse','update']
print(list(filter(lambda x:x.startswith('update'),list1)))

#列表中是字典
list2 = [dict(zip('ab',range(2))),dict(zip('cd',range(4)))]
print(list2)
print(list(filter(lambda x:'b' in x.keys(),list2)))

#正则表达式匹配字段
import re
print(list(filter(lambda x:re.findall(u'(to_)',x),list1)))


