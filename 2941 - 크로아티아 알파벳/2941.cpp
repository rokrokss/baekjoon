#include <iostream>
#include <string.h>
using namespace std;

int main() {
	char s[102]={'\0'};
	scanf("%s",s);
	int len = strlen(s);
	int result = len;
	for (int i=0;i<len;i++){
		char curr = s[i];
		char next = s[i+1];
		if(curr=='c'){
			if (next=='-'||next=='='){
				result--;
			}
		}
		else if(curr=='d'){
			if(next=='z'&&s[i+2]=='='){
				result=result-1;
			}
			else if(next=='-'){
				result--;
			}
		}
		else if(curr=='l'){
			if(next=='j'){
				result--;
			}
		}
		else if(curr=='n'){
			if(next=='j'){
				result--;
			}
		}
		else if(curr=='s'){
			if(next=='='){
				result--;
			}
		}
		else if(curr=='z'){
			if(next=='='){
				result--;
			}
		}
	}
	cout << result;
	return 0;
}