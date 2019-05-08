using System;


namespace _2902
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            Console.Write(input[0]);
            for (int i = 1; i < input.Length; i++)
            {
                if (input[i] == '-') Console.Write(input[i + 1]);
            }
        }
    }
}

