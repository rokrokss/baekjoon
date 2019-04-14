#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

int cost[1000];
int d[1000];
int indegree[1000];

int ACM(int N, int w, vector<int, allocator<int>>* adj) {
	queue<int> Q;
	for (int j = 0; j < N; j++) {
		if (indegree[j] == 0) {
			Q.push(j);
			d[j] = cost[j];
		}
	}
	for (int j = 0; j < N; j++) {
		if (Q.empty()) {
			break;
		}
		int curr = Q.front();
		Q.pop();
		for (int next: adj[curr]) {
			d[next] = max(d[next], d[curr] + cost[next]);
			indegree[next]--;
			if (indegree[next] == 0) {
				Q.push(next);
				if (next == w){
					return d[w];
				}
			}
		}
	}
}
int main() {
	int t;
	cin >> t;

	int* result = new int[t];
	for (int i=0;i<t;i++){
		vector<int> adj[1000];
		int N, K;
		cin >> N >> K;
		for (int j=0;j<N;j++){
			cin>>cost[j];
			indegree[j]=0;
			d[j]=0;
		}
		for (int j=0;j<K;j++){
			int l, r;
			cin >> l >> r;
			adj[l-1].push_back(r-1);
			indegree[r-1]++;
		}
		int w;
		cin>>w;
		result[i]=ACM(N, w-1, adj);
	}
	for (int i=0;i<t;i++){
		cout<< result[i];
		if (i!=t-1){
			cout << endl;
		}
	}
	return 0;
}