class Solution {
public:
    const int MOD = 1e9 + 7;
    
    long long int power(long long int x, long long int y){
        long long int res = 1;
        while(y){
            if(y%2==1) res =(res * x) % MOD;
            x = (x*x) % MOD;
            y /= 2;
        }
        return res;       
    }


    int countGoodNumbers(long long n) {        
        long long int odd = n/2;
        long long int even = n - odd;

        return (power(5, even) * power(4, odd))%MOD;
    }
};