#include <iostream>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	int tmp;
	int* ary = new int[10001];
	for (int i=0;i<10001;i++){
		ary[i]=0;
	}
	for (int i=0;i<n;i++){
		scanf("%d", &tmp);
		ary[tmp]++;
	}
	for (int i=0;i<10001;i++){
		for (int j=0;j<ary[i];j++){
			printf("%d\n", i);
		}
	}
	return 0;
}