using System.Runtime.CompilerServices;

public class Problem04I
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
                count += Horizontal(x, y, "XMAS", data);
                count += Horizontal(x, y, "SAMX", data);
                count += Vertical(x, y, "XMAS", data);
                count += Vertical(x, y, "SAMX", data);
                count += Diagonal(x, y, "XMAS", data);
                count += Diagonal(x, y, "SAMX", data);
                count += Diagonaleft(x, y, "XMAS", data);
                count += Diagonaleft(x, y, "SAMX", data);
                x++;
            }
            y++;
        }


        Console.Write(count);

    }

    public int Horizontal(int x, int y, string word, List<string> data)
    {

        foreach (var c in word)
        {
            if (x > data[y].Length - 1)
                return 0;

            if (c != data[y][x])
                return 0;

            x++;
        }

        return 1;
    }


    public int Vertical(int x, int y, string word, List<string> data)
    {

        foreach (var c in word)
        {
            if (y > data.Count - 1)
                return 0;

            if (c != data[y][x])
                return 0;

            y++;
        }

        return 1;
    }

    public int Diagonal(int x, int y, string word, List<string> data)
    {

        foreach (var c in word)
        {
            if (y > data.Count - 1)
                return 0;

            if (x > data[y].Length - 1)
                return 0;

            if (c != data[y][x])
                return 0;

            y++;
            x++;
        }

        return 1;
    }


    public int Diagonaleft(int x, int y, string word, List<string> data)
    {

        foreach (var c in word)
        {
            if (y > data.Count - 1)
                return 0;

            if (x < 0)
                return 0;

            if (c != data[y][x])
                return 0;

            y++;
            x--;
        }

        return 1;
    }

}