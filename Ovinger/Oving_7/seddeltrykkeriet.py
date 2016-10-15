__author__ = 'ohodegaa'
#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    # SKRIV DIN KODE HER
    return max_value_greedy(widths, heights, values, paper_width, paper_height)

def max_value_greedy(widths, heights, values, paper_width, paper_height):
    pass

def max_value_dynamic(widths, heights, values, paper_width, paper_height):
    max_value = 0

    # 2-D array representing the whole sheet [width][height]
    result = [None]*paper_width
    for i in range(len(result)):
        result[i] = [-1]*paper_height





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