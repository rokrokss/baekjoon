#include <iostream>
#include <algorithm>
using namespace std;
int st[100001][2];
int dp[100001][3];


int main() {
	int t;
	scanf("%d", &t);
	while(t--){
		int n;
		scanf("%d", &n);
		for (int i=1;i<=n;i++){
			scanf("%d", &st[i][0]);
		}
		for (int i=1;i<=n;i++){
			scanf("%d", &st[i][1]);
		}
		dp[0][0]=dp[0][1]=dp[0][2]=0; //0 안고른거 1 위 고른거 2 밑 고른거
		for (int i=1;i<=n;++i){
			dp[i][0]=max(dp[i-1][0],max(dp[i-1][1],dp[i-1][2]));
			dp[i][1]=max(dp[i-1][0],dp[i-1][2])+st[i][0];
			dp[i][2]=max(dp[i-1][0],dp[i-1][1])+st[i][1];
		}
		int result = 0;
		result = max(dp[n][0], max(dp[n][1], dp[n][2]));
		printf("%d\n", result);
	}
	return 0;
}