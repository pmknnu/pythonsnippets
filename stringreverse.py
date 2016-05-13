def reverseStr(S):
    S.split()
    print " ".join(S.split()[::-1])

def reverseStr2(S):
    words=[]
    length=len(S)
    i=0

    while i<length:

        if S[i]!=" ":
            word_count=i

            while i<length and S[i]!=" ":
                i=i+1
            words.append(S[word_count:i])

        i=i+1
    print " ".join(words[::-1])



if __name__=="__main__":
    S="This is a String"
    reverseStr2(S)
