#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
	char a[101] = {'\0'};
	int result[26];
	for (int i=0; i<26; i++){
		result[i]=-1;
	}
	scanf("%s",a);
	for (int i=101;i>=0;i--){
		for (int j=0;j<26;j++){
			if(alphabet[j]==a[i]){
				result[j]=i;
			}
		}
	}
	for (int i=0; i<26; i++){
		printf("%d ", result[i]);
	}
	return 0;
}