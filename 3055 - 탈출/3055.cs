using System;
using System.Collections.Generic;


namespace _3055
{
    class Program
    {
        static readonly int[] dx = new int[] {1, -1, 0, 0};
        static readonly int[] dy = new int[] {0, 0, 1, -1};
        static void Main(string[] args)
        {
            string[] RC = Console.ReadLine().Split();
            int R = int.Parse(RC[0]);
            int C = int.Parse(RC[1]);
            bool[,] rocks = new bool[R, C];
            bool[,] waters = new bool[R, C];
            bool[,] visited = new bool[R, C];
            int[] D = new int[] {0, 0};
            Queue<int[]> waterQ = new Queue<int[]>();
            Queue<int[]> SQ = new Queue<int[]>();
            for (int i = 0; i < R; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < C; j++)
                {
                    if (line[j] == 'S')
                    {
                        SQ.Enqueue(new int[] {i, j});
                        visited[i, j] = true;
                    }
                    else if (line[j] == 'D')
                    {
                        D[0] = i;
                        D[1] = j;
                    }
                    else if (line[j] == 'X')
                        rocks[i, j] = true;
                    else if (line[j] == '*')
                    {
                        waterQ.Enqueue(new int[] {i, j});
                        waters[i, j] = true;
                    }
                }
            }
            int[] S, water;
            int cnt = 0;
            while (SQ.Count != 0)
            {
                int tmpWaterCnt = waterQ.Count;
                while (tmpWaterCnt-- > 0)
                {
                    water = waterQ.Dequeue();
                    for (int i = 0; i < 4; i++)
                    {
                        int[] nextW = new int[] {water[0] + dx[i], water[1] + dy[i]};
                        if (nextW[0] < 0 || nextW[0] == R || nextW[1] < 0 || nextW[1] == C)
                            continue;
                        if (rocks[nextW[0], nextW[1]] || waters[nextW[0], nextW[1]])
                            continue;
                        if (nextW[0] == D[0] && nextW[1] == D[1])
                            continue;
                        waterQ.Enqueue(nextW);
                        waters[nextW[0], nextW[1]] = true;
                    }
                }
                cnt++;
                int tmpSCount = SQ.Count;
                while (tmpSCount-- > 0)
                {
                    S = SQ.Dequeue();
                    for (int i = 0; i < 4; i++)
                    {
                        int[] nextS = new int[] {S[0] + dx[i], S[1] + dy[i]};
                        if (nextS[0] < 0 || nextS[0] == R || nextS[1] < 0 || nextS[1] == C)
                            continue;
                        if (rocks[nextS[0], nextS[1]] || waters[nextS[0], nextS[1]] || visited[nextS[0], nextS[1]])
                            continue;
                        if (nextS[0] == D[0] && nextS[1] == D[1])
                        {
                            Console.WriteLine(cnt.ToString());
                            return;
                        }
                        SQ.Enqueue(nextS);
                        visited[nextS[0], nextS[1]] = true;
                    }
                }
            }
            Console.WriteLine("KAKTUS");
        }
    }
}

