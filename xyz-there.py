# problem: https://codingbat.com/prob/p149391


def xyz_there(str):
    i = 0
    if i + 3 < len(str) and str[i] != 'x' and str[i + 1] != 'y' and str[i + 2] != 'z':
        while i + 3 < len(str):
            if str[i] != '.' and str[i + 1] == 'x' and str[i + 2] == 'y' and str[i + 3] == 'z':
                return True
            i = i + 1
        return False
    elif len(str) < 3:
        return False
    else:
        return True
