#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	int t;
	cin >> t;
	char s[81];
	int score = 1;
	int total = 0;
	for (int a=0; a<t; a++){
		scanf("%s", &s);
		for(int i=0; s[i]!='\0';i++){
			if (s[i]=='O'){
				total = total + score;
				score ++;
			}else{
				score = 1;
			}
		}
		printf("%d\n", total);
		total = 0;
		score = 1;
	}
	return 0;
}