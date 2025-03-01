from typing import List

def longestCommonSubsequence_2D(text1: str, text2: str) -> int:
    # Get lengths of text1 and text2
    M, N = len(text1), len(text2)

    # Initialize the DP table with zeros
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    LCS = set()

    # Fill the DP table
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:  # Match found
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # No match, take max from left or top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[M][N]
    #return dp[M][N]

def longestCommonSubsequence_1D(text1: str, text2: str) -> int:
    # Get lengths of text1 and text2
    M, N = len(text1), len(text2)

    # Initialize the DP table with zeros
    dp = [0] * (N+1)

    # Fill the DP table
    for i in range(M):
        cur = [0]*(N+1)
        for j in range(N):
            if text1[i]==text2[j]:
                cur[j+1] = 1 + dp[j]
            else: 
                cur[j+1] = max(dp[j+1], cur[j])
        dp = cur

    return dp[N]


word1 = "aggtab"
word2 = "gxtxayb"
word1 = "bbabacaa"
word2 = "cccababab"
dp1 = longestCommonSubsequence_1D(word1, word2)
dp2 = longestCommonSubsequence_2D(word1, word2)
import pandas as pd

df2 = pd.DataFrame(dp2, index=[""] + list(word1), columns=[""] + list(word2))
print(df2)
