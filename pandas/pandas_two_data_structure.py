import pandas

num = [5,4,3,2,1,0]

ser = pandas.Series(data=num)
print(ser[0])
print(ser)

data = {
    '1':[1,2,3],
    '2':[4,5,6],
    '3':[7,8,9],
    '4':[1,2,3],
    '5':[4,5,6],
    '6':[7,8,9]
}
# dataFrame =pandas.DataFrame(data=data,index=[0,1,2,3,4,5],columns=['a','b','c','d','e','f'],dtype=int8)
dataFrame =pandas.DataFrame(data=data)
dataFrame['a'] = [1,2,3]
new = dataFrame.drop(['a'],axis=1)
print(dataFrame)
print(new)