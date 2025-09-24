def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[m][n]

    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str = X[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, lcs_str


X = "AGGTAB"
Y = "GXTXAYB"
print(lcs_recursive(X, Y, len(X), len(Y)))


length, subseq = lcs_dp(X, Y)
print("Comprimento da LCS:", length)  
print("LCS:", subseq)                   


