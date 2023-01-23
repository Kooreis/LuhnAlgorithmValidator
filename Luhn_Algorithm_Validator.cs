```CSharp
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter a number: ");
        string number = Console.ReadLine();
        Console.WriteLine(IsValid(number) ? "Valid" : "Invalid");
    }

    static bool IsValid(string number)
    {
        int sum = 0;
        bool alternate = false;
        for (int i = number.Length - 1; i >= 0; i--)
        {
            int n = int.Parse(number[i].ToString());
            if (alternate)
            {
                n *= 2;
                if (n > 9)
                {
                    n = (n % 10) + 1;
                }
            }
            sum += n;
            alternate = !alternate;
        }
        return (sum % 10 == 0);
    }
}
```