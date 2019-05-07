using System;
using System.Text;
using System.Collections.Generic;


namespace _1874
{
    class Program
    {
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            Stack<int> s = new Stack<int>();
            StringBuilder sb = new StringBuilder();
            s.Push(0);
            int n;
            int item = 1;
            bool flag = false;
            for (int _ = 0; _ < t; _++)
            {
                n = int.Parse(Console.ReadLine());
                if (n >= item)
                {
                    for (; item <= n; item++) {
                        s.Push(item);
                        sb.AppendLine("+");
                    }
                }
                else if (n != s.Peek())
                {
                    flag = true;
                    break;
                }
                s.Pop();
                sb.AppendLine("-");
            }
            Console.WriteLine(flag ? "NO" : sb.ToString());
        }
    }
}

