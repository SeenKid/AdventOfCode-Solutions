#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <math.h>

double binaryToDecimal(int *, int);
void bitCounter(char *, int *, int *, int);
char * concat(const char *s1, const char * s2);
char * getInput(char *);
char * keepAllZeroes(char *, int pos);
char * keepAllOnes(char *, int pos);
void resetCounter(int *, int);

int main(void) {
char * str;
char c;
char * binary;
int i;
int * gamma;
int * epsilon;
char * O2rating;
char * CO2rating;

str = getInput("input.txt");

/* splitting the input string in substring with strtok(). */
binary = strtok(str, "\n");
int bits = strlen(binary) - 1;
// create an array long as the binary string itself
int * ctr_Z = (int *) malloc(bits * sizeof(int)); // counter for 0 bits
int * ctr_O = (int *) malloc(bits * sizeof(int)); // counter for 1 bits
gamma = (int *)malloc(bits * sizeof(int));
epsilon = (int *)malloc(bits * sizeof(int));

// initialize all counters values to 0
resetCounter(ctr_Z, bits);
resetCounter(ctr_O, bits);
// proceed to check all the substring
bitCounter(binary, ctr_Z, ctr_O, bits);

// comparing the counters toghether, generating the binary value for gamma & epsilon
for(i = 0; i < bits; i++) {
if(ctr_O[i] > ctr_Z[i]) {
gamma[i] = 1;
epsilon[i] = 0;
} else {
gamma[i] = 0;
epsilon[i] = 1;
}
}
// conversion to decimal - part 1 result
int decimal_gamma = binaryToDecimal(gamma, bits);
int decimal_epsilon = binaryToDecimal(epsilon, bits);
free(gamma);
free(epsilon);
int result = decimal_gamma * decimal_epsilon;
printf("power consumption (part 1): %d\n", result);


/* ----- PART 2 ------ */
/* O2 rating calculation */
O2rating = getInput("input.txt");
char * tmp = (char *)malloc(strlen(O2rating) * sizeof(char));
strcpy(tmp, O2rating);

char * o2data = strtok(tmp, "\n");
bits = strlen(o2data) - 1;
resetCounter(ctr_Z, bits);
resetCounter(ctr_O, bits);
bitCounter(o2data, ctr_Z, ctr_O, strlen(o2data));
i = 0;
while(strlen(O2rating) >= (strlen(o2data) * 2) && i < 12) {
int z = ctr_Z[i];
int u = ctr_O[i];
if(z > u) { // if there are more zeroes than ones in the i column
O2rating = keepAllZeroes(O2rating, i);
// CO2rating = keepAllOnes(O2rating, i);
} else {
/* number of 1 equals number of 0 */
O2rating = keepAllOnes(O2rating, i);
}

strcpy(tmp, O2rating);
o2data = strtok(tmp, "\n");
bits = strlen(o2data) - 1;
resetCounter(ctr_Z, bits);
resetCounter(ctr_O, bits);
bitCounter(o2data, ctr_Z, ctr_O, strlen(tmp));

i++;
}


/* CO2 rating calculation - as for O2 rating with reverse condition for ones and zeroes */
CO2rating = getInput("input.txt");
char * tmp2 = (char *) malloc(strlen(CO2rating) * sizeof(char));
strcpy(tmp2, CO2rating);

char * co2data = strtok(tmp2, "\n");
bits = strlen(co2data) - 1;
resetCounter(ctr_Z, bits);
resetCounter(ctr_O, bits);
bitCounter(co2data, ctr_Z, ctr_O, strlen(co2data));
i = 0;
while(strlen(CO2rating) >= (strlen(co2data) * 2) && i < 12) {
int z = ctr_Z[i];
int u = ctr_O[i];
if(z > u) {
CO2rating = keepAllOnes(CO2rating, i);
} else {
CO2rating = keepAllZeroes(CO2rating, i);
}

strcpy(tmp2, CO2rating);
co2data = strtok(tmp2, "\n");
bits = strlen(co2data) - 1;
resetCounter(ctr_Z, bits);
resetCounter(ctr_O, bits);
bitCounter(co2data, ctr_Z, ctr_O, strlen(tmp2));

i++;
}

int o2[12];
int co2[12];

printf("\nBinary O2 rating: %s", O2rating);
printf("\nBinary CO2 rating: %s\n", CO2rating);

for(i = 0; i < 12; i++){
if(O2rating[i] == '1')
o2[i] = 1;
else
o2[i] = 0;

if(CO2rating[i] == '1')
co2[i] = 1;
else
co2[i] = 0;
}
double res1 = binaryToDecimal(o2, 12);
double res2 = binaryToDecimal(co2, 12);
printf("Decimal O2: %.0f\n", res1);
printf("Decimal CO2: %.0f\n", res2);

printf("life support rating (part2): %.0f", res1 * res2 );

printf("\n");
return 0;
}

void bitCounter(char * binary, int * ctr_Z, int * ctr_O, int bits) {
int i;
while(binary != NULL) {
for(i = 0; i < bits; i++) {
if(binary[i] == '1' ) {
ctr_O[i]++;
} else {
ctr_Z[i]++;
}
}
binary = strtok(NULL, "\n");
}
}


double binaryToDecimal(int * arr, int len) {
double decimal = 0;
int i;
double p;
double exp;
for(i = 0; i < len; i++) {
if(arr[i] == 1){
exp = len - i - 1;
p = pow(2.0, exp);
} else {
p = 0;
}
decimal += p;
}
return decimal;
}

char * concat(const char *s1, const char * s2) {
char * result;

result = (char *)malloc(strlen(s1) + strlen(s2) + 1);
if(result == NULL) {
printf("Error: malloc failed in concat\n");
exit(EXIT_FAILURE);
}
strcpy(result, s1);
strcat(result, s2);
return result;
}

char * getInput(char * file_name) {
FILE * fp;
struct stat st;
char * str;
int sz;
int i;

// check the file dimension
stat(file_name, &st);
sz = st.st_size;

// memory allocation for read the file into a string
str = (char *)malloc(sz * sizeof(char));

// open the file in read only
fp = fopen(file_name, "r");

// chek if the file is correctly open
if(fp) {
// first reading of the file
fscanf(fp, "%c", &str[0]);

while(!feof(fp)) {
for(i = 1; i < sz; i++) {
fscanf(fp, "%c", &str[i]);
}
}
}
fclose(fp); // closing the input file after reading
return str;
}

char * keepAllZeroes(char * str, int pos) {
char * tmp;
char * binary;

// read the first line
binary = strtok(str, "\n");
while(binary != NULL) {
if(binary[pos] == '0') {
binary = concat(binary, "\n");
tmp = concat(tmp, binary);
}
// read the next line, till end of input string.
binary = strtok(NULL, "\n");
}
return tmp;
}

char * keepAllOnes(char * str, int pos) {
char * tmp;
char * binary;

// read the first line
binary = strtok(str, "\n");
while(binary != NULL) {
if(binary[pos] == '1') {
binary = concat(binary, "\n");
tmp = concat(tmp, binary);
}
binary = strtok(NULL, "\n");
}
return tmp;
}


void resetCounter(int * counter, int len){
int i;
for(i = 0; i < len; i++) {
counter[i] = 0;
}
}
