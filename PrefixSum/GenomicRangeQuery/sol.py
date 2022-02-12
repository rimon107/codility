from collections import Counter 
def timeout_solution(S, P, Q):
    l = len(S)
    impact = [0] * l
    pl = len(P)
    res = []
    for index in range(l):
        if S[index]=='A':
            impact[index] = 1
        if S[index]=='C':
            impact[index] = 2
        if S[index]=='G':
            impact[index] = 3
        if S[index]=='T':
            impact[index] = 4
    for i in range(pl):
        start = P[i]
        end = Q[i]
        n = impact[start:end+1]
        res.append(min(n))
    return res

def timeout_solution(S, P, Q):
    l = len(S)
    impact = [0] * l
    pl = len(P)
    res = []
    for index in range(l):
        if S[index]=='A':
            impact[index] = 1
        if S[index]=='C':
            impact[index] = 2
        if S[index]=='G':
            impact[index] = 3
        if S[index]=='T':
            impact[index] = 4
    for i in range(pl):
        start = P[i]
        end = Q[i]
        n = S[start:end+1]
        res.append(n)
    rl = []
    for r in res:
        if "A" in r:
            rl.append(1)
        elif "C" in r:
            rl.append(2)
        elif "G" in r:
            rl.append(3)
        elif "T" in r:
            rl.append(4)
    return rl

def time_out_3_solution(S, P, Q):
    l = len(S)
    pl = len(P)
    res = []
    for i in range(pl):
        start = P[i]
        end = Q[i]
        n = S[start:end+1]
        res.append(n)
    rl = []
    for r in res:
        cnt = Counter(r)
        min = 5
        for key, _ in cnt.items():
            if key=='A':
                min = 1
            if key=='C':
                if min > 2:
                    min = 2
            if key=='G':
                if min > 3:
                    min = 3
            if key=='T':
                if min > 4:
                    min = 4
        rl.append(min)
    return rl

def eff_solution(S, P, Q):
    result = []
    DNA_len = len(S)
    mapping = {"A":1, "C":2, "G":3, "T":4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return result

def solution(S, P, Q):
    n = len(S)
    sumA = [0]*(n+1)
    sumC = [0]*(n+1)
    sumG = [0]*(n+1)
    sumT = [0]*(n+1)
    for idx, nucleotide in enumerate(S):
        sumA[idx+1] = sumA[idx]
        sumC[idx+1] = sumC[idx]
        sumT[idx+1] = sumT[idx]
        sumG[idx+1] = sumG[idx]
        if nucleotide == 'A':
            sumA[idx+1] += 1
        elif nucleotide == 'C':
            sumC[idx+1] += 1
        elif nucleotide == 'G':
            sumG[idx+1] += 1
        else:
            sumT[idx+1] += 1
    result = [0]*len(P)
    for i in range(len(P)):
        AsInRange = sumA[Q[i] + 1]- sumA[P[i]]
        CsInRange = sumC[Q[i] + 1]- sumC[P[i]]
        GsInRange = sumG[Q[i] + 1]- sumG[P[i]]
        if AsInRange > 0:
            result[i] = 1
        elif CsInRange > 0:
            result[i] = 2
        elif GsInRange > 0:
            result[i] = 3
        else:
            result[i] = 4
    return result

if __name__=="__main__":
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]

    res = solution(S, P, Q)
    print(res)