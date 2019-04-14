#include <iostream>
#include <algorithm>
#include <cmath>
#include <string.h>
using namespace std;


int main() {
	char s[1000001];
	if(scanf("%s", s)){};
	int length = strlen(s);
	int* conv = new int[length];
	char A[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char a[]="abcdefghijklmnopqrstuvwxyz";
	int check[26]={0};
	bool Q = true;
	for (int i =0; i<length; i++){
		for (int j=0;j<26;j++){
			if(s[i]==A[j]||s[i]==a[j]){
				check[j]++;
				conv[i]=j;
			}
		}
	}
	int dp=0;
	int result;
	for (int i=0;i<26;i++){
		if(dp<check[i]){
			Q = false;
			dp = check[i];
			result = i;
		}
		else if(dp==check[i]){
			Q = true;
		}
	}
	if (Q){
		printf("?");
	}
	else{
		printf("%c", A[result]);
	}
	return 0;
}