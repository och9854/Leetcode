# Intro to DP

---

## When to use DP

---

<ol>
    <li>
    The first characteristic that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something.</li>
    <li>
    The second characteristic that is common in DP problems is that future "decisions" depend on earlier decisions.
    </li>

</ol>

Ex: [House Robber](https://leetcode.com/problems/house-robber/), [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

- To summarize: if a problem is asking for the maximum/minimum/longest/shortest of something, the number of ways to do something, or if it is possible to reach a certain point, it is probably greedy or DP. With time and practice, it will become easier to identify which is the better approach for a given problem. Although, in general, if the problem has constraints that cause decisions to affect other decisions, such as using one element prevents the usage of other elements, then we should consider using dynamic programming to solve the problem. These two characteristics can be used to identify if a problem should be solved with DP.

# Strategic Approach to DP

---
