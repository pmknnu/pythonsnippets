def compress(S):
    if len(S)==0:
        return ""
    if len(S)==1:
        return S+"1"

    count=1
    l=len(S)
    i=1
    r=""

    while i< l:
        if S[i]==S[i-1]:
            count +=1
        else:
            r=r+S[i-1]+str(count)
            count=1

        i=i+1
    return r+S[i-1]+str(count)  ###for the last letter


if __name__=="__main__":
    S="AAB"
    print compress(S)
