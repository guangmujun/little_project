'''带条件的推导列表'''

print([x for x in range(10) if x%2 == 0])

print([x for x in range(30) if x%2 == 0 and x%6 == 0])

print([x+1 if x>=5 else x*10 for x in range(10)])

#嵌套推导列表
list_of_list=[[1,2,3],[4,5,6],[7,8]]
print([y for x in list_of_list for y in x])
