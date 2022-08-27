/*Battleship game?*/
#include<iostream>
using namespace std;

int main(){
	//put 1 to indicate there is a ship
	bool ships[4][4]={
		{0,1,1,0},
		{0,0,0,0},
		{0,0,1,0},
		{0,0,1,0}};
	//keep track of hits
	int hits = 0;
	int turnNumber = 0;
	//allow player to keep going until 
	//they have hit all four ships
	while (hits < 4){
		int row,col;
		cout << "Selecting coords ..."<<endl;
		//ask player for row
		cout << "choose row number 0~3: ";
		cin >> row;
		//ask player for col
		cout << "choose col number 0~3: ";
		cin >> col;
		//check if ship exists in those coords
		if (ships[row][col]){
			//if player hit a ship rm and chg value to 0
			ships[row][col] = 0;
			hits++;
			//tell player hit a ship
			cout << "You sunk my battle ship " << (4-hits)<< " left\n\n";
		}else{
		//Tell player that it missed
		cout << "Missed\n\n";}
		turnNumber++;
	}

	cout << "Victory!\n";
	cout << "You won in " << turnNumber << " turns";
	return 0;
}
