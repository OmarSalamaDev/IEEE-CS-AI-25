

# that takes list from user
def get_numbers():
    nums = list(map(int, input().split(", ")))
    nums.sort()
    print(nums)
    return nums


# returns min
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


# returns max 
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# returns mean
def find_mean(numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    return num_sum / len(numbers)


# returns mode
def find_mode(numbers):
    occurences = {}
    mode = []
    for num in numbers:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1
    max_occurences = 0
    for num in occurences:
        if occurences[num] > max_occurences:
            mode = [num]
            max_occurences = occurences[num]
        elif occurences[num] == max_occurences:
            mode.append(num)
    return mode


# returns median 
def find_median(numbers):
    if len(numbers) % 2 == 0:
        mid = len(numbers) // 2
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[len(numbers) // 2]
    

# Returns range
def find_range(numbers):
    return max(numbers) - min(numbers)


# Returns variance
def find_variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


# Returns standard deviation
def find_STD(numbers):
    return find_variance(numbers) ** 0.5


# Returns Q1, Q2, Q3
def find_Quartiles(numbers):
    
    n = len(numbers)

    Q2 = find_median(numbers)

    lower_half = numbers[:n//2]
    if len(lower_half) % 2 == 0:
        Q1 = (lower_half[len(lower_half)//2 - 1] + lower_half[len(lower_half)//2]) / 2
    else:
        Q1 = lower_half[len(lower_half)//2]

    upper_half = numbers[(n+1)//2:]
    if len(upper_half) % 2 == 0:
        Q3 = (upper_half[len(upper_half)//2 - 1] + upper_half[len(upper_half)//2]) / 2
    else:
        Q3 = upper_half[len(upper_half)//2]

    return Q1, Q2, Q3


# Returns Interquartile range
def find_IQR(numbers):
    Q1, _, Q3 = find_Quartiles(numbers)
    return Q3 - Q1


nums = get_numbers()
print(find_min(nums))
print(find_max(nums))
print(find_mean(nums))
print(find_mode(nums))
print(find_median(nums))
print(find_range(nums))
print(find_variance(nums))
print(find_STD(nums))
print(find_Quartiles(nums))
print(find_IQR(nums))