nums = [1, 2, 10, 11, 12, 13]
print(nums)       

last = nums.pop()  
print(last)       
print(nums)         

nums = [1, 2, 10, 11, 12]
print(nums)          

first = nums.pop(0)  
print(first)         
print(nums)          

a = [1, 2]
print(a)

a.append(3)
print(a)

a.extend([11, 12, 13])
print(a)

a.extend([14, 15])
print(a)

a = a[:-2]   
print(a)

coins = [1, 2]
print(coins)

coins.insert(1, 10)
print(coins)

coins.append(25)
print(coins)
