def myfun(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            new_numbers = new_numbers + [numbers[i]]
    return new_numbers

def max_num(mylst):
    max_num=mylst[0]
    for i in range(len(mylst)):
        if mylst[i]> max_num:
            max_num=mylst[i]
    return max_num
