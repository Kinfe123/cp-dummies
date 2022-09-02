class Solution(object):
    def nextGreaterElements(self, arr):
        s = [];
        n = len(arr)
        # Initialize nge[] array to -1
        nge = [-1] * n;

        i = 0;

        # Traverse the array
        while (i < 2 * n) :

            # If stack is not empty and
            # current element is greater
            # than top element of the stack
            while (len(s) != 0 and arr[i % n] > arr[s[-1]]) :

                # Assign next greater element
                # for the top element of the stack
                nge[s[-1]] = arr[i % n];

                # Pop the top element
                # of the stack
                s.pop();

            s.append(i % n);
            i += 1;
        return nge


