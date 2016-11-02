__author__ = 'ohodegaa'


from sys import stdin


def sort_list(A):
    sorter = MergeSort()
    sorter.sort(A, 0, len(A) - 1)
    return A


class MergeSort:

    def sort(self, my_list, start, end):
        if start < end:
            mid = (start + end)//2
            self.sort(my_list, start, mid)
            self.sort(my_list, mid+1, end)
            self.merge(my_list, start, mid + 1, end)


    def merge(self, my_list, start, mid, end):
        left = my_list[start:mid] + [float('inf')]
        right = my_list[mid:end+1] + [float('inf')]
        j = 0
        k = 0
        for i in range(start,end+1):
            if left[j] <= right[k]:
                my_list[i] = left[j]
                j += 1
            else:
                my_list[i] = right[k]
                k += 1


class QuickSort:

    def sort(self, my_list,start, i_pivot):
        if start < i_pivot:
            new_pivot = self.partition(my_list, start, i_pivot)
            self.sort(my_list, start, new_pivot - 1)
            self.sort(my_list, new_pivot + 1, i_pivot)


    def partition(self, my_list, start, i_pivot):
        pivot = my_list[i_pivot]
        i = start
        for j in range(start, i_pivot):
            if my_list[j] <= pivot:
                if i != j:
                    temp = my_list[j]
                    my_list[j] = my_list[i]
                    my_list[i] = temp
                i += 1
        temp = my_list[i_pivot]
        my_list[i_pivot] = my_list[i]
        my_list[i] = temp
        return i


def find_lower(my_list, num):
    start = 0
    end = len(my_list) - 1
    if my_list[start] >= num:
        return my_list[start]

    while True:
        mid = (start + end)//2
        if my_list[mid] == num:
            return my_list[mid]
        else:
            if my_list[start] > num:
                i = start
                while i >= 0:
                    if my_list[i] < num:
                        return my_list[i]
                    i -= 1
            if num < my_list[mid]:
                end = mid - 1
            elif num > my_list[mid]:
                start = mid + 1

    return my_list[start]


def find_upper(my_list, num):
    start = 0
    end = len(my_list) - 1
    if my_list[end] <= num:
        return my_list[end]
    while start <= end + 1:
        mid = (start + end)//2
        if my_list[mid] == num:
            return my_list[mid]
        else:
            if my_list[end] < num:
                i = end
                while i <= len(my_list) - 1:
                    if my_list[i] > num:
                        return my_list[i]
                    i += 1
            elif num < my_list[mid]:
                end = mid - 1
            elif num > my_list[mid]:
                start = mid + 1

    return my_list[end]


def find(my_list, lower, upper):
    low_bound = find_lower(my_list,lower)
    high_bound = find_upper(my_list, upper)
    return [low_bound, high_bound]


def main():
    input_list = []
    #stdin = open("input_eksempel_01.txt", "r+")
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()

