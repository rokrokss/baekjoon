#include <iostream>
#include <string.h>
using namespace std;


int main() {
	int t;
	cin >> t;
	int result = 0;
	char word[101];
	int c[101];
	bool* b = new bool[26];
	for (int a=0;a<t;a++){
		if(scanf("%s", word)){};
		int len = strlen(word);
		for (int i=0;i<26;i++){
			b[i]=true;
		}
		char alpha[]="abcdefghijklmnopqrstuvwxyz";
		for (int i=0;i<len;i++){
			for(int j=0;j<26;j++){
				if (word[i]==alpha[j]){
					c[i]=j;
				}
			}
		}
		int i;
		for ( i=0;i<len;i++){
			if (i==0){
				b[c[i]] = false;
			}
			else if(!b[c[i]]&&c[i-1]!=c[i]){
				break;
			}
			else{
				b[c[i]] = false;
			}
		}
		if(i == len){
			result++;
		}
	}
	printf("%d", result);
	return 0;
}