#ifndef _LIBVEC_H


#define _LIBVEC_H
#include <stddef.h>

// int vector struct
typedef struct vector {
	size_t size;
	int *data;
} vecint;

// create vector
extern vecint* vecint_create(size_t size);
// free vector
extern void vecint_free(vecint *vec);
// resize vector
extern void vecint_realloc(vecint *vec, size_t size);
// resize vector
extern void vecint_print(vecint *vec);
// sort vector elements
extern void vecint_sort(vecint *vec);

#endif
