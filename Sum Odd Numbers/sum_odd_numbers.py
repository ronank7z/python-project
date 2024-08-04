def generate_odd_array_with_rows(num_rows):
    result = []
    current = 1  # Start with the first odd number
    for length in range(1, num_rows + 1):
        # Create the next sub-array with 'length' number of odd numbers
        sub_array = [current + 2 * i for i in range(length)]
        result.append(sub_array)
        # Update the current position for the next sub-array
        current += 2 * length
    return result

# Example usage
rows = 41  # Change this to the number of rows you want
array = generate_odd_array_with_rows(rows)
print(sum(array[rows-1]))