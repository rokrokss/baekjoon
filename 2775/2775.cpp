#include <iostream>
#include <math.h>
using namespace std;



int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++){
		int k, n;
		cin >> k >> n;
		int arr[k+1][n];
		for (int i=0;i<=k;i++){
			for(int j=0;j<n;j++){
				arr[i][j]=0;
			}
		}
		for (int j=0;j<n;j++){
			arr[0][j]=j+1;
		}
		for (int j=1;j<=k;j++){
			for (int k=0;k<n;k++){
				for (int m=0;m<=k;m++){
					arr[j][k] = arr[j][k]+arr[j-1][m];
				}
			}
		}
		int answer = arr[k][n-1];
		cout << answer << endl;
	}
	return 0;
}