"""
Your module description
"""
array = [10,9,8,7,6,5,4,3,2,1,0]
length = len(array)
index = 0

def getArrayValue(array, length, index):
    try:
        value = 0
        if index >=0 and index < length:
            value = array[index]
            print("Value is: %s" % array[index])
    except IndexError:
        value = 'null'
        print('Index does not exist')
    return value

getArrayValue(array,length,300)
getArrayValue(array,length,2)
        
        