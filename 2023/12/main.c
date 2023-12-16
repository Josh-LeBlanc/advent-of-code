#include <stdio.h>

int main(int argc, char ** argv){
    
    FILE * input = fopen("test.in", "r");

    char string[256];
    
    while(fscanf(input, "%s", string) == 1)
    {

        continue;

    }
    
    fclose(input);
    return 0;
}
