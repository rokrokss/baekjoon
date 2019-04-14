#include <iostream>
using namespace std;

void swap(int i, int j, int *a){
	int temp=a[i];
	a[i]=a[j];
	a[j]=temp;
}

int partition(int *arr, int left, int right){
	int pivot=arr[right];
	int i=left-1;
	for(int j=left; j<=right-1; j++){
		if(arr[j]>pivot){
			i++;
			swap(i, j, arr);
		}
	}
	swap(i+1,right,arr);
	return i+1;
}

void quicksort(int *arr, int left, int right){
	if(left<right){
		int i = partition(arr, left, right);
		quicksort(arr, left, i-1);
		quicksort(arr, i+1, right);
	}
}

int main() {
	int n;
	cin >> n;
	bool done = false;
	int* ary = new int[11];
	int i=0;
	int tmp=n;
	while(!done){
		ary[i] = tmp%10;
		tmp = tmp/10;
		i++;
		if(tmp==0){
			done=true;
		}
	}
	quicksort(ary, 0, i-1);
	for(int j=0;j<i;j++){
		cout << ary[j];
	}
	return 0;
}