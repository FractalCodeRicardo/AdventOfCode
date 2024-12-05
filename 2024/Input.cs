public class Input {

    public static List<string> Read(int problem) {
        var file = $"Input{problem.ToString("D2")}.txt";
        return File.ReadLines(file).ToList();
    }
}