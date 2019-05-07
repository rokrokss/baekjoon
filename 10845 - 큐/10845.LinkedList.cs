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
            LinkedList<string> q = new LinkedList<string>();
            StringBuilder sb = new StringBuilder();
            string[] lineArr;
            for (int i = 0; i < n; i++)
            {
                lineArr = Console.ReadLine().Split();
                switch(lineArr[0])
                {
                    case "push":
                        q.AddLast(lineArr[1]);
                        break;

                    case "pop":
                        if (q.Count == 0) {
                            sb.AppendLine("-1");
                        } else {
                            sb.AppendLine(q.First.Value);
                            q.RemoveFirst();
                        }
                        break;

                    case "front":
                        sb.AppendLine(q.Count == 0 ? "-1" : q.First.Value);
                        break;

                    case "back":
                        sb.AppendLine(q.Count == 0 ? "-1" : q.Last.Value);
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

