#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	char c[105];
	scanf("%s", c);
	for (int i=0;i<101;i++){
		if(c[i] == '\0' || c[i]==EOF){
			break;
		}
		printf("%c", c[i]);
		if ((i+1)%10==0){
			printf("\n");
		}
	}
	return 0;
}