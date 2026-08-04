salaries = [32000, 29000, 48000, 12000, 67000, 50000]

def bubble_sort(salaries):
    n = len(salaries)

    for i in range(n):

        for j in range(0,n - i -1):
            
            if salaries[j] > salaries[j+1]:
                #swap the elements 
                salaries[j], salaries[j+1] = salaries[j+1], salaries[j]

    return salaries

def selection_sort(salaries):
    n = len(salaries)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j

        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]

    return salaries



bubble_sorted = bubble_sort(salaries.copy())
selection_sorted = selection_sort(salaries.copy())


print("Bubble Sort (Ascending):")
print(bubble_sorted)

print("\nSelection Sort (Ascending):")
print(selection_sorted)

print("\nTop 5 Highest Salaries:")
print(selection_sorted[-5:][::-1])