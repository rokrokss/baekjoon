#include <iostream>
#include <string.h>
using namespace std;

int main() {
	char alpa[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char s[16];

	int c[16];
	scanf("%s",s);
	int len = strlen(s);
	for (int i=0;i<len;i++){
		for(int j=0;j<26;j++){
			if(s[i]==alpa[j]){
				if(j<18) {
					c[i] = j / 3 + 3;
				}
				else if(j>=18&&j<25){
					c[i] = (j-1)/3+3;
				}
				else{
					c[i] = 10;
				}
			}
		}
	}
	int result = 0;
	for (int i=0;i<len;i++){
		result = result + c[i];
	}
	cout << result;
	return 0;
}