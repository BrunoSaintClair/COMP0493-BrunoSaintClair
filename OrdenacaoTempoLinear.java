import java.util.*;

class OrdenacaoTempoLinear {
    
    static void BucketSort(int[] arr, int bucketSize){
        if (arr == null || arr.length == 0 || bucketSize <= 0){
            return;
        }

        int n = arr.length;
        int minValue = arr[0];
        int maxValue = arr[0];

        for (int i = 1; i < n; i++){
            if (arr[i] < minValue){
                minValue = arr[i];
            } else if (arr[i] > maxValue){
                maxValue = arr[i];
            }
        }   

        double range = Math.ceil((double) (maxValue - minValue + 1) / bucketSize);

        List<List<Integer>> buckets = new ArrayList<>();

        for (int i = 0; i < bucketSize; i++){
            buckets.add(new LinkedList<>());
        }

        for (int value : arr){
            int bucketIndex = (int) ((value - minValue) / range);
            buckets.get(bucketIndex).add(value);
        }

        for (List<Integer> bucket : buckets){
            Collections.sort(bucket);
        }

        int index = 0;

        for (List<Integer> bucket : buckets){
            for (int value : bucket){
                arr[index++] = value;
            }
        }
    }

    static void CountingSort(int[] arr){
        if (arr == null || arr.length == 0){
            return;
        }

        int n = arr.length;
        int maxValue = arr[0];

        for (int i = 1; i < n; i++){
            if (arr[i] > maxValue){
                maxValue = arr[i];
            }
        }

        int[] count = new int[maxValue + 1];

        for (int value : arr){
            count[value]++;
        }

        int index = 0;

        for (int i = 0; i < count.length; i++){
            for (int j = 0; j < count[i]; j++){
                arr[index++] = i;
            }
        }
    }

    static void RadixSort(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }
    
        int maxValue = arr[0];
        for (int value : arr) {
            if (value > maxValue) {
                maxValue = value;
            }
        }
    
        int exp = 1; 
        while (maxValue / exp > 0) {
            countingSortByDigit(arr, exp);
            exp *= 10; 
        }
    }

    static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n]; 
        int[] count = new int[10]; 
    
        for (int value : arr) {
            int digit = (value / exp) % 10; 
            count[digit]++;
        }
    
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
    
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }
    
        System.arraycopy(output, 0, arr, 0, n);
    }
    
}