__author__ = 'ohodegaa'
#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    # SKRIV DIN KODE HER

    # c 2-D - array
    # accessing table with c[width][height] according to coordinate system
    c = [[]] * (paper_width + 1)
    for i in range(paper_width + 1):
        c[i] = [-1]*(paper_height + 1)

    # zeroing out width=0 and height=0
    for i in range(len(c)):
        c[i][0] = 0
    for j in range(len(c[0])):
        c[0][j] = 0

    # zeroing out the less-than-minimum-sized note. No note will be smaller than min_size
    min_size = minimum_size(widths, heights)
    for i in range(1, min_size):
        # rows:
        for r in range(1, paper_width + 1):
            c[r][i] = 0
        for s in range(1, paper_height + 1):
            c[i][s] = 0

    # putting in values for the notes, if smaller notes fits "inside" a note, decomp_note() will handle this
    for i in range(len(values)):
        decomped = decomp_note(widths, heights, values, i)
        if widths[i] <= paper_width and heights[i] <= paper_height and c[widths[i]][heights[i]] < values[i]:
            c[widths[i]][heights[i]] = max(values[i], decomped)
        if widths[i] <= paper_height and heights[i] <= paper_width and c[heights[i]][widths[i]] < values[i]:
            c[heights[i]][widths[i]] = max(values[i], decomped)

    max_value_dynamic(c, widths, heights, values, paper_width, paper_height)
    #show_table(c)
    return c[paper_width][paper_height]

def decomp_note(widths, heights, values, i):
    w = widths[i]
    h = heights[i]
    v = values[i]
    max_value = -1
    for j in range(len(values)):
        if widths[j] < w and heights[j] < h:
            max_value = max(max_value, max((widths[j]//w), (heights[j]//h))*values[j])
        if widths[j] < h and heights[j] < w:
            max_value = max(max_value, max((widths[j]//h), (heights[j]//w))*values[j])

    return max_value

def minimum_size(widths, heights):
    min_size = 10**6
    for i in range(len(widths)):
        if widths[i] < min_size:
            min_size = widths[i]
        if heights[i] < min_size:
            min_size = heights[i]
    return min_size


def max_value_dynamic(c, widths, heights, values, paper_width, paper_height):
    if paper_height <= 0 or paper_width <= 0:
        return 0
    elif c[paper_width][paper_height] >= 0:
        return c[paper_width][paper_height]

    else:
        for i in range(len(values)):
            if widths[i] > paper_width or heights[i] > paper_height:
                continue

            else:
                max_upper = max_value_dynamic(c, widths, heights, values, paper_width - widths[i], heights[i])
                #print("max_upper ", max_upper)
                max_lower = max_value_dynamic(c, widths, heights, values, paper_width, paper_height - heights[i])
                #print("max_lower ", max_lower)
                max_right = max_value_dynamic(c, widths, heights, values, paper_width - widths[i], paper_height)
                #print("max_right ", max_right)
                max_left = max_value_dynamic(c, widths, heights, values, widths[i], paper_height - heights[i])
                #print("max_left", max_left)

                c[paper_width][paper_height] = max(c[paper_width][paper_height],
                                                   values[i] + max_upper + max_lower,
                                                   values[i] + max_right + max_left)
        return c[paper_width][paper_height]

def show_table(c):
    for i in range(len(c[0])):
        for j in range(len(c)):
            print(c[j][i], end="\t")
        print()


def main():
    widths = []
    heights = []
    values = []
    #stdin = open("input_eksempel_01", "r+")
    for triple in stdin.readline().split():
        if len(triple) > 0:
            dim_value = triple.split(':', 1)
            dim = dim_value[0].split('x', 1)
            width = int(dim[0][1:])
            height = int(dim[1][:-1])
            value = int(dim_value[1])
            widths.append(int(width))
            heights.append(int(height))
            values.append(int(value))
    for line in stdin:
        if len(line) > 0:
            paper_width, paper_height = [int(x) for x in line.split('x', 1)]
            print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()