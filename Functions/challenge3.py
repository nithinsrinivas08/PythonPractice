def sum_numbers(*num: float) -> float :
    """ calculates the sum of all the numbers passed as arguments """
    ans = 0
    for i in num:
        ans += i
    return ans

print(sum_numbers(1,2,3))