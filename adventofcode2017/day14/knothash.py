# making day10 answer a function

from operator import xor

def knothash(lengths, numbers, current_position, skip_size):
    n = len(numbers)

    for length in lengths:
        if current_position + length < n:
            sublist = numbers[current_position:current_position+length]
            numbers[current_position:current_position+length] = sublist[::-1]

        else:
            diff = current_position + length - n
            sublist = numbers[current_position:] + numbers[:diff]
            rev_sublist = sublist[::-1]
            numbers[current_position:] = rev_sublist[:len(sublist)-diff]
            numbers[:diff] = rev_sublist[len(sublist)-diff:]

        current_position = current_position + length + skip_size
        while current_position >= n:
            current_position -= n

        skip_size += 1

    return numbers, current_position, skip_size

def get_hash(string):

    n = 256
    suffix = [17, 31, 73, 47, 23]
    lengths = [ord(char) for char in string]
    lengths += suffix

    numbers = range(n)
    current_position = 0
    skip_size = 0

    for i in range(64):
        numbers, current_position, skip_size = \
            knothash(lengths, numbers, current_position, skip_size)

    sparse_hash = numbers
    dense_hash = []

    for n in range(15):
        block = sparse_hash[n*16:(n+1)*16]
        res = reduce(xor, block)
        dense_hash.append(res)

    dense_hash.append(reduce(xor, sparse_hash[-16:]))


    def to_hex(digit):
        h = hex(digit).split('x')
        if digit <= 15:
            return '0'+ h[-1]
        else:
            return h[-1]

    hashcode = ''.join([to_hex(digit) for digit in dense_hash])
    return hashcode

if __name__ == '__main__':
    print get_hash("")
    print get_hash("AoC 2017")
    print get_hash("1,2,3")
    print get_hash("1,2,4")

