#include <stdio.h> 
int main() {
	int a = 2; 
	int b = 2; 
	int c = a + b;

       	printf("C says: Hello, World!\n"); 
	printf("%d + %d = %d\n", a,b,c); 
	
 	char * listOfUsers[] = {"users1", "users2", "users3"}; 
	printf("size of the list: %ld", sizeof(listOfUsers));
	for(int i = 0; i < sizeof(listOfUsers)/sizeof(char *); i++) {
		printf("%s\n", listOfUsers[i]);
	}
	return 0;
}
