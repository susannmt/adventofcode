from operator import xor

# --- PART 1 ---
lengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
current_position = 0
skip_size = 0
n = 256
numbers = range(n)

def knothash(length, numbers, current_position, skip_size):
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


num, pos, skip = knothash(lengths, numbers, current_position, skip_size)
print num[0]*num[1]


# --- PART 2 ---
suffix = [17, 31, 73, 47, 23]
lengthstring = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
lengths = [ord(char) for char in lengthstring]
lengths += suffix

numbers = range(n)

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

hashcode = ''.join([hex(digit)[-2:] for digit in dense_hash])
print len(hashcode)
print hashcode


