__author__ = 'ohodegaa'
#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    # SKRIV DIN KODE HER

    # result 2-D - array
    # accessing table with result[width][height] according to coordinate system
    result = [[]] * (paper_width + 1)
    for i in range(paper_width + 1):
        result[i] = [-1]*(paper_height + 1)

    # zeroing out width=0 and height=0
    for i in range(len(result)):
        result[i][0] = 0
    for j in range(len(result[0])):
        result[0][j] = 0

    # zeroing out the less-than-minimum-sized note. No note will be smaller than min_size
    min_size = minimum_size(widths, heights)
    for i in range(1, min_size):
        # rows:
        for r in range(1, paper_width + 1):
            result[r][i] = 0
        for c in range(1, paper_height + 1):
            result[i][c] = 0

    return max_value_dynamic(widths, heights, values, paper_width, paper_height)


def minimum_size(widths, heights):
    min_size = 10**6
    for i in range(len(widths)):
        if widths[i] < min_size:
            min_size = widths[i]
        if heights[i] < min_size:
            min_size = heights[i]
    return min_size


def max_value_greedy(widths, heights, values, paper_width, paper_height):
    pass


def max_value_dynamic(widths, heights, values, paper_width, paper_height):
    max_value = 0

    # 2-D array representing the whole sheet [width][height]
    pass

def show_table(c):
    for i in range(len(c[0])):
        for j in range(len(c)):
            print(c[j][i], end="\t")
        print()


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()