#include<stdio.h>
#include<stdlib.h>
#include"tool.h"

#define ls 655U
#define pwd 3495U
 
 
int main(){

    unsigned int directive_hash;
    directive_hash=hash_string("pwd");
    switch (directive_hash)
    {
        case ls:
        puts("ls");
        break;
        case pwd:
        puts("pwd");
        break;

        default:
        break;
    }

    return 0;

}