#include <iostream>
#include <algorithm>
using namespace std;
int sc[1000];

int main() {
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int sum = 0;
		for (int i=0;i<n;i++){
			cin >> sc[i];
			sum = sum + sc[i];
		}
		double m = ((double)sum)/n;
		int people = 0;
		for (int i=0;i<n;i++){
			if (sc[i]>m){
				people++;
			}
		}
		printf("%.3f%%\n", (double)people*100/(double)n);
	}
	return 0;
}