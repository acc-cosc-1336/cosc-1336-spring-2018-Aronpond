def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    counta = 0
    countt = 0
    countg = 0
    countc = 0
    for ch in (dna_string[:]):
        if ch == 'a' or ch == 'A':
            counta += 1
        if ch == 't' or ch == 'T':
            countt += 1
        if ch == 'g' or ch == 'G':
            countg += 1
        if ch == 'c' or ch == 'C':
            countc += 1
    return(counta, countt, countg, countc)
