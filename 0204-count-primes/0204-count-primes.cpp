class Solution {
public:
    vector<bool> generated(int n){
        vector<bool> primes(n+1 , true);
        int start = 2;
        primes[0] = false;
        primes[1] = false;
        int sqrtval = ceil(sqrt(n));
        for(long long i=2; i<sqrtval; i++){
            if(primes[i] == true){
                for(long long j = i*i; j<n; j+=i){
                    primes[j] = false;
                }
            }
        }
        
        return primes;
         
        
    }
    int countPrimes(int n) {
        int count = 0;
        vector<bool> primes = generated(n);
        for(int i=0; i<primes.size()-1; i++){
            if(primes[i]) count++;
        }
        return count;
        
    }
};