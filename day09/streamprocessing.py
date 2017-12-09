

stream = open("input.txt", "r").read()
garbage = 0


def delete_deletes(my_stream):
    stream = list(my_stream)
    i = 0
    j = []
    while i < len(stream):
        if stream[i] == '!':
            j += [i, i+1]
            i += 2
        else:
            i += 1
    for index in sorted(j, reverse=True):
        del stream[index]

    return ''.join(stream)

def delete_garbage(stream, garbage):
    beg = stream.find('<')
    if beg == -1:
        return stream, garbage

    end = stream.find('>', beg)
    if end == -1:
        return stream, garbage

    garbage += len(stream[beg:end]) -1
    return stream[:beg] + stream[end+1:], garbage

stream = delete_deletes(stream)

new_stream, garbage = delete_garbage(stream, garbage)

while stream != new_stream:
    stream = new_stream
    new_stream, garbage = delete_garbage(stream, garbage)


processed = []
current_group = 0

i = 0
while i < len(new_stream):
    char = stream[i]
    if char == '!':
        i += 2

    elif char == '{':
        current_group += 1
        i += 1

    elif char == '}':
        processed.append(current_group)
        current_group -= 1
        i += 1

    else:
        i += 1

print sum(processed)
print garbage


