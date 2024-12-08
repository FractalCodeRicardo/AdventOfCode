using System.Text.RegularExpressions;

public class Problem03II
{
    public void Solve()
    {
        var data = Input.Read(3);
        var bigString = String.Join("", data);
        //var bigString = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
        Regex rg = new Regex(@"mul\([\d]+,[\d]+\)");


        var matches = rg.Matches(bigString);

        long sum = 0;

        var i = 0;
        var startI = 0;
        var endI = 0;
        while (i < matches.Count)
        {
            var match = matches[i];
            endI = startI + match.Index + match.Length - 1;
            var line = bigString.Substring(startI, endI - startI + 1);

            if (Applies(line))
            {
                sum += Mul(match);
            }
            i++;
        }

        Console.Write(sum);

    }

    public long Mul(Match match)
    {
        var cad = match.Captures.First().Value;
        cad = cad.Replace("mul", "")
            .Replace("(", "")
            .Replace(")", "");

        var split = cad.Split(",");

        return long.Parse(split[0]) * long.Parse(split[1]);
    }

    public bool Applies(string line)
    {
        var iDont = line.LastIndexOf("don't()");
        if (iDont < 0) return true;


        var iDo = line.LastIndexOf("do()");

        if (iDont < 0 && iDo < 0) return true;

        if (iDont > iDo) return false;

        return true;
    }
}