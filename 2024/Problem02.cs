public class Problem02
{

    public void Solve()
    {
        var data = Input.Read(2);

        var count = 0;
        foreach (var line in data)
        {
            if (isSafe(line))
            {
                count++;
            }
        }

        Console.Write(count);
    }

    public bool isSafe(string line)
    {
        var split = line.Split(" ");
        var numbers = split
            .Select(i => int.Parse(i))
            .ToList();

        var cIncresing = numbers[0] < numbers[1];
        var cDecresing = numbers[0] > numbers[1];

        if (!cIncresing && !cDecresing)
            return false;

        var size = Math.Abs(numbers[0] - numbers[1]);

        if (size > 3) return false;

        var i = 1;

        while (i < numbers.Count - 1)
        {
            var nIncresing = numbers[i] < numbers[i + 1];
            var nDecresing = numbers[i] > numbers[i + 1];

            if (cIncresing != nIncresing)
                return false;

            if (cDecresing != nDecresing)
                return false;

            if (Math.Abs(numbers[i] - numbers[i + 1]) > 3)
                return false;

            if (!nIncresing && !nDecresing)
                return false;

            cDecresing = nDecresing;
            cIncresing = nIncresing;
            i++;
        }

        return true;
    }
}