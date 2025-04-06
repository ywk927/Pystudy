S = list(input())
alphabet_list = [-1] * 26
for i in range(len(S)-1,-1,-1):
    if S[i] == 'a':
        alphabet_list[0] = i
    elif S[i] == 'b':
        alphabet_list[1] = i
    elif S[i] == 'c':
        alphabet_list[2] = i
    elif S[i] == 'd':
        alphabet_list[3] = i
    elif S[i] == 'e':
        alphabet_list[4] = i
    elif S[i] == 'f':
        alphabet_list[5] = i
    elif S[i] == 'g':
        alphabet_list[6] = i
    elif S[i] == 'h':
        alphabet_list[7] = i
    elif S[i] == 'i':
        alphabet_list[8] = i
    elif S[i] == 'j':
        alphabet_list[9] = i
    elif S[i] == 'k':
        alphabet_list[10] = i
    elif S[i] == 'l':
        alphabet_list[11] = i
    elif S[i] == 'm':
        alphabet_list[12] = i
    elif S[i] == 'n':
        alphabet_list[13] = i
    elif S[i] == 'o':
        alphabet_list[14] = i
    elif S[i] == 'p':
        alphabet_list[15] = i
    elif S[i] == 'q':
        alphabet_list[16] = i
    elif S[i] == 'r':
        alphabet_list[17] = i
    elif S[i] == 's':
        alphabet_list[18] = i
    elif S[i] == 't':
        alphabet_list[19] = i
    elif S[i] == 'u':
        alphabet_list[20] = i
    elif S[i] == 'v':
        alphabet_list[21] = i
    elif S[i] == 'w':
        alphabet_list[22] = i
    elif S[i] == 'x':
        alphabet_list[23] = i
    elif S[i] == 'y':
        alphabet_list[24] = i
    elif S[i] == 'z':
        alphabet_list[25] = i
print(*alphabet_list)