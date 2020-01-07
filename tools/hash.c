#include<stdio.h>
#include"../tool.h"

 
int main(int argc ,char * argv[]){

    if(argc==2){
       printf("%u\n",hash_string(argv[1]));
    }
    return 0;

}