"""
python List

Sum of elements: Write a function that takes a list of numbers
as input and returns the sum of all the elements in the list.

input_List: [1,8,3,2] -> 14

Edge cases: the difference input like ([] , [string] , [int] , [undefined]) whatever...

Algorithm:
  - current_sum = 0 
  - Iterate over the items of list
  - In each iteration, add the current_element to the res
  -Once the loop is finished return res
"""


def sum_elements(input_list):
    res = 0

    for num in input_list: #time complexity : O(n)
        res += num

    return res    

# print(sum_elements([1,8,2,3]))

"""
Taking a list as an input -> return the largest value
"""

#Argument

#Dynamically and statically typed languages like Python is Dynamic 
 
def largest_value(input_list):
    largest_value = ""
    for i in input_list: # time complexity O(n)
        if(len(i) < len(largest_value)):
            continue
        if(len(i) > len(largest_value)):
            largest_value = i
    return largest_value   

print(largest_value(["hassan", "nermin","mahomoud" ,"ismailAdawieh"]))

# class TestSolution(unittest.testCase):
#     def test_func(self):
#         self.assertEqual(largest_value(["hassan", "nermin","mahmoud" , "ismailAdawieh"]), "ismailAdawieh")


# run the unit test command : python -m unittest [file name].[class name]
        

"""
  - We have two list
  - Check if there is a common element between them
"""

def have_common_element(list1 , list2): # time complexity is O(n)
    store_list = set(list2) # in this case you can get any element in the list O(1)
    for num1 in list1:
        for num1 in store_list:
                return True
    return False        

print(have_common_element([2,3,0,4,5,6],[1,7,8,9,0]))            

