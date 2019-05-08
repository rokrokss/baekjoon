using System;
using System.Text;
using System.Linq;


namespace _1018
{
    class Program
    {
        static char changeChar(char c)
        {
            if (c == 'W') return 'B';
            else return 'W';
        }
        static void Main(string[] args)
        {
            int[] nm = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
            int n = nm[0], m = nm[1];
            char[,] grid = new char[n, m];
            for (int i = 0; i < n; i++)
            {
                char[] tmp = Console.ReadLine().ToCharArray();
                for (int j = 0; j < m; j++)
                {
                    grid[i, j] = tmp[j];
                }
            }
            int ans = 64;
            for (int i = 0; i <= n - 8; i++)
            {
                for (int j = 0; j <= m - 8; j++)
                {
                    int cnt1 = 0;
                    int cnt2 = 0;
                    char wFirst = 'W';
                    char bFirst = 'B';
                    for (int k = 0; k < 8; k++) {
                        for (int l = 0; l < 8; l++) {
                            if (grid[i + k, j + l] != wFirst)
                            {
                                cnt1 += 1;
                            }
                            if (grid[i + k, j + l] != bFirst)
                            {
                                cnt2 += 1;
                            }
                            wFirst = changeChar(wFirst);
                            bFirst = changeChar(bFirst);
                        }
                        wFirst = changeChar(wFirst);
                        bFirst = changeChar(bFirst);
                    }
                    ans = Math.Min(Math.Min(cnt1, cnt2), ans);
                }
            }
            Console.Write(ans.ToString());
        }
    }
}

