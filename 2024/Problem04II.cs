using System.Threading.Channels;

public class Problem04II
{

    public void Solve()
    {
        var data = Input.Read(4);
        data = data.Select(i => i.Trim()).ToList();

        var count = 0;
        var len = data[0].Length;
        var y = 0;

        while (y < data.Count)
        {
            var x = 0;
            while (x < len)
            {
                count +=HasXMAS(x, y, "MAS", "MAS", data);
                count +=HasXMAS(x, y, "MAS", "SAM", data);
                count +=HasXMAS(x, y, "SAM", "MAS", data);
                count +=HasXMAS(x, y, "SAM", "SAM", data);
                    
                x++;
            }
            y++;
        }


        Console.Write(count);

    }

    public int HasXMAS(int x, int y, string w1, string w2, List<string> data)
    {
        if (x + 2 > data[y].Length - 1) return 0;
        if (y + 2 > data.Count - 1) return 0;

        if (
        data[y][x] == w1[0] &&
        data[y + 1][x + 1] == w1[1] &&
        data[y + 2][x + 2] == w1[2] &&

        data[y + 2][x] == w2[0] &&
        data[y + 1][x + 1] == w2[1] &&
        data[y][x + 2] == w2[2])
        {
            return 1;
        }

        return 0;
    }

}