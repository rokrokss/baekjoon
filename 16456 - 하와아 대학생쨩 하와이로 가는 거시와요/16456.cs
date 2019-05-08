using System;


namespace _16456
{
    class Program
    {
        static void Main(string[] args)
        {
            int mod = 1000000009;
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n + 3];
            arr[0] = 1;
            arr[1] = 1;
            arr[2] = 2;
            for (int i = 3; i < n; i++)
            {
                arr[i] = (arr[i - 1] + arr[i - 3]) % mod;
            }
            Console.WriteLine((arr[n - 1] % mod).ToString());
        }
    }
}
