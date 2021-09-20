def decode(string):
    k=1
    string+=' '
    snew = ''
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            k+=1
        else:
            if k != 1:
                snew +=str(k)+string[i]
            else:
                snew += string[i]
            k = 1
    return snew
