#include <stdio.h>

int main()
{
int vals[2][13] = {0}, i, k=11, g = 0, e = 0;
char num[13];

while(scanf("input.txt", num) > 0)
for(i = 0; i < 12; i++)
(num[i] == '0') ? vals[0][i]++ : vals[1][i]++;

for(i = 0; i < 12; i++, k--)
if(vals[1][i] > vals[0][i]) g+=1<<k;
e = g;

for(i = 0; i < 12; i++)
e = (e ^ (1 << i));

printf("%d",g*e);
}