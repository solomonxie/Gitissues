---
layout: post
title: "Interval of Convergence"
date: 2017-08-03 03:32:44
image: '/assets/img/'
description: 'First steps to use this template'
tags:
    - infinite series 
    - convergence 
    - series
categories:
    - calculus
    - I love Jekyll
---

# `Interval of Convergence`
When we see the series as a function, we can actually specify an interval for the function so that the series certainly converges over this interval.

[`►Jump over to have practice at Khan academy: Interval of convergence`](https://www.khanacademy.org/math/ap-calculus-bc/bc-series/modal/e/find-interval-of-convergence)

The method is kind of like finding the interval of an ordinary function:
- The `term` of series **can't** be `0`, so set `a_n ≠ 0` and solve  it to get the condition.
- Take some `convergence tests`, etc. `ratio test`.
- Calculate to get the condition that makes the **test** passes.
- Substitute the `endpoints` of the interval back in the function and see if it also converges.


### Example
![image](https://user-images.githubusercontent.com/14041622/42081333-c02988b6-7bb7-11e8-90f0-1ba22b2c8610.png)
Solve:
- The term **can't be** zero, so:
![image](https://user-images.githubusercontent.com/14041622/42081873-2b7b6b38-7bb9-11e8-965d-d7c717510360.png)
- And further more, take a `ratio test` which makes it converges:
![image](https://user-images.githubusercontent.com/14041622/42081958-5f7a6204-7bb9-11e8-86ea-3393b5cfafa9.png)
- Calculate the `ratio test` to get the interval:
![image](https://user-images.githubusercontent.com/14041622/42082079-a471ddf6-7bb9-11e8-974d-cbc19ad7948b.png)
- Get the interval for `x`:
![image](https://user-images.githubusercontent.com/14041622/42082091-aba91cb0-7bb9-11e8-9e8d-0b0b1d879446.png)
- Test the `endpoints` for this interval:
![image](https://user-images.githubusercontent.com/14041622/42082232-0872485e-7bba-11e8-8baf-bd7423dde200.png)
- In conclusion, the `interval of convergence` is:
![image](https://user-images.githubusercontent.com/14041622/42082258-1aa5ede6-7bba-11e8-9b71-68ab89885a47.png)
