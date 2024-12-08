public class Problem01II
{
    public void Solve()
    {
        var data = Input.Read(1);
        var l1 = new List<int>();
        var l2 = new List<int>();

        foreach (var line in data)
        {
            var split = line.Split("   ");
            var s1 = int.Parse(split[0].Trim());
            var s2 = int.Parse(split[1].Trim());

            l1.Add(s1);
            l2.Add(s2);
        }
        var sum = 0;
        foreach (var left in l1)
        {
            var count = l2
                .Where(i => i == left)
                .Count();

            sum += left * count;

        }

        Console.Write(sum);
    }

}