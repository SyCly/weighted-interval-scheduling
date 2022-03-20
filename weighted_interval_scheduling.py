#Silas Clymer 3/18/21
#Analysis of Algorithms

#These are various algorithms that solve the Weighted Interval Scheduling Problem dynamically
#Based on pseudocode from Ch. 6 of Kleinberg & Tardos' Algorithm Design

mylist = [[17,47,20],[32,48,12],[55,64,3],[18,69,28],[58,70,15],[58,89,30],[88,90,29]]
L = sorted(mylist, key=lambda tup: tup[1])
print(L)
n = len(L)

def p(j):
    res = 0
    for i in range(len(L[:j-1])+1):
        if L[i][1] <= L[j-1][0]:
            res = i+1
    return res

#Top Down (recursive)
M={}
def M_Compute_Opt(j):
    if j == 0:
        return 0
    elif j in M:
        return M[j]
    else:
        M[j] = max(L[j-1][2]+M_Compute_Opt(p(j)), M_Compute_Opt(j-1))
        return M[j]

print('Memoized:')
print(M_Compute_Opt(n))


#Bottom Up
def Iterative_Compute_Opt():
    M[0] = 0
    for j in range(1, n+1):
        M[j] = max(L[j-1][2]+M[p(j)], M[j-1])
    return M[n]

print('Tabulated:')
print(Iterative_Compute_Opt())

#Actual solution set of indices, where 1 is 1st index
sol = []
def Find_Solution(j):
    if j > 0:
        if L[j-1][2]+M[p(j)] >= M[j-1]:
            sol.append(j)
            if Find_Solution(p(j)):
                sol.append(Find_Solution(p(j)))
        else:
            if Find_Solution(j-1):
                sol.append(Find_Solution(j-1))

print('Solution Set:')
Find_Solution(n)
print(sol)

