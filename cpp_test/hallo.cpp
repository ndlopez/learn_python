#include<iostream>
#include<string>
using namespace std;
struct{
	int mynum;
	string mystr;
}myStruct;

int myFunc(int x, int y){return x*y;}

int main(){
	string greet = "Hallo";
	greet = greet + " work";
	cout << greet << greet.length() << endl;
	string usrInput;
	for (int i =0;i<2;i++){
		cout << "Type in sth: ";
		cin >> usrInput; //considers one-single word input
		cout << "You typed: " << usrInput << endl;
		usrInput = "";
	}
	cout << "Type in sth: ";
	getline(cin,usrInput);
	cout << "Again, you typed: " << usrInput << endl;
	int time = 11;
	string result = (time < 18)? "Good day.":"Good evening";
	cout << result;
	int myNum[4] = {10,23,53,76};
	cout << sizeof(myNum)/sizeof(int) << endl;

	//Assign values to members of struct
	myStruct.mynum = 20;
	myStruct.mystr = "Half the time the world...";
	cout << myStruct.mynum << "\n" << myStruct.mystr << endl;
	//refs
	string food = "pizza";
	cout << food << "and " << &food << endl;
	//pointers
	string* pFood = &food;
	cout << food << "and " << pFood << endl;
	//Func
	cout << "3 * 4 = " << myFunc(3,4) << endl;
}
