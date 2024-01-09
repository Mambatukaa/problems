function decodeVariations(S) {
    const N = S.length;
    const dp = new Array(N + 1);
    dp[N] = 1;

    for (let i = N - 1; i >= 0; i--) {
        if (S[i] === '0') {
            dp[i] = 0;
        } else if (S[i] === '1') {
            dp[i] = dp[i + 1] + dp[i + 2];
        } else if (S[i] === '2') {
            dp[i] = dp[i + 1];
            if (i + 1 < S.length && S[i + 1] <= '6') {
                dp[i] += dp[i + 2];
            }
        } else {
            dp[i] = dp[i + 1];
        }
    }

    return dp[0];
};

console.log(decodeVariations('262'))
