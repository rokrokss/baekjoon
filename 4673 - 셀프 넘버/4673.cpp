#include <iostream>
#include <algorithm>
using namespace std;
int visited[10050]={0};

void d(int n){
	int dn = n+n%10;
	while (n>0){
		n = n/10;
		dn = dn + n%10;
	}
	visited[dn]=1;
}

int main() {
	for (int i = 1; i<10000; i++){
		if (visited[i]==0){
			printf("%d\n", i);
			d(i);
		}
		else{
			d(i);
		}
	}
	return 0;
}