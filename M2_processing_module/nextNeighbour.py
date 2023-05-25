## Function next neighbour ##

""" Obtain the next no-null neighbour """
def next_neighbour(matrix, i, j, dir):
    array = []
    pto = 0
    val = 1
    init = 0

    if dir == "right":
        array = matrix[i]
        pto = j+1
        init = j
    elif dir == "bottom":
        array = []
        for c in matrix:
            array.append(c[j])
        pto = i+1
        init = i
    else:
        val = 0

    if val:
        while pto < len(array) and array[pto] == 0:
            pto = pto + 1

    if (pto < len(array)):
        val = array[pto]
    elif init-1 > 0:
        val = array[init-1]
    else:
        val = 0

    return val

