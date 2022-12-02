#include "libvec.h"
#include <stdlib.h>
#include <stdio.h>

vecint* vecint_create(size_t size){
	vecint* vec =(vecint *) malloc(sizeof(size_t) + sizeof(int*));
	vec->size = size;
	vec->data =(int*) malloc(sizeof(int)*size);
	return vec;
}

void vecint_free(vecint *vec){
	free(vec->data);
	vec->data = NULL;
	free(vec);
	vec = NULL;
}

void vecint_realloc(vecint *vec, size_t size){
	vec->size = size;
	vec->data = (int *) realloc(vec->data, size);
}

void vecint_print(vecint *vec){
	for(long unsigned int i=0; i<vec->size; i++){
		printf("%d ", vec->data[i]);
	}
	printf("\n");
}

#define SORT 0

void vecint_sort(vecint *vec){

#if SORT==0
	// cascade sort
	for(long unsigned int i=0; i<vec->size; i++){
		for(long unsigned int j=0; j<i; j++){
			if(vec->data[j] > vec->data[i]){
				vec->data[i] ^= vec->data[j];
				vec->data[j] ^= vec->data[i];
				vec->data[i] ^= vec->data[j];
			}
		}
	}
#elif SORT==1
	// merge sort
#elif SORT==2
	// heapsort
#elif SORT==3
	// quick sort
#elif SORT==4
	// shell sort
#elif SORT==5
#endif


}
