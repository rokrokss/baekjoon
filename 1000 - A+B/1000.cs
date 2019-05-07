using System;


class Program
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        string[] ss = s.Split();
        int a = int.Parse(ss[0]);
        int b = int.Parse(ss[1]);
        Console.WriteLine(a + b);
    }
}

