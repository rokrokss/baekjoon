#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int N;
	cin >> N;
	int* a = new int[N];
	int m=0;
	for (int i=0;i<N;i++){
		cin >> a[i];
		m=max(m, a[i]);
	}
	double sum = 0;
	for (int i=0;i<N;i++){
		sum = sum + ((double)a[i])/((double)m)*100;
	}
	printf("%.2f", sum/N);
	return 0;
}