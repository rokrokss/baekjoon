using System;


namespace _2294
{
    class Program
    {
        const int inf = 10001;
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]), k = int.Parse(nk[1]);
            int[] coins = new int[n];
            for (int i = 0; i < n; i++)
                coins[i] = int.Parse(Console.ReadLine());
            int[] dp = new int[k + 1];
            Array.Fill(dp, inf);
            dp[0] = 0;
            for (int i = 0; i < n; i++)
                for (int j = coins[i]; j <= k; j++)
                    if (dp[j] > dp[j - coins[i]] + 1) dp[j] = dp[j - coins[i]] + 1;
            Console.WriteLine(dp[k] == inf ? "-1": dp[k].ToString());
        }
    }
}

