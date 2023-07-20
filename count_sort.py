def count_sort(nums_array: list) -> list:
    max_element = max(nums_array)
    count_array = [0] * (max_element + 1)
    for num in nums_array:
        count_array[num] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(nums_array)
    for num in nums_array:
        output_array[count_array[num] - 1] = num
        count_array[num] -= 1

    return output_array


if __name__ == "__main__":
    try:
        num_array = list(map(int, input("Enter only integers separated by space : ").split()))
        print("The array after sorting is:", count_sort(num_array))
    except ValueError:
        print("Invalid Input, Please enter only integers")
