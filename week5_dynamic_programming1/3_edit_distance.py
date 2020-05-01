def output_alignment(i, j, matrix, s, t, res):
    if i == 0 and j == 0:
        return
    if i > 0 and matrix[i][j] == matrix[i-1][j]+1:
        output_alignment(i-1, j, matrix, s, t, res)
        res[0].append(t[i-1])
        res[1].append("-")
    elif j > 0 and matrix[i][j] == matrix[i][j-1]+1:
        output_alignment(i, j-1, matrix, s, t, res)
        res[0].append("-")
        res[1].append(s[j-1])
    else:
        output_alignment(i-1, j-1, matrix, s, t, res)
        res[0].append(t[i-1])
        res[1].append(s[j-1])



def edit_distance(s, t):
    dynamic_matrix = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]

    for i in range(len(s)+1):
        dynamic_matrix[0][i] = i
    for j in range(len(t)+1):
        dynamic_matrix[j][0] = j

    for j in range(1, len(s)+1):
        for i in range(1, len(t)+1):
            insertion = dynamic_matrix[i][j-1]+1
            deletion = dynamic_matrix[i-1][j]+1
            mismatch = dynamic_matrix[i-1][j-1]+1
            match = dynamic_matrix[i-1][j-1]

            if s[j-1] == t[i-1]:
                dynamic_matrix[i][j] = min(insertion, deletion, match)
            else:
                dynamic_matrix[i][j] = min(insertion, deletion, mismatch)

    res = [[], []]
    output_alignment(i, j, dynamic_matrix, s, t, res)

    edit_length = 0
    for i in range(len(res[0])):
        if res[0][i] != res[1][i]:
            edit_length += 1
    return edit_length


if __name__ == "__main__":
    print(edit_distance(input(), input()))

