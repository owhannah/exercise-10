# Create a new list from two list using the following condition

# Write a program to create a new list such that the new list should contain 
# odd numbers from the first list
# and even numbers from the second list

def create_new_list(list1, list2):
   result = []
   for number in list1 + list2:
       if number % 2 == 0:
           if number in list2:
               result.append(number)
       else:
           if number in list1:
               result.append(number)

   return result

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result = create_new_list(list1, list2)
print("Result list:", result)

