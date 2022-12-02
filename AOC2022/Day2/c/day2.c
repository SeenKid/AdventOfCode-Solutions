#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

#include "./lib/libvec.h"
#define DEBUG 0

// a roc b paper c scissors
// response 2nd collumn

int main(int argc, char* argv[]){
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	long unsigned int head = 0;
	fp = fopen(argv[1], "r");
	while((read = getline( &line, &len, fp)) != -1){
		int add = 0;
	#if DEBUG
		printf("%s", line);
	#endif
		line[0]-=65;
		line[2]-=88;

		add += line[2]+1;

		if(line[2]==line[0]){
			add +=3;
		} else if (line[2]==(line[0]+1)%3){
			add +=6;
		}
	#if DEBUG
		printf("--%d %d head: %d\n", (int)line[0], (int) line[2], add);
	#endif
		head += add;
		
	}

	printf("%ld\n", head);
	return 0;
}

#if 0 // part 2
int main(int argc, char* argv[]){
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	long unsigned int head = 0;
	fp = fopen(argv[1], "r");
	while((read = getline( &line, &len, fp)) != -1){
		int add = 0;
	#if DEBUG
		printf("%s", line);
	#endif
		line[0]-=65;
		line[2]-=88;

		add += line[2]*3;
		switch(line[2]){
			case 0:
				add +=(line[0]+2)%3 +1;
			break;
			case 1:
				add +=line[0]+1;

			break;
			case 2:
				add +=(line[0]+1)%3 +1;

			break;
		}

	#if DEBUG
		printf("--%d %d head: %d\n", (int)line[0], (int) line[2], add);
	#endif
		head += add;
		
	}

	printf("%ld\n", head);
	return 0;
}
#endif
