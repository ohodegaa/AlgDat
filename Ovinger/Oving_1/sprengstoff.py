__author__ = 'ohodegaa'

from sys import stdin


class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record, largest):
    return search(record.next, record if record.value > largest.value else largest) if record is not None else (largest.value if largest is not None else None)



def main():
    # reading from stdin and creating a linked list
    first = None
    next = None
    for line in stdin:
        if not is_digit(line):
            continue
        penultimate = next
        next = Record(int(line))
        if first is None:
            first = next
        else:
            penultimate.next = next

    # searching and printing out the result
    #print(search(first.next, first))
    print(search(first, first))

def is_digit(test):
    try:
        test = int(test)
    except:
        return False
    return True


if __name__ == "__main__":
    main()



