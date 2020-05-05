import random

# объявили массив и заполнили рандомными значениями от 1 до 99
num = []
for x in range(10):
    # print(x)
    num.append(random.randint(1, 100))


def arrays_sort(nums):
    swapped = True  # что бы хоть раз пройти по циклу
    num_of_iterations = 0
    while swapped:
        swapped = False
        # итерируемся по массиву. Берем длину массива минус 1, так как счет в программировании начинается с 0
        for i in range(len(nums) - num_of_iterations - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # меняем местами
                swapped = True
        num_of_iterations += 1
    return nums


print(arrays_sort(num))  # выводим поулченные результаты в консоль
# print("let's test it")
