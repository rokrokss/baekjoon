using System;
using System.Text;
using System.Collections.Generic;


namespace _10845
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Deque<string> q = new Deque<string>();
            StringBuilder sb = new StringBuilder();
            string[] lineArr;
            for (int i = 0; i < n; i++)
            {
                lineArr = Console.ReadLine().Split();
                switch(lineArr[0])
                {
                    case "push":
                        q.Enqueue(lineArr[1]);
                        break;

                    case "pop":
                        sb.AppendLine(q.Count == 0 ? "-1" : q.Dequeue());
                        break;

                    case "front":
                        sb.AppendLine(q.Count == 0 ? "-1" : q.PeekLeft());
                        break;

                    case "back":
                        sb.AppendLine(q.Count == 0 ? "-1" : q.PeekRight());
                        break;

                    case "size":
                        sb.AppendLine(q.Count.ToString());
                        break;

                    case "empty":
                        sb.AppendLine(q.Count == 0 ? "1" : "0");
                        break;
                }
            }
            Console.WriteLine(sb);
        }
    }
}

