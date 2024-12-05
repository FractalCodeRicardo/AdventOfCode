public class Problem01 {

    public void Solve() {
        var data = Input.Read(1);
        var l1 = new List<int>();
        var l2 = new List<int>();

        foreach(var line in data) {
            var split = line.Split("   ");
            var s1 =  int.Parse(split[0].Trim());
            var s2 =  int.Parse(split[1].Trim());

            l1.Add(s1);
            l2.Add(s2);
        }

        l1 = l1.Order().ToList();
        l2 = l2.Order().ToList();

        var i = 0;
        var sum = 0;
        while(i < l1.Count()) {
            var d = Math.Abs(l1[i] - l2[i]);
            sum += d;
            i++;
        }

        Console.Write(sum);
    }
}