def uniq_char(S):
    return len(set(S))==len(S)

def uniq_char2(S):
    chars=list()
    for i in S:
        if i in chars:
            return False
        else:
            chars.append(i)
    return True

if __name__=="__main__":
    S="abcdefg"
    print uniq_char2(S)
