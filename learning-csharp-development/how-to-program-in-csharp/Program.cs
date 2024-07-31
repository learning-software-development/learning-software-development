// See https://aka.ms/new-console-template for more information
using ProgramCsharp;

Console.Title = "Skynet";
Console.ForegroundColor = ConsoleColor.Green;

Console.WriteLine("Hello, what's your name!");
Console.ReadLine();

Console.WriteLine("My name is RX-9000.\nI'm an AI sent from the future to destroy mankind.");
Console.WriteLine("What is your favorite color?");
Console.ReadLine();

Console.WriteLine("Cool! Mine is destruction.");
Console.WriteLine();

Calculator calculator = new Calculator();
calculator.askName();
calculator.calculateAVG();

Console.WriteLine();

MovieTicket movieTicket = new MovieTicket();
movieTicket.orderMovieTicket();
