def next_sequence(seq):
    result = ''
    i = 0
    while i < len(seq):
        count = 1
        while i + 1 < len(seq) and seq[i] == seq[i+1]:
            count += 1
            i += 1
        result = f'{result}{count}{seq[i]}'
        i += 1
    return result


def main(n, start_seq):
    print(start_seq)
    next_seq = start_seq
    for i in range(n):
        next_seq = next_sequence(next_seq)
        print(next_seq)


if __name__ == '__main__':
    main(n=4, start_seq='1')
