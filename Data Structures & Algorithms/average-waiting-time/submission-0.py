class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0]
        end = start + customers[0][1]
        wait = end - start
        avg = wait
        cust = customers[1:]
        for l, r in cust:
            if l > end:
                start = l
            else:
                start = end
            print("started at", start)
            end = start + r
            print("ended at", end)
            wait = end - l
            print("waited", wait)
            avg += wait
        return avg/len(customers)