#sample list sample list of customer id's 
customer_ids_input = input("Enter customer IDs separated by space: ")
customer_ids = [int(x) for x in customer_ids_input.split()]


#linear search 

def linear_search(customer_list, target_id):
    for i in range (len(customer_list)):
        if customer_list[i] == target_id:
            return i
    return -1


#Binary search 

def binary_search(sorted_list, target_id):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target_id:
            return mid
        elif sorted_list[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#testing the search functions

search_id = int(input("Enter the customer id to search: "))

#linear search

found_linear = linear_search(customer_ids, search_id)
if found_linear != -1:
    print(f"Linear search: Found at index {found_linear}")
else:
    print("Linear Search: Not Found")


#binary search(requires sorted list)
sorted_ids = sorted(customer_ids)
found_binary = binary_search(sorted_ids, search_id)
if found_binary != -1:
    print(f"Binary search: Found at sorted index {found_binary}")
else:
    print("Binary Search: Not Found")


#output :

# (base) cg@cg-ThinkCentre-neo-50s-Gen-3:~/arnv$ /usr/bin/python3 /home/cg/arnv/customer_search.py
# Enter customer IDs separated by space: 22 23 24 55 45 12 1 3243 12 
# Enter the customer id to search: 22 
# Linear search: Found at index 0
# Binary search: Found at sorted index 3
# (base) cg@cg-ThinkCentre-neo-50s-Gen-3:~/arnv$ /usr/bin/python3 /home/cg/arnv/customer_search.py
# Enter customer IDs separated by space: 23 22 55 66 77
# Enter the customer id to search: 22
# Linear search: Found at index 1
# Binary search: Found at sorted index 0
# (base) cg@cg-ThinkCentre-neo-50s-Gen-3:~/arnv$ 