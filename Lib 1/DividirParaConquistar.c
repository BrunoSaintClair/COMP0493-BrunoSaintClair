#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1. Binary Exponentiation
long long binaryExponentiation(long long base, long long exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result *= base;
        }
        base *= base;
        exp /= 2;
    }
    return result;
}

// 2. Merge Sort
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// 3. Inversion Index
int mergeAndCount(int arr[], int temp[], int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    int inv_count = 0;

    while ((i <= mid) && (j <= right)) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            inv_count += (mid - i + 1);
        }
    }

    while (i <= mid)
        temp[k++] = arr[i++];
    while (j <= right)
        temp[k++] = arr[j++];

    for (i = left; i <= right; i++)
        arr[i] = temp[i];

    return inv_count;
}

int countInversions(int arr[], int temp[], int left, int right) {
    int inv_count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        inv_count += countInversions(arr, temp, left, mid);
        inv_count += countInversions(arr, temp, mid + 1, right);
        inv_count += mergeAndCount(arr, temp, left, mid, right);
    }
    return inv_count;
}

int getInversionIndex(int arr[], int n) {
    int *temp = (int *)malloc(n * sizeof(int));
    int result = countInversions(arr, temp, 0, n - 1);
    free(temp);
    return result;
}

// 4. Longest Common Prefix
int min(int a, int b) {
    return a < b ? a : b;
}

char *longestCommonPrefix(char **strings, int left, int right) {
    if (left == right) {
        return strings[left];
    }

    int mid = left + (right - left) / 2;
    char *lcpLeft = longestCommonPrefix(strings, left, mid);
    char *lcpRight = longestCommonPrefix(strings, mid + 1, right);

    int minLen = min(strlen(lcpLeft), strlen(lcpRight));
    int i;
    for (i = 0; i < minLen; i++) {
        if (lcpLeft[i] != lcpRight[i]) {
            break;
        }
    }

    char *lcp = (char *)malloc((i + 1) * sizeof(char));
    strncpy(lcp, lcpLeft, i);
    lcp[i] = '\0';
    return lcp;
}
