//{ Driver Code Starts
//Initial Template for C++

#include <iostream>
using namespace std;


// } Driver Code Ends
//User function Template for C++

void reverse_dig(int &a,int &b)
{
    int reverseA = 0;
    int reverseB = 0;
    while(a!=0 || b!=0){
        if(a != 0){
            int lastD = a%10;
            reverseA = reverseA * 10 + lastD;
            a = a/10; 
            
        }
        if(b != 0){
            int lastD = b%10;
            reverseB = reverseB * 10 + lastD;
            b = b/10; 
            
        }
    }
    a = reverseA;
    b = reverseB;
    
    //Add your code here.
}
void swap(int &a,int &b)
{
    int temp = a;
    a = b;
    b=  temp;
    //Add your code here.
}


//{ Driver Code Starts.

int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
        int a, b;
	    cin>>a>>b;
	
	    reverse_dig(a,b);
	    swap(a,b);
	    cout<<a<<" "<<b<<endl;
    }
	return 0;
}
// } Driver Code Ends