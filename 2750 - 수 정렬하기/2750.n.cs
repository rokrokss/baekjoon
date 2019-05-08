using System;
using System.Text;


namespace _2750
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = int.Parse(Console.ReadLine());
            }
            Array.Sort(arr);
            for (int i = 0; i < n; i++) {
                sb.AppendLine(arr[i].ToString());
            }
            Console.WriteLine(sb);
        }
    }
}

