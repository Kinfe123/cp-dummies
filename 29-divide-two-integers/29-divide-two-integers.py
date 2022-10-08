class Solution:
    
    def divide(self, dividend, divisor):
         
        
        dividend1, divisor1 = abs(dividend), abs(divisor)
        quotient = 0
        while dividend1 >= divisor1:
            temp, i = divisor1, 1
            while dividend1 >= temp:
                dividend1 -= temp
                temp += temp
                quotient += i
                i += i
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            quotient = -quotient
        return min(max(quotient, -pow(2,31)),pow(2,31)-1)
