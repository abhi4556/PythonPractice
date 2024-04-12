def liner_search():
    list1 = [2,1,4,6,23,6,83]
    index = 0
    for num in list1:
        if(num == 23):
            print("Numbre found: {} and is at index: {}".format(num,index))
        else:
            index = index + 1
            
def binary_search():
    ''' Binary search works only on sorted list'''
    num_list = [2,1,4,6,5,8,12,71,45,32]
    num = 12
    num_list.sort() # Sort function modify the existing list
    print(num_list)
    low = 0
    high = len(num_list) - 1
    while(low < high):
        mid = int((low+high)/2)
        print("Mid value is {}".format(mid))
        if (num == num_list[mid]):
            print("Number found{} at index {}".format(num,mid))
            return
        elif num < num_list[mid]:
            high = mid - 1
        elif num > num_list[mid]:
            low = mid + 1
    return -1
    
binary_search()
    
        
