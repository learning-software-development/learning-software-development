namespace ProgramCsharp
{
  public class Calculator
  {
    public void askName()
    {
      Console.WriteLine("Hello, what's your name!");
      string userName = Console.ReadLine();

      Console.WriteLine("Hello " + userName + ", nice to meet you!");
    }
    public void calculateAVG()
    {
      Console.Write("Input first number:");
      int numOne = Convert.ToInt32(Console.ReadLine());

      Console.Write("Input second number:");
      int numTwo = Convert.ToInt32(Console.ReadLine());

      Console.Write("Input third number:");
      int numThree = Convert.ToInt32(Console.ReadLine());

      if (numOne + numTwo + numThree > 3)
      {
        Console.WriteLine("The result is: " + (numOne + numTwo + numThree) / 3);
      }
      else
      {
        Console.WriteLine("Something went wrong.");
      }
    }
  }
}
