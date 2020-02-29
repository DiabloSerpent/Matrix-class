# returns all permutations of input sequence
def Permfind(sequence):
    if type(sequence) == int:  # turns int into range
        sequence = range(1, sequence + 1, 1)
    if type(sequence) == set or type(sequence) == dict:
        raise TypeError

    order = [1 for n in range(len(sequence))]
    # order denotes the item each element in order pops from the remaining pool of elements in tempseq

    Stop = False
    while Stop == False:
        tempseq = list(sequence)
        perm = []
        for x in order:
            perm.append(tempseq.pop(x - 1))
        yield perm

        order[-1] += 1
        for x in range(-1, -len(order) - 1, -1):
            if order[x] > -x:
                if x - 1 < -len(order):
                    Stop = True
                    break
                order[x] = 1
                order[x - 1] += 1
            else:
                break


def sgn(seq, perm):
    seq = list(seq)
    perm = list(perm)

    if len(seq) != len(perm):
        raise TypeError('Invalid permutation')
    for x in seq:
        if seq.count(x) != perm.count(x):
            raise TypeError('Invalid permutation')

    if seq == perm:
        return 1

    swaps = 0

    for x in range(len(seq)):
        if seq[x] == perm[x]:
            continue
        for y in range(x, len(seq)):
            if seq[x] == perm[y]:
                perm.insert(x, perm.pop(y))
                swaps += 1
                perm.insert(y, perm.pop(x + 1))
                break

    if swaps % 2 == 0:
        return 1
    else:
        return -1


def mult(ints):
    product = 1
    for x in ints:
        product *= x
    return product


def swap(sequence, index1, index2):
    typeseq = type(sequence)
    sequence = list(sequence)
    sequence.insert(index1, sequence.pop(index2))
    sequence.insert(index2, sequence.pop(index1 + 1))
    # seq = typeseq()
    # for element in sequence:
    #  seq = seq + typeseq(element)
    return typeseq(sequence)


# Added 10/5/19 - 
# It's technically longer, but is also more simple
def swapV2(sequence, index1, index2):
    typeseq = type(sequence)
    sequence = list(sequence)
    index1Val = sequence[index1]
    sequence[index1] = sequence[index2]
    sequence[index2] = index1Val
    return typeseq(sequence)
