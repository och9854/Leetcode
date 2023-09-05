class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Answer
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]

        # Feedback
        '''
        - The way to solve was similar
        - Could not think when there are same points
        - Practice lambda more
        '''


        # Tried
        # # init
        # answer_dict = {}
        # ans = []
        # # Iterate and add in dictionary
        # for x,y in points:
        #     answer_dict[(x,y)] = x*x + y*y
        # print(answer_dict)
        # sorted_dict = sorted(answer_dict, key=answer_dict.get, reverse=False)
        # print(sorted_dict)

        # for i in range(k):
        #     ans.append(list(sorted_dict[i]))


        # print(ans)
        # return ans
