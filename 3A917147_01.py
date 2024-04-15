def get_even_squares(num_list):
    return [num ** 2 for num in num_list if num % 2 == 0]


def get_odd_cubes(num_list):
    return [num ** 3 for num in num_list if num % 2 != 0]


def get_sliced_list(num_list):
    return num_list[4:]


def format_numbers(numbers):
    return [f'{num:8}' for num in numbers]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    even_sqs = get_even_squares(nums)
    odd_cbs = get_odd_cubes(nums)
    sliced_lst = get_sliced_list(nums)

    formatted_even_sqs = format_numbers(even_sqs)
    formatted_odd_cbs = format_numbers(odd_cbs)
    formatted_sliced_lst = format_numbers(sliced_lst)

    print(', '.join(formatted_even_sqs))
    print(', '.join(formatted_odd_cbs))
    print(', '.join(formatted_sliced_lst))
