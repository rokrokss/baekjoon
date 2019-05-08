using System;
using System.Linq;


namespace _2293
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nk = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
            int n = nk[0], k = nk[1];
            int[] coins = new int[n];
            for (int i = 0; i < n; i++)
            {
                coins[i] = int.Parse(Console.ReadLine());
            }
            int[] dp = new int[k + 1];
            dp[0] = 1;
            for (int i = 0; i < n; i++)
            {
                for (int j = 1; j <= k; j++)
                {
                    if (coins[i] <= j) dp[j] += dp[j - coins[i]];
                }
            }
            Console.WriteLine(dp[k].ToString());
        }
    }
}

