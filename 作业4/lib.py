from typing import Sequence

def square_sum(nums: Sequence[int]) -> int:
    result = 0
    for i in range(len(nums)):
        n = nums[i]
        result += n*n

    return result