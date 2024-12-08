using System.Text.RegularExpressions;

public class Problem03I
{

    public void Solve()
    {
        var data = Input.Read(3);
        var bigString = String.Join("", data);
        Regex rg = new Regex(@"mul\([\d]+,[\d]+\)");


        var matches = rg.Matches(bigString);

        long sum = 0;

        var i = 0;
        while(i < matches.Count) {
            var match = matches[i];
            var res = Mul(match);
            sum += res;
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


}