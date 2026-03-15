import sys
nums = [int(line) for line in open(sys.argv[1]) if line.strip()]
nums.sort()
m = nums[len(nums) // 2]
moves = sum(abs(num - m) for num in nums)
if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
