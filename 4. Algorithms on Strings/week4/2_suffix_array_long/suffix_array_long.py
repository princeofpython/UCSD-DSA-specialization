# python3
import sys


def sort_characters(text):
    order = [0] * len(text)
    chars={'$':0,'A':1,'C':2,'G':3,'T':4}
    count = [0]*5
    for i in text:
        count[chars[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i, c in reversed(list(enumerate(text))):
        count[chars[c]] -= 1
        order[count[chars[c]]] = i

    return order


def compute_char_classes(text, order):
    classs = [0] * len(text)

    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            classs[order[i]] = classs[order[i - 1]] + 1
        else:
            classs[order[i]] = classs[order[i - 1]]

    return classs


def sort_doubled(text, l, order, classs):
    len_text = len(text)
    count = [0] * len_text
    new_order = [0] * len_text

    for i in range(len_text):
        count[classs[i]] += 1
    for j in range(1, len_text):
        count[j] += count[j - 1]

    for i in range(len_text - 1, -1, -1):
        start = (order[i] - l + len_text) % len_text
        cl = classs[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order


def update_classes(new_order, classs, l):
    n = len(new_order)
    new_classs = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = cur + l, (prev + l) % n
        if classs[cur] != classs[prev] or classs[mid] != classs[mid_prev]:
            new_classs[cur] = new_classs[prev] + 1
        else:
            new_classs[cur] = new_classs[prev]

    return new_classs


def build_suffix_array(text):
    order = sort_characters(text)
    classs = compute_char_classes(text, order)
    length = 1
    len_text = len(text)

    while length < len_text:
        order = sort_doubled(text, length, order, classs)
        classs = update_classes(order, classs, length)
        length = length * 2

    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))