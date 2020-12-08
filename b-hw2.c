#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROW 12
#define COL 6
#define MAX 25

int costMatrix[ROW][COL]=
  {
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
	{500,200,500,500,200,500},
  };
  
void initialSeats(char flight[][COL],int count);
void displayMenu(void);
int menuErrorCheck(int option);
void printFlightMap(char flight[][COL]);
int loginMatch(int passcode,int adminPasscode);
int getTotalRevenue(char f1[][COL],char f2[][COL],char f3[][COL]);
void flightMenu();
void seatReservation(char flight[][COL]);
void printMessage(char name[],char num[]);

//==========================================================================

int main(void)
{
	srand((unsigned)time(NULL)); //Seeds rand in main
	int randomNum = rand() % 20 + 1;       //sets bounds for random numbers
	
	int adminPasscode = 105018;				//Sets admin password
	
	char flight1[ROW][COL];             //Initializes flights and randomizes them
	initialSeats(flight1,rand() % 20+1); 
	char flight2[ROW][COL];
	initialSeats(flight2,randomNum);
	char flight3[ROW][COL];
	initialSeats(flight3,randomNum);
	
	int inputSize;                //Variable for menu choice
	int flightOption;             //Variable for second menu
	int passcode;                 //Variable for password inputted by user
	
	while(inputSize != 3){        //Loops the program until user selets option 3
		displayMenu();            //Displays menu
		scanf("%d", &inputSize);  //Takes menu choice
	
			while(menuErrorCheck(inputSize) == 0){       //Error checking for menu
				printf("Please enter a valid choice");
				scanf("%d", &inputSize);
			}
			
			
			
		if(inputSize == 1){                             //Admin mode- prompts for passcode and checks it
			printf("Enter admin passcode:");
			scanf("%d",&passcode);
			loginMatch(passcode, adminPasscode);
				while( loginMatch(passcode, adminPasscode) == 0){
					printf("Incorrect passcode! Please try again:");
					scanf("%d",&passcode);
					loginMatch(passcode, adminPasscode);
				}
			printf("Printing the map of flight Columbia to Miami\n");     //prints all 3 seat maps of planes
			printFlightMap(flight1);

			printf("\nPrinting the map of flight Columbia to Nashville\n");
			printFlightMap(flight2);

			printf("\nPrinting the map of flight Columbia to Las Vegas\n");
			printFlightMap(flight3);
			
			printf("\nThe total earnings from all the flights: $ %d\n", getTotalRevenue(flight1,flight2,flight3)); //puts total amount of money earned in a printf
			printf("You are logged out now!\n");    //Returns to  beginning of loop   
			}
			
			
			
			else if(inputSize ==2){          //if statement for booking a flight
				flightMenu();
				printf("\nChoose a flight:");
				scanf("%d",&flightOption);                         //prompts user for which flight and error checks
					while(menuErrorCheck(flightOption) == 0){
						flightMenu();
						printf("\nChoose a valid flight:");
						scanf("%d",&flightOption);
					}
				
				
				
				if (flightOption == 1){                         //if and if else statements for reserving a flight
					printFlightMap(flight1);
					seatReservation(flight1);
				}
				
				else if (flightOption == 2){
					printFlightMap(flight2);
					seatReservation(flight2);
				}
				
				else if (flightOption == 3){
					printFlightMap(flight3);
					seatReservation(flight3);
				}
				
				
			}
		}
		
		printf("Terminating the Program.\n");                        //Exit message
		printf("Thank you for using Mizzou Airline Booking System!\n");
		
	}




//==========================================================================

void initialSeats(char flight[ROW][COL], int count)
{
	
	int x;
	int y;
	int z;
	
	for(x = 0; x < ROW; x ++){
		
		for(y = 0; y < COL; y++){
			
			flight[x][y] = 'O';
		}
	}
	
	for(z = 0; z < count; z++){
		int row = rand()%ROW;
		int col = rand()%COL;
		if(flight[row][col] == 'X'){
			z--;
		}
		if( flight[row][col] == 'O'){
			flight[row][col] = 'X';
		}
	}

}

//==========================================================================

void displayMenu()
{
	printf("*******WELCOME TO MIZZOU AIRLINE BOOKING SYSTEM********\n");
	printf("\n1.) Admin Login\n");
	printf("2.) Reserve a seat\n");
	printf("3.) Exit\n");
	printf("Choose an option:");
}
//==========================================================================

int menuErrorCheck(int option)
{
	if (option < 1 || option > 3){
		return(0);
	}
		else{
			return(1);
		}
}

//==========================================================================

void printFlightMap(char flight[ROW][COL])
{
	for(int x=0; x < ROW; x++){
		
		for(int y=0; y < COL; y++){
			
			printf("%2c", flight[x][y]);
		}
	printf("\n");
	}
}
//==========================================================================

int loginMatch(int passcode,int adminPasscode){
	if ( passcode == adminPasscode){
		return(1);
	}
	else{
		return(0);
	}
}
	
//==========================================================================

int getTotalRevenue(char f1[ROW][COL],char f2[ROW][COL],char f3[ROW][COL])
{
	int totalCost = 0;
	
	for(int x=0; x < ROW; x++){
		
		for(int y=0; y < COL; y++){
			
			if (f1[x][y] == 'X'){
			totalCost += costMatrix[x][y];
			}
		}
	}
	
	for(int x=0; x < ROW; x++){
		
		for(int y=0; y < COL; y++){
			
			if (f2[x][y] == 'X'){
			totalCost += costMatrix[x][y];
			}
		}
	}
	
	for(int x=0; x < ROW; x++){
		
		for(int y=0; y < COL; y++){
			
			if (f3[x][y] == 'X'){
			totalCost += costMatrix[x][y];
			}
		}
	}

return totalCost;

}
	
//==========================================================================

void flightMenu()
{
	printf("1.)COU ----> MIA\n");
	printf("2.)COU ----> BNS\n");
	printf("3.)COU ----> LAS\n");
}
//==========================================================================

void seatReservation(char flight[ROW][COL]){
	int x ;
	int y ;
	int loop = 0;
	
	while(loop == 0){ 
	printf("Which seat row do you want?:");
	scanf("%d", &x);
		while(x < 0 || x > 11){
			printf("Seat rows are 0 to 11\n");
			printf("Try again. Which seat row do you want?:");
			scanf("%d", &x);
		}
		
		
	printf("\nWhich seat column do you want?:");
	scanf("%d", &y);
		while(y < 0 || y > 5){
			printf("Seat columns are 0 to 5\n");
			printf("Try again. Which seat column do you want?:");
			scanf("%d", &y);
		
		}
		if(flight[x][y] == 'X'){
			printf("Seat taken! Please select an open seat.\n");
		}
			else
			{
				flight[x][y] = 'X';
				printf("\nFlight successfully booked!\n"); //Confirmation message
				loop ++;
			}
	}
}


//==========================================================================
