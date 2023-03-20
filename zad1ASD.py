import time

def main():
    sorted_tables = []
    unsorted_tables = []
    num_of_elements = 2000

    while (num_of_elements <= 32000):
        sorted_tables.append(generate_sorted_table(num_of_elements))
        unsorted_tables.append(generate_unsorted_table(num_of_elements))

        num_of_elements = num_of_elements * 2

    print("Complexity for sorted tables:")
    check_complexity(sorted_tables, True)
    print("\nComplexity for unsorted tables:")
    check_complexity(unsorted_tables, False)


def check_complexity(tables, tables_are_sorted):
    for table in tables:
        start_of_sorting = time.time()
        
        sorted_succesfully = sort_table(table)

        if (sorted_succesfully):
            end_of_sorting = time.time()
            time_of_sorting_in_s = end_of_sorting - start_of_sorting

            if (tables_are_sorted):
                n = len(table)
            else:
                n = len(table) ** 2
            
            ratio = n / time_of_sorting_in_s

            print(ratio)


def generate_sorted_table(num_of_elements):
    sorted_table = []
    
    for i in range (1, num_of_elements + 1):
        sorted_table.append(i)
    
    return sorted_table


def generate_unsorted_table(num_of_elements):
    unsorted_table = []
    
    while num_of_elements > 0:
        unsorted_table.append(num_of_elements)

        num_of_elements -= 1
    
    return unsorted_table


def sort_table(table):
    sorting_complete = False

    for j in range(0, len(table)):
        key = table[j]
        i = j - 1

        while i >= 0 and table[i] > key:
            table[i + 1] = table[i]
            i = i - 1
        
        table[i + 1] = key 
    
    sorting_complete = True

    return sorting_complete


main()