class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)
        for first , last , seat in bookings:
            answer[first-1] += seat
            answer[last] -= seat
        answer.pop()
        for i in range(1 ,  len(answer)):
            answer[i] += answer[i-1]
        return answer
        
            