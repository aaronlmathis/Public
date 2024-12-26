def longest_common_subsequence(A, B):
    m, n = len(A), len(B)
    # Initialize DP table with (m+1) rows and (n+1) columns
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # Fill the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Uncomment below to print the DP table
    for row in dp:
        print(row)
    
    return dp[m][n]

# Example usage
A = "AGGTAB"
B = "GXTXAYB"
print("Length of LCS:", longest_common_subsequence(A, B))  # Output: 4