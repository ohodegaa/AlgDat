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
    min_size = min([min(widths), min(heights)])
    for i in range(1, min_size):
        # rows:
        for r in range(1, paper_width + 1):
            c[r][i] = 0
        for s in range(1, paper_height + 1):
            c[i][s] = 0

    # putting in values for the notes, if smaller notes fits "inside" a note, decomp_note() will handle this
    for i in range(len(values)):
        if widths[i] <= paper_width and heights[i] <= paper_height and c[widths[i]][heights[i]] < values[i]:
            c[widths[i]][heights[i]] = values[i]
        if widths[i] <= paper_height and heights[i] <= paper_width and c[heights[i]][widths[i]] < values[i]:
            c[heights[i]][widths[i]] = values[i]

    #show_table(c)
    max_value = max_value_top_down(c, widths, heights, values, paper_width, paper_height, min_size)
    #show_table(c)
    return max_value


def max_value_bottom_up(c, widths, heights, values, paper_width, paper_height, min_size):





def max_value_top_down(c, widths, heights, values, paper_width, paper_height, min_size):
    if paper_height < 0 or paper_width < 0:
        return 0
    elif c[paper_width][paper_height] > min_size:
        return c[paper_width][paper_height]

    else:
        for i in range(len(values)):
            if widths[i] > paper_width or heights[i] > paper_height:
                continue

            else:
                max_upper_a = max_value_top_down(c, widths, heights, values, paper_width - widths[i], heights[i], min_size)

                max_lower_a = max_value_top_down(c, widths, heights, values, paper_width, paper_height - heights[i], min_size)

                max_right_a = max_value_top_down(c, widths, heights, values, paper_width - widths[i], paper_height, min_size)

                max_left_a = max_value_top_down(c, widths, heights, values, widths[i], paper_height - heights[i], min_size)

                c[paper_width][paper_height] = max(c[paper_width][paper_height],
                                                   values[i] + max_upper_a + max_lower_a,
                                                   values[i] + max_right_a + max_left_a)

        for j in range(len(values)):
            if widths[j] > paper_height or heights[j] > paper_width:
                continue
            else:
                max_upper_b = max_value_top_down(c, widths, heights, values, paper_width - heights[j], widths[j], min_size)

                max_lower_b = max_value_top_down(c, widths, heights, values, paper_width, paper_height - widths[j], min_size)

                max_right_b = max_value_top_down(c, widths, heights, values, paper_width - heights[j], paper_height, min_size)

                max_left_b = max_value_top_down(c, widths, heights, values, heights[j], paper_height - widths[j], min_size)

                c[paper_width][paper_height] = max(c[paper_width][paper_height],
                                                   values[j] + max_upper_b + max_lower_b,
                                                   values[j] + max_right_b + max_left_b)
        if c[paper_width][paper_height] < 0:
            c[paper_width][paper_height] = 0
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
    stdin = open("input_eksempel_02.txt", "r+")
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
        if len(line.strip()) <=0:
            break
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()