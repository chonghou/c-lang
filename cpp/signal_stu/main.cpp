#include <stdio.h>
#include<signal.h>
#include<unistd.h>

sig_atomic_t signaled = 0;
 
void my_handler (int param)
{
  signaled = 1;
}

void  handler(int signo)//自定义一个函数处理信号
{
    printf("catch a signal:%d\n:",signo);
}


int main(int argc, char** argv)
{
    // void (*prev_handler)(int);
    // prev_handler = signal (SIGINT, my_handler);
    // raise(SIGINT); //中断信号
    // printf ("signaled is %d.\n",signaled);



    //处理信号的三种方式
    //SIG_IGN 信号处理方式为忽略，ctrl+c产生的信号编号为2，若要停止进程可用Ctrl+z（SIGQUIT）
    // signal(2,SIG_IGN);
    // while(1)
    // {
    //     printf("2333\n");
    //     sleep(1);
    // }

    //当执行程序时，同样是死循环，此时按下Ctrl+C进程停止，因为我们对2号信号采取默认动作处理，系统默认2号信号终止进程
    // signal(2,SIG_DFL);
    // while(1)
    // {
    //     printf("2333\n");
    //     sleep(1);
    // }


    // signal(2,handler);
    // while(1)
    // {
    //     printf("2333\n");
    //     sleep(1);
    // }
    signal(SIGABRT,handler);
    signal(SIGFPE,handler);
    if(1){
        1.0/0;
        return -1;
    }
    

    return 0;
}