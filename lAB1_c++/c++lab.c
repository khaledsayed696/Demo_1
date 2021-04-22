.........................................Q1....................................

Create a C++ program that asks the user for their favorite number
between 1 and 100. Then read this number from the console.
Suppose the user enters number 24 you want to display the
following to the console.
Amazing.
That's my favorite number too.

.........................................ANswer................................
#include <iostream>
using namespace std;

int main()
{
    int x;

     cout<<"Enter your favorite number between 1 and 100: ";
     cin >> x;
     if(x ==15)
     cout<<" Amazing!! that's my favorite number too ";
     else
      cout<<"no really!! 15 is my favorite number!" ;  
    return 0;
}   

.............................................Q2........................................

Create a C++ program to Reverse an Integer

..............................................Answer.................................


#include <iostream>
using namespace std;

int main() {
    int n, reversedNumber = 0, remainder;

    cout << "Enter an integer: ";
    cin >> n;

    while(n != 0) {
        remainder = n%10;
        reversedNumber = reversedNumber*10 + remainder;
        n /= 10;
    }

    cout << "Reversed Number = " << reversedNumber;

    return 0;
}


....................................Q3............................................

Access Array Elements Using Pointer
...................................ANswer........................................

#include <iostream>
using namespace std;

int main()
{
    int a[5],i,j;
    int *Ptr =a;

    for(i=0;i<5;i++)
    {
           cin>> a[i];
    }
    for(j=0;j<5;j++)
    {
           cout<< Ptr[j];
    }



    return 0;
}   

..........................................Q4.......................................
Display Largest Element of an array

...........................................Answer................................

#include <iostream>
using namespace std;

int main()
{
    int a[4],i ,j,max=0; ;
    
 
cout<< "Enter Total number of element (1 to 100): \n";
 for (i=0 ;i<4 ; i++)
 { 
       cin >> a[i];
 }
 for (j=0 ;j<4 ; j++)
 {
     if (a[j] >max)
     {
         max=a[j];
     }
 }
        
     
       cout <<" Largest number is :" << max;


    return 0;
}   




..................................................Q5...............................
Calculate Average of Numbers Using Arrays
..........................................Answer..............................

#include <iostream>
using namespace std;

int main()
{
    int a[3],i,Ave,sum=0; 
    
 
cout<< "ENter  the number of data : ";
 for (i=0 ;i<3 ; i++)
 { 
       cin >> a[i];
        sum+=a[i];
 }
Ave=sum/3;
       cout <<" AVerage " ;
              cout <<Ave;




    return 0;
}   

....................................................Q6.............................
) Write a program and input two integers in main and pass them to
default constructor of the class. Show the result of the addition of two
numbers.
................................................Answer.............................

#include <iostream>
using namespace std;

class Numbers
{
	private:
		int a;
		int b;
	public:
		
		void readNumbers(void);
		void printNumbers(void);
		int calAddition(void);
};


void Numbers::readNumbers(void)
{
	cout<<"Enter first number: ";
	cin>>a;
	cout<<"Enter second number: ";
	cin>>b;	
}

void Numbers::printNumbers(void)
{
	cout<<"a= "<<a<<",b= "<<b<<endl;
}

int Numbers::calAddition(void)
{
	return (a+b);
}

int main()
{
	
	Numbers num;
	int add; 
	
	num.readNumbers();
	
	add=num.calAddition();
	
	
	num.printNumbers();
	
	cout<<"Addition/sum= "<<add<<endl;
	
	return 0;	
}


.....................................Q7.....................................

) Perform addition operation on complex data using class and object.
The program should ask for real and imaginary part of two complex
numbers, and display the real and imaginary parts of their sum.

.....................................Answer....................................

#include <iostream> 

using namespace std;

class complex_number
{
   public :
      int real, imag;
};

int main()
{
   complex_number num1, num2, sum;

  
   cout << "Enter real and imaginary parts of first complex number:"<<endl; 
   cin >> num1.real >> num1.imag;

   
   cout << "Enter real and imaginary parts of second complex number:"<<endl; 
   cin >> num2.real >> num2.imag;

  
   sum.real = num1.real + num2.real;
   sum.imag = num1.imag + num2.imag;

   
   if ( sum.imag >= 0 )
      cout << "Sum of two complex numbers = " << sum.real << " + " << sum.imag << "i";
   else
      cout << "Sum of two complex numbers = " << sum.real << " - " << sum.imag << "i";

   return 0;
}


