package Java;
public class Program_2 {
    int[] findMinMax(int[] arr){
        int min = arr[0];
        int max = arr[0];
        for (int i=0;i<arr.length;i++)
        {
            if (arr[i] < min)
                min = arr[i];
            if (arr[i] > max)
                max = arr[i];        
        }
        return new int[]{min, max};

    }
    public static void main(String[] args) {
        Program_2 obj = new Program_2();

        int[] arr = {1, 4, 3, 5, 8, 6};

        int[] result = obj.findMinMax(arr);

        System.out.println("Minimum: " + result[0]);
        System.out.println("Maximum: " + result[1]);
    }
}
