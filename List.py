'''List
List is used to store multiple values.
These can be of any type
List items are ordered, mutable and allow duplicates
operatons in List are append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort, min, max,etc..,'''

#List
nums = [10, 5, 55, 90, 30, 91]
print(nums)

#add the element at last
nums.append(22)
print(nums)

#insert the element at a specified position
nums.insert(4,66)
print(nums)

#deleting multiple values
del nums[0:5]
print(nums)

#adding multiple values
nums.extend([11,22,33])
print(nums)

#minimum and maximum values and sum
print(min(nums))
print(max(nums))
print(sum(nums))

#sorting the list
nums.sort()
print(nums)
