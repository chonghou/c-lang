#include<vector>
#include<iostream>
#include<functional>



class Caller {

    public:
  template<class T> void addCallback(T* const object, void(T::* const mf)(bool,int))
  {
    using namespace std::placeholders; 
    callbacks_.emplace_back(std::bind(mf, object, _1, _2));
  }
  void addCallback(void(* const fun)(bool,int)) 
  {
    callbacks_.emplace_back(fun);
  }
  void callCallbacks(bool firstval, int secondval) 
  {
    for (const auto& cb : callbacks_)
      cb(firstval, secondval);
  }
private:
  std::vector<std::function<void(bool,int)>> callbacks_;
};

class Callee {
    public:
  void MyFunction(bool a,int b){
      std::cout<<a<<" "<<b<<std::endl;
  }

 
};

void MyRegularFunction(bool a, int b){
    std::cout<<a<<b;
}


int main(){

    Caller *ptr=new Caller;
Callee c;
    //or to add a call back to a regular function
    ptr->addCallback(&MyRegularFunction);
    ptr->addCallback(&c,&Callee::MyFunction);
    ptr->callCallbacks(true,4);

    delete ptr;
    return 0;
}



