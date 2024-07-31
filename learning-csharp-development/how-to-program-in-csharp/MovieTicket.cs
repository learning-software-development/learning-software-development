namespace ProgramCsharp
{
  public class MovieTicket
  {
    public void orderMovieTicket()
    {
      Console.Write("Welcome!\nTickets are 5$. Please insert cash. ");
      int cash = Convert.ToInt32(Console.ReadLine());

      if (cash < 5)
      {
        Console.WriteLine("That is not enough money.");
      }
      else if (cash == 5)
      {
        Console.WriteLine("Here is your ticket.");
      }
      else
      {
        int change = cash - 5;
        Console.WriteLine("Here is your ticket and " + change + " dollars in change.");
      }
    }
  }
}
