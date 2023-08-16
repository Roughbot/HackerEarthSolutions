#include <iostream>
#include <string.h>
using namespace std;
int main() {
	string name;
	
	cin >> name;
	int z = 0, o = 0;

	for(char i : name){
		if (i == 'z'){
			z = z + 1;
		}
		else if(i == 'o'){
			o = o + 1;
		}
	}
	z*2 == o? cout<<"Yes"<<endl:
	cout<<"No"<<endl;		


	return 0;
}
