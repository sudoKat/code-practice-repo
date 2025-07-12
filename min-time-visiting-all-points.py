
'''
1266. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one 
unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but 
these do not count as visits.

'''
class Solution:

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:

        time_sum = 0

        'Calculate the distance, between each set of two points'
        for i in range(len(points)-1):
            time_sum += Solution().getdistance(points[i],points[i+1] )        
        return time_sum
    
    'Function to get distance between the start and stop point'
    def getdistance(self, start:list[int], stop:list[int]) -> int:
         
        'Since it takes only 1 second to travel diagonally, maximize this first.'
        max_diagonal = min(abs(start[0] - stop[0]), abs(start[1] - stop[1]))
        time = max_diagonal

        if abs(start[0] - stop[0]) ==  abs(start[1] - stop[1]):
            'If the diff between x and y coordinates is the same, only diagonal travel is needed to '
            'reach the stop point'
            return time
        else:
            'if not, then by this time, 1 coordinate will be satisfied by diagonal travel and we get '
            'the diff of the remaining coordinate to complete the remaining distance'
            return time + abs(abs(start[0] - stop[0]) -  abs(start[1] - stop[1]))
                
        