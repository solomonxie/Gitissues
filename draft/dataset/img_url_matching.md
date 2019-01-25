# Calculus Basics 微积分基础
> Mainly some basic Calculus knowledges for Machine Learning

## Study resources
- [ ] [Khan academy: AP Calculus AB](https://www.khanacademy.org/mission/ap-calculus-ab)
- [ ] [Mathispower4u](http://www.mathispower4u.com/calculus.php)
- [ ] [Kristan King: Calculus I](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BOYyyC-Gunxrh-jYnSfsQy0)
- [ ] [Kristan King: Calculus II](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BMdeuQfJDVRJ5DPMduSzVow)
- [ ] [Kristan King: Calculus III](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BMObozItpbiZ8f2pjf3qS9M)
- [ ] [The Organic Chemistry Tutor: New Calculus Playlist](https://www.youtube.com/playlist?list=PL0o_zxa4K1BWYThyV4T2Allw6zY0jEumv)
- [ ] [MIT OCW 18.01SC: Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/index.htm)
- [ ] [MIT OCW 18.02SC: Multivariable Calculus](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)

## Practice To-do List (Linked with Unit tests)
- [x] [Limits and continuity](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/modal/test/ab-limits-continuity-unit-test)
- [x] [Derivatives introduction](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/test/ab-derivative-intro-unit-test)
- [x] [Derivative rules](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/test/ab-derivative-rules-unit-test)
- [x] [Advanced derivatives](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/test/ab-derivatives-advanced-unit-test)
- [x] [Existence theorems](https://www.khanacademy.org/math/ap-calculus-ab/ab-existence-theorems/modal/test/ab-existence-theorems-unit-test)
- [x] [Using derivatives to analyze functions](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/test/ab-derivatives-analyze-functions-unit-test)
- [ ] [Applications of derivatives](https://www.khanacademy.org/math/ap-calculus-ab/ab-applications-derivatives/modal/test/ab-applications-derivatives-unit-test)
- [ ] Accumulation and Riemann sums
- [ ] Antiderivatives and the fundamental theorem of calculus
- [ ] Differential equations
- [ ] Applications of definite integrals

## Study goals 
- [ ] Limits
- [ ] Derivatives




# `Limits`
> Limits are all about approaching.
And the entire Calculus is built upon this concept.


# `Function's Continuity`

Pencil Definition: 
**IF YOU CAN DRAW THE FUNCTION WITH A PENCIL WITHOUT PICKING UP THE PENCIL, THEN THE FUNCTION IS A CONTINUOUS FUNCTION**


# Strategy in finding Limits

[Refer to Khan academy.](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/ab-limit-strategy/a/limit-strategies-flow-chart)

![image](https://user-images.githubusercontent.com/14041622/40041663-65775634-5851-11e8-9382-e6de982dc496.png)



# `Limits at infinity`

No matter why kinds of Limits you're looking for, 
to understand it better, 
the best way is to read the `Step-by-Step Solution` from `Symbolab`:
[Limit Calculator from Symbolab.](https://www.symbolab.com/solver/limit-calculator/%5Clim_%7Bx%5Cto%5Cinfty%7D%5Cleft(%5Cfrac%7B6x%5E%7B2%7D-x%7D%7B%5Csqrt%7B9x%5E%7B4%7D%2B7x%5E%7B3%7D%7D%7D%5Cright))

## `Rational functions`
> The KEY point is to look at the powers & coefficients of Numerator & Dominator.
Just the same with `Finding the Asymptote`.

[Refer to previous note on the `How to find Asymptote`](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-374894945).

![image](https://user-images.githubusercontent.com/14041622/40049084-5303489a-5866-11e8-9ba5-d2ffe6045955.png)

Example:
![image](https://user-images.githubusercontent.com/14041622/40048425-c4959c30-5864-11e8-947d-cd5c59375f72.png)
Solve:


## `Quotients with square roots`
> The KEY point is to calculate both `numerator & dominator`, then calculate the limit of EACH term with in the square root.

Example:
![image](https://user-images.githubusercontent.com/14041622/40047707-c2a05052-5862-11e8-805a-5d8c6ca98d47.png)
Solve:
[Refer to Symbolab step-by-step solution.](https://www.symbolab.com/solver/limit-calculator/%5Clim_%7Bx%5Cto%5Cinfty%7D%5Cleft(%5Cfrac%7B6x%5E%7B2%7D-x%7D%7B%5Csqrt%7B9x%5E%7B4%7D%2B7x%5E%7B3%7D%7D%7D%5Cright))
- Divide by **highest** dominator power to get:
![image](https://user-images.githubusercontent.com/14041622/40047885-48fdaf46-5863-11e8-85b8-118c09272fbf.png)
- Calculate separately the limit of `Numerator` & `Dominator`:
![image](https://user-images.githubusercontent.com/14041622/40047966-896c2990-5863-11e8-924e-8898d747fafd.png)
- Calculate the `Square root`: Need to find limits for **EACH** term **inside** the square root.
![image](https://user-images.githubusercontent.com/14041622/40048191-2dc755d2-5864-11e8-8733-e91ca609069f.png)
![image](https://user-images.githubusercontent.com/14041622/40048201-330160c4-5864-11e8-9b7b-b98fbae043f5.png)
![image](https://user-images.githubusercontent.com/14041622/40048216-3c8970b4-5864-11e8-8496-68e2e638df1d.png)
- Then get the result easily.

## `Quotients with trig`
> The KEY point is to apply the **`Squeeze theorem`**, and it is a MUST.

Example:
![image](https://user-images.githubusercontent.com/14041622/40047015-e86fb63a-5860-11e8-9f72-b97d62f785c2.png)
Solve:
- Know that `-1 ≦ cos(x) ≦ 1`, so we can tweak it to apply the `squeeze theorem` to get its limit.
- Make the inequality to: `3/-1 ≦ 3/cos(x)/-1 ≦ 3/1`
- Get that right side `3/-1 = -1` and left side `3/1 =1` is not equal.
- So the limit doesn't exist.

**Easier solution steps**:
- Know the inequality `-1 ≦ cos(x) ≦ 1`
- Replace `cos(x)` to ` ±1` in the equation, `3/±1`.
- Calculate limits of two sides.
- If the results are exactly the same, then the limit is the result; Otherwise the limit doesn't exist.

Example 2:
![image](https://user-images.githubusercontent.com/14041622/40047463-2181c778-5862-11e8-8658-d439cdcecf65.png)
Solve:
- Know that `-1 ≦ sin(x) ≦ 1`
- Replace `sin(x)` as `±1`
- Left side becomes `(5x+1)/(x-5)`, right side becomes `(5x-1)/(x-5)`
- Both sides' limits are `5`, so the limit exists, and is `5`.


# `All types of discontinuities`

[Refer to Mathwarehouse: What are the types of Discontinuities?](http://www.mathwarehouse.com/calculus/continuity/what-are-types-of-discontinuities.php)

## `Jump Discontinuities`
> A `Jump discontinuity` occurs at some point, the `left side limit` is DIFFERNT with the `right side limit`.

![image](https://user-images.githubusercontent.com/14041622/40050621-8b4da930-586a-11e8-909f-424af8b6c04e.png)
We see that clearly:
![image](https://user-images.githubusercontent.com/14041622/40050642-9cbaa704-586a-11e8-9c82-adc8f0032a15.png)


## `Removable Discontinuities`
> A `removable discontinuity` occurs at some point, both `left side limit` & `right side limit` are the SAME.

![image](https://user-images.githubusercontent.com/14041622/40050774-0466bc94-586b-11e8-981c-7427d765f794.png)


## `Infinite Discontinuities`
> An `Infinite Discontinuity` occurs  at some point, both `left side` & `right side` are approaching to INFINITY, which means both sides DO NOT have limits.

![image](https://user-images.githubusercontent.com/14041622/40050881-5c76418e-586b-11e8-9f03-eb66464a8730.png)


## `Endpoint Discontinuities`
> An `Endpoint Discontinuity` occurs at some point, it DOESN'T HAVE **both** sides, it only has ONE SIDE.

![image](https://user-images.githubusercontent.com/14041622/40051007-d0196e0e-586b-11e8-930a-c2f1c392a019.png)


## `Mixed Discontinuities`
![image](https://user-images.githubusercontent.com/14041622/40051076-06f92d38-586c-11e8-9d2e-415a2c6e95ad.png)



# `Analyzing functions for discontinuities: algebraic`
> If the limits of both side of some point, are EQUAL, then it's continuous at this point.

At a point `a`, for `f(x)` to be continuous at `x=a`, we need `lim(x→a)f(x) = f(a)`.

Example:
![image](https://user-images.githubusercontent.com/14041622/40051602-eb4faf88-586d-11e8-91d8-504937405601.png)
Solve:
- Got the limit of left side is `-1/2`
- Got the limit of right side is `-1/2`
- They're equal, so it's continuous at this point.


# Application of Removable Discontinuities

Example:
![image](https://user-images.githubusercontent.com/14041622/40052537-b4a9ec66-5870-11e8-8451-89d2e640f220.png)
Solve:
It's just the same with calculating the limits of both sides.


# `Derivative Basics`
> Simply saying, it's just the SLOPE of ONE POINT of a graph (line or curves or anything).

[Refer to Mathsisfun: Introduction to Derivatives](https://www.mathsisfun.com/calculus/derivatives-introduction.html)

![image](https://user-images.githubusercontent.com/14041622/40104999-4f4ccb18-5924-11e8-9baf-d9e43e3e1cd8.png)


A Derivative, is the `Instantaneous Rate of Change`, which's related to the `tangent line` of a point, instead of a secant line to calculate the Average rate of change.

“Derivatives are the result of performing a differentiation process upon a function or an expression. ”

## `Derivative notations`

[Refer to Khan academy article: Derivative notation review.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/a/derivative-notation-review)

![image](https://user-images.githubusercontent.com/14041622/40266166-d90e5e1a-5b78-11e8-9fdf-20e72b432012.png)

### `Lagrange's notation`
In Lagrange's notation, the derivative of `f(x)` expressed as `f'(x)`, reads as `f prime of x`.

### `Leibniz's notation`
In this form, we write `dx` instead of `Δx heads towards 0`.
And `the derivative of` is commonly written as: 
![image](https://user-images.githubusercontent.com/14041622/40105095-9470659c-5924-11e8-8e8d-8916bef4c995.png)

> For memorizing, just see `d` as `Δ`, reads `Delta`, means change. So `dy/dx` means `Δy/Δx`. Or it can be represent as `df / dx` or `d/dx · f(x)`, whatever.

![image](https://user-images.githubusercontent.com/14041622/40105113-9d98cdd0-5924-11e8-86a2-e918c0109b23.png)

![image](https://user-images.githubusercontent.com/14041622/40102277-a5ba5b26-591c-11e8-9d8f-ecdb59db5b69.png)

### `How to understand dy/dx`

This is a review from "the future", which means while studying Calculus, you have to come back constantly to review what the `dy/dx` means.  ---- It's just so confusing.
Without fully understanding the `dy/dx`, you will be lost at topics like `Differentiate Implicit functions`, `Related Rates` and such.

![image](https://user-images.githubusercontent.com/14041622/40266233-1868f164-5b7a-11e8-9516-712cd539fd91.png)


## `Tangent line & Secant line`

- The `secant line` is drawn to connect TWO POINTS, and gets us the `Average Rate of Change` between two points.
- The `Tangent line` is drawn through ONE POINT, and gets us the `Rage of change at the exact moment`.

As for the `secant line`, its interval gets smaller and smaller and APPROACHING to `0` distance, it actually is a process of calculating `limits` approaching `0`, which will get us the `tangent line`, that been said, is the whole business we're talking about: the `Derivative`, the `Instantaneous Rate of Change`.

![image](https://user-images.githubusercontent.com/14041622/40102814-125b24e4-591e-11e8-9d6d-f51e0fc85ee6.png)

![image](https://user-images.githubusercontent.com/14041622/40102982-8c9e92c2-591e-11e8-9893-6f4d4c7fc876.png)

![secant to tangent animation](https://user-images.githubusercontent.com/14041622/40102854-2ef65b6e-591e-11e8-8041-a9e7a4b58b40.gif)




# `Differentiability`
> "If the point of a function IS differentiable, then it MUST BE continuous at the point."

Example of NOT `differentiable` points:
![image](https://user-images.githubusercontent.com/14041622/40107341-8e16a390-592a-11e8-9d9a-82a01c2c64e1.png)

You can see, if the point DOES NOT have `limit`, it's NOT DIFFERENTIABLE. 
In another word, the point is not CONTINUOUS, it's `Jump Discontinuity`, or `Removable Discontinuity`, or any type of discontinuities.

## Not differentiable situations
- Vertical Tangent (∞)
- Not Continuous
- Two sides' limits are different

![image](https://user-images.githubusercontent.com/14041622/40108012-64c1e426-592c-11e8-99c9-357d59ee9a87.png)



# `Derivative equation`
The idea of derivative equation is quite simple: **The LIMIT of the SLOPE.**

> The slope is equal to `change in Y / change in X`. 
So for a point `a`, we IMAGINE we have another near point which lies on the SAME LINE with `a`, 
and since we have TWO POINTS now, 
we can then let their `Y-value Change` divided by their `X-value Change` to get the slope.

There're two equations for calculating derivative at a point, and the only different thing is how to express the IMAGINARY POINT with respect to the point `a`, it could either be `x` or `a+h` :

![image](https://user-images.githubusercontent.com/14041622/40187586-70e7343c-5a2a-11e8-83ab-e36804921b73.png)
or:
![image](https://user-images.githubusercontent.com/14041622/40187604-78b086b4-5a2a-11e8-8539-76872a76996e.png)


## `How to calculate derivative`
Strategy:
- Determine if it's **CONTINUOUS** at this point, by:
    - See if the point is defined in the interval
    - Calculate **LIMITS** of both RIGHT SIDE and LEFT SIDE of the point.
    - If two sides' limits are the same, then it's continuous. Otherwise it's discontinuous.
- Determine if it's **DIFFERENTIABLE** (Actually is the process of getting its **derivative**):
    - Apply Derivative equation to get both RIGHT SIDE LIMIT and LEFT SIDE LIMIT.
    - If two sides' limits are the same, then that value is the **Derivative** at the point. If not, then it's NOT DIFFERENTIABLE.

Example:
![image](https://user-images.githubusercontent.com/14041622/40156524-990fb1fe-59cc-11e8-939c-104e910309ab.png)
Solve:
- See that the point `3` is defined in the interval.
- Left side limit of the point, is using the first equation, and gets the `lim g(x) = -7`
- Right side limit of the point, is using the second equation, and gets the `lim g(x) = -7`
- Limits of both sides are the SAME, so it's continuous, and let's see if it's differentiable.
- Apply the derivative equation for both Left side  & Right side:
![image](https://user-images.githubusercontent.com/14041622/40156768-197072c4-59ce-11e8-9a2f-d9e09cd354c7.png)
- Both sides' limits exists but not that same, so it's not differentiable.

Example2:
![image](https://user-images.githubusercontent.com/14041622/40156269-fa328364-59ca-11e8-97fa-af21bfa10de9.png)
Solve:
- See that the point `-1` is defined in the interval.
- Left side limit of the point, is using the first equation, and gets the `lim g(x) = 1`
- Right side limit of the point, is using the second equation, and gets the `lim g(x) = 4`
- Limits of both sides are NOT SAME, so it's not continuous, then of course not differentiable.


# `Local linearity & Linear approximation`
> `Local linearity` is for approximating of a point's value by its near known point.

Just think of a curve, a good way to approximate its Y-value, is to find another known point near it, and make a line connecting two points, then gets the value by linear equation.

[Refer to Khan academy lecture.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/v/local-linearization-intro)

![image](https://user-images.githubusercontent.com/14041622/40158438-1ff4586e-59d7-11e8-901f-b76764884a83.png)

![image](https://user-images.githubusercontent.com/14041622/40158363-b07acc02-59d6-11e8-8d62-76ab8643c7c9.png)


Example: 
![image](https://user-images.githubusercontent.com/14041622/40158643-2fb7a9da-59d8-11e8-9ca0-956bf405ff79.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/40158702-81d93242-59d8-11e8-87ad-9622f18ddbc7.png)




# Basic Differentiation Rules

![image](https://user-images.githubusercontent.com/14041622/40227636-a305cc52-5ac1-11e8-9fbe-ac7e11dd4a6f.png)

[Refer to Math is fun: Derivative Rules](https://www.mathsisfun.com/calculus/derivatives-rules.html)

## Derivative of Single Common Functions
Functions | Function | Derivative
-- | -- | --
Constant | c | 0
Line | x | 1
        | ax | a
Square | x² | 2x
Square Root | √x | ![image](https://user-images.githubusercontent.com/14041622/40228460-eca5310c-5ac3-11e8-91c1-1ef393f60202.png)
Exponential | eˣ | eˣ
                     | aˣ | aˣ · ln(a)
Logarithms | ln(x) | 1/x
                    | loga(x) | 1 / (x·ln(a))
Trigonometry (x is in radians) | sin(x) | cos(x)
                                                   | cos(x) | −sin(x)
                                                   | tan(x) | sec²(x)
Inverse Trigonometry | sin⁻¹(x) | 1/√(1−x²)
                                     | cos⁻¹(x) | −1/√(1−x²)
                                     | tan⁻¹(x) | 1/(1+x²)



## Common Rules for multiple functions
Rules | Function | Derivative
-- | -- | --
With constant | c·f | c·f’
Power Rule | xⁿ | n·xⁿ⁻¹
Sum Rule | f + g | f’ + g’
Difference Rule | f - g | f’ − g’
Product Rule | f · g | fg’ + f’ g
Quotient Rule | f / g | (f’g − g’f ) / g²
Reciprocal Rule | 1 / f | −f’ / f²
Chain Rule | f(g(x)) | f’(g(x)) · g’(x)



# `Chain Rule`
> One of the **core principles** in Calculus is the Chain Rule.

![image](https://user-images.githubusercontent.com/14041622/40289431-ce3b8652-5cea-11e8-9aba-c40a24f19bdd.png)

[Refer to Khan academy article: Chain rule](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/a/chain-rule-review)

It tells us how to differentiate `Composite functions`.

![image](https://user-images.githubusercontent.com/14041622/40225236-178dc84c-5abb-11e8-8bbf-098d8df7d3b9.png)

**It must be composite functions, and it has to have `inner & outer` functions, which you could write in form of `f(g(x))`.**
![image](https://user-images.githubusercontent.com/14041622/40225120-c6ddf174-5aba-11e8-8b1b-2859c7eeb749.png)

### Common mistakes
- Not recognizing whether a function is composite or not
- Wrong identification of the inner and outer function
- **Forgetting to multiply by the derivative of the inner function**
- Computing `f(g(x))` wrongly:
![image](https://user-images.githubusercontent.com/14041622/40225381-7744459a-5abb-11e8-848d-9a28c39db99c.png)

### How to identify Composite functions
> Seems a basic algebra101, but actually a quite tricky one to identify.

[Refer to Khan lecture: Identifying composite functions](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/v/recognizing-compositions-of-functions)

The core principle to identify it, is trying to re-write the function into a nested one: `f(g(x))`. If you could do this, it's composite, if not, then it's not one.

Examples:
![image](https://user-images.githubusercontent.com/14041622/40226233-add7f910-5abd-11e8-8522-853ca335a2a1.png)
It's a composite function, which the inner is `cos(x)` and outer is `x²`.

![image](https://user-images.githubusercontent.com/14041622/40226318-f2bbe668-5abd-11e8-9f47-405b4476c054.png)
It's a composite function, which the inner is `2x³-4x` and outer is `sin(x)`.

![image](https://user-images.githubusercontent.com/14041622/40226383-24b4fe48-5abe-11e8-9cb0-9c0bda203c89.png)
It's a composite function, which the inner is `cos(x)` and outer is `√(x)`.

## `Two forms of Chain Rule`

The general form of Chain Rule is like this:
![image](https://user-images.githubusercontent.com/14041622/40289487-313c6d84-5ceb-11e8-85a9-2aee2108aa60.png)

But the Chain Rule has another **more commonly used** form:
![image](https://user-images.githubusercontent.com/14041622/40289493-3ddcdfa6-5ceb-11e8-9771-2d93d210a85b.png)

Their results are exactly the same.
It's just some people find the first form makes sense, some more people find the second one does.



Example:
![image](https://user-images.githubusercontent.com/14041622/40268880-38210900-5ba8-11e8-8e45-3691ad3b5163.png)
Solve:
[Refer to Symbolab worked example.](https://www.symbolab.com/solver/step-by-step/%5Cfrac%7Bd%7D%7Bdx%7D%5Cleft(sqrt%5Cleft(3cos%5E%7B3%7D%5Cleft(x%5Cright)%5Cright)%5Cright))


# `Derivatives of Trig functions`

![image](https://user-images.githubusercontent.com/14041622/40227555-69eb9e74-5ac1-11e8-98cf-75d6088b5b4f.png)

## Reminder of Trig identities & Unit circle values
```py
# Reciprocal and quotient identities
tan(θ) = sin(θ) / cos(θ)
csc(θ) = 1/sin(θ)
sec(θ) = 1/cos(θ)
cot(θ) = 1/tan(θ)
```

[Refer to previous note of all trig identities.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-377684464)

![unit circle](https://user-images.githubusercontent.com/14041622/38487029-724164d8-3c11-11e8-9913-17a6da068090.png)




# `Implicit differentiation`
> Bit hard to understand it in the first place.

![image](https://user-images.githubusercontent.com/14041622/40266041-b0ae9720-5b76-11e8-823f-33d3935a9124.png)


## `What is Implicit & Explicit Function`
[Refer to video by Krista King: What is implicit differentiation?](https://www.youtube.com/watch?v=GpWCFoCznGI)

- `Explicit function`: it's the normal function we've seen a lot before, which's in the form of `y = x....`
- `Implicit function`: it't NOT YET in the general form of a function and not easily separated, like `x² + y² = 1`

So knowing how to differentiate an `implicit function` is quite helpful when we're dealing with those NOT EASILY SEPARATED functions.

## `How to Differentiate Implicit function`

[Refer to video: Use implicit differentiation to find the second derivative of y (y'') (KristaKingMath)](https://www.youtube.com/watch?v=MzwcOw27ZRE)
[Refer to video by The Organic Chemistry Tutor: Implicit Differentiation Explained - Product Rule, Quotient & Chain Rule - Calculus](https://www.youtube.com/watch?v=LGY-DjFsALc)

[Refer to Symbolab: Implicit Derivative Calculator](https://www.symbolab.com/solver/implicit-derivative-calculator/implicit%20derivative%20%5Cfrac%7Bdy%7D%7Bdx%7D%2C%20x%5E%7B2%7D%2Bxy%2By%5E%7B3%7D%3D0)

Assume you are to differentiate `Y` **WITH RESPECT** to `X`, written as `dy/dx`:
- Differentiate terms with `X` as normal
- Differentiate terms with `Y` as the same to `X`, BUT multiply by `(dy/dx)`
- Differentiate terms **MIXED** with `X & Y` by using `Product Rule`, then differentiate each term.

### `How to differentiate Y with respect to X`
![image](https://user-images.githubusercontent.com/14041622/40266769-864f311c-5b83-11e8-9f35-f6087c87e85d.png)

### `How to differentiate term MIXED with both X & Y`
![image](https://user-images.githubusercontent.com/14041622/40266809-34b13dfe-5b84-11e8-8981-cd6b0349fb80.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/40271196-87e4a61c-5bcc-11e8-9b9a-bfe940549680.png)
Solve:
[Refer to Symbolab: Implicit Derivative Calculator](https://www.symbolab.com/solver/implicit-derivative-calculator/implicit%20derivative%20%5Cfrac%7Bdy%7D%7Bdx%7D%2C%20x%5E%7B2%7D%2Bxy%2By%5E%7B3%7D%3D0)

- Treat `y` as `y(x)`
- Apply the Sum Rule:
![image](https://user-images.githubusercontent.com/14041622/40271287-c61ce952-5bcd-11e8-92d4-3ed3c706cd2f.png)
- Apply the normal rules to `X term`, and
- Apply the Product Rule to the `Mixed term`, and
- Apply the Chain Rule to the `Y term`:
![image](https://user-images.githubusercontent.com/14041622/40271324-5448fa9a-5bce-11e8-9d89-f30ad9a81658.png)
- Operate the equation and **solve for `dy/dx`**, and get:
![image](https://user-images.githubusercontent.com/14041622/40271337-94837f9a-5bce-11e8-8861-3b894ff5f0b9.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/40301867-f537cfd8-5d1f-11e8-87d7-308a2ebb320b.png)
Solve:
- First thing we need to find the **RIGHT** equation of Chain rule. Since it's asking us to find `dy/dt`, so we will re-write it to this one to form an equation:
![image](https://user-images.githubusercontent.com/14041622/40303119-18105648-5d24-11e8-9825-91f14654faa6.png)
- Then since we've given the `dx/dt = -3`, we only need to find out the `dy/dx` to get the result.
- We've got an equation of `x & y`, regardless whom it's respecting to. So we can do either `Implicit or Explicit differentiation` to the equation `y²=7x+1`, with respect to `y`:
![image](https://user-images.githubusercontent.com/14041622/40303322-e0535cc2-5d24-11e8-9176-d082e0c68a70.png)
- Use the implicit differentiation method, we got the `dy/dx = 7/2y`
- And since `y=6`, so `7/2y = 7/12`
- Back to the Chain Rule equation, we get `dy/dt = 7/12 · (-3) = -7/4 = -1.75`



### Example
![image](https://user-images.githubusercontent.com/14041622/40303447-5c3a1196-5d25-11e8-9239-b95c743b8be0.png)
Solve:
- Remind you that, in this problem, it's **NOT** respecting to `x` anymore, so you need to change mind before getting confused.
- First thing we need to find the **RIGHT** equation of Chain rule. Since it's asking us to find `dx/dt`, so we will re-write it to this one to form an equation:
![image](https://user-images.githubusercontent.com/14041622/40303475-78622dd6-5d25-11e8-9912-bd3744e514e9.png)
- Then since we've given the `dy/dt = -0.5`, we only need to find out the `dx/dy` to get the result.
- We've got an equation of `x & y`, regardless whom it's respecting to. It seems easier to **differentiate** explicitly:
![image](https://user-images.githubusercontent.com/14041622/40303547-c07bde32-5d25-11e8-8e6c-2c2d532a45b8.png)
- Then we use `d/dx` to differentiate the equation to get: `dx/dy = y⁻² = (0.2)⁻² = 25`
- Back to the Chain Rule equation, we get `dx/dt = dx/dy · dy/dt = 25 * (-0.5) = -12.5`.

### Example
![image](https://user-images.githubusercontent.com/14041622/40303696-6b528324-5d26-11e8-879e-e923697a8eaa.png)
Solve (Same with above examples):
- Form an equation: 
![image](https://user-images.githubusercontent.com/14041622/40303793-e113564c-5d26-11e8-94b8-fce0631e50b6.png)
- `dx/dt` has been given equals to `5`, so just to find out `dy/dx`:
![image](https://user-images.githubusercontent.com/14041622/40303865-20a8bfd6-5d27-11e8-9a70-e1d51f5451cf.png)
- And get:
![image](https://user-images.githubusercontent.com/14041622/40303898-3e7eac96-5d27-11e8-908d-e492d292c78b.png)
![image](https://user-images.githubusercontent.com/14041622/40304158-238d9892-5d28-11e8-8588-c1923d4c33b4.png)
- Now let's see what is `sin(x)` equal to:
![image](https://user-images.githubusercontent.com/14041622/40304151-1b93eee8-5d28-11e8-970b-04df4099abcb.png)
- All done.


# `Related Rates`

Just so you know, `related rates` is actually the **Application** of `Implicit Differentiation` by using Chain Rule in the form of `dy/dx = dy/du * du/dx`.

![image](https://user-images.githubusercontent.com/14041622/40288873-ff4bacf2-5ce7-11e8-9729-fb9d1bd1d9f2.png)

Btw, at Khan academy it's called the `Differentiate related functions`.

[Refer to Khan lecture.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/v/differentiating-related-functions-intro)
[Refer to video by KristaKingMath: Related rates](https://www.youtube.com/watch?v=Vi5KBiXg0Co)
[Refer to video by The Organic Chemistry Tutor: Introduction to Related Rates](https://www.youtube.com/watch?v=I9mVUo-bhM8&t=0s&index=78&list=PL0o_zxa4K1BWYThyV4T2Allw6zY0jEumv)

Strategy:
- Abstract every given condition algebraically, e.g. `s(t), s'(t), V(t), V'(t)...`
- Find a proper equation to **CONNECT** all these given conditions
- Differentiate both sides of equation, with using the Chain rule.
- Take back the given values to the Differentiated equation to get the result.

## `Example: Change of volumes`
[Refer to previous note of Implicit Differentiation.](https://github.com/solomonxie/solomonxie.github.io/issues/49#issuecomment-390174936)
![image](https://user-images.githubusercontent.com/14041622/40703294-441a0802-6417-11e8-9486-7eacddd51c9f.png)

Solve:
- Write out all conditions algebraically:
    - `r'(t)=1`
    - `r(t)=5`
    - `h'(t)=-4`
    - `h(t)=8`
    - `V(t) = π·r²·h`
- So they're asking for `V'(t)`, it then becomes `V'(t) = π·d/dt (r²·h)`
- Apply `Product rule` & `Chain rule` then substitute: `V'(t) = π((r²)'·h + r²h') = π(2r'·r + r²·h') = -20π`
Notice that: `(r²)'` is a composite function, so you want to apply the Chain rule, `=2r·r'`

## `Example: Change of volumes`
![image](https://user-images.githubusercontent.com/14041622/40665369-a652e8b4-638f-11e8-915f-976d5a502d45.png)
Solve:
- From the given conditions, we got that `r'(t)=-12`, `r(t)=40` and `h=2.5`.
- We know the equation of cylinder's volume is: `V= π·[r(t)]²·h`
- Differentiate both side of the equation to get:
![image](https://user-images.githubusercontent.com/14041622/40665972-3bbf6e12-6391-11e8-96cd-487f1b108583.png)
- Take back all the known values into the equation get `V'(t)=-2400π`

## `Example: Change of area`
![image](https://user-images.githubusercontent.com/14041622/40703993-8cdf0e3c-6419-11e8-8f8d-25d67ef5d7f6.png)
Solve:
- Write out all conditions algebraically:
    - `d₁'(t) = -7`
    - `d₁(t) = 4`
    - `d₂'(t) = 10`
    - `d₂(t) = 6`
    - `A(t) = (d₁·d₂)/2`
- So it's asking for instantaneous rate of change, then it is `A'(t) = (d₁'·d₂ + d₁·d₂')/2`
- Apply the Product rule only, to get `A'(t) = -1`.

## `Example: Pythagorean Theorem`
![image](https://user-images.githubusercontent.com/14041622/40705392-5be7534e-641d-11e8-9345-72a75f6f0715.png)
![image](https://user-images.githubusercontent.com/14041622/40707585-abdd4fce-6423-11e8-9343-1fac520bb809.png)
[Refer to Khan academy lecture: Related rates: Approaching cars](https://www.khanacademy.org/math/ap-calculus-ab/ab-applications-derivatives/ab-related-rates/v/rate-of-change-of-distance-between-approaching-cars)

Solve:
- It's a problem to calculate two objects' dynamic absolute distance: it's getting closer and closer until distance become `0`, which means they crashes at `0`.
- Write down all the conditions algebraically:
    - `c₁'(t) = -10`
    - `c₁(t) = 4`
    - `c₂'(t) = -6`
    - `c₂(t) = 3`
    - `D(t) = √(c₁²+c₂²)`
- So `D'(t) = d/dt · (√(c₁²+c₂²)) = (2c₁'c₁+2c₂'c₂)/(2√(c₁²+c₂²))`

## `Example: Sliding ladder`
![image](https://user-images.githubusercontent.com/14041622/40710951-8ac86086-642c-11e8-88ff-3e82a4425acc.png)

## `Example: multiple composite`
![image](https://user-images.githubusercontent.com/14041622/40711519-f2d9e6c6-642d-11e8-9cc7-b5c0812fd899.png)
Solve:
- Write down all the conditions algebraically:
    - `S'(t) = π/2`
    - `S(t) = 12π`
    - `S = 2π·r`, which means `r = S/2π`
    - `A(t) = π·r²`
- So `A'(t) = d/dt · (π·r²) = 2π·r·r' = 2π·6·(S/2π)' = 6S' = 3π`


# `Second derivatives`
The second derivative of a function is simply the derivative of the function's derivative.

Notation:
Leibniz's notation for second derivative is:
![image](https://user-images.githubusercontent.com/14041622/40231289-2c34f3da-5acd-11e8-9348-2ba4fb04a2aa.png)
![image](https://user-images.githubusercontent.com/14041622/40231293-344c4e10-5acd-11e8-886d-39457c2efb2d.png)



# `Derivative of Inverse functions`

![image](https://user-images.githubusercontent.com/14041622/40294394-f6786cb2-5d07-11e8-8d47-1d71456b4d2f.png)

It's developed by the Chain rule:
![image](https://user-images.githubusercontent.com/14041622/40294502-6f80d4c8-5d08-11e8-82a5-5b91e20a2e7f.png)

## `Derivative of Inverse Trig functions`
![image](https://user-images.githubusercontent.com/14041622/40313487-801adde8-5d48-11e8-8260-a631d6be6c6a.png)



## `Derivative of exponential functions`
> It's save a lot of time of life not to dig in how mathematicians developed these formulas.
If you do want to, [refer to Khan's lecture: Exponential functions differentiation intro](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/v/exponential-functions-differentiation-intro)

Reminder: **Don't forget it's a `composite function` and you need to apply the chain rule.**

![image](https://user-images.githubusercontent.com/14041622/40298682-8ae4c95a-5d16-11e8-8115-1363d8ae637c.png)

## `Derivative of logarithm functions`
![image](https://user-images.githubusercontent.com/14041622/40300440-d3893a06-5d1b-11e8-9103-4461535d8023.png)

## Examples
Find the derivative of:
![image](https://user-images.githubusercontent.com/14041622/40298914-3a2b92f4-5d17-11e8-884e-be6cf50eb431.png)
Solve:

![image](https://user-images.githubusercontent.com/14041622/40298961-6157e9e0-5d17-11e8-8f73-56ca14655ccf.png)



# `Existence Theorems`
> Existence theorems includes 3 theorems: `Intermediate Value Theorem`, `Extreme Value Theorem`, `Mean Value Theorem`.

[Refer to Khan academy: Existence theorems intro](https://www.khanacademy.org/math/ap-calculus-ab/ab-existence-theorems/modal/v/existence-theorems)

![image](https://user-images.githubusercontent.com/14041622/40358703-b872e8f2-5df2-11e8-9230-88d5a5bb8059.png)

## `Intermediate Value Theorem (IVT)`

The definition is quite simple:
When we have 2 points **connected** by a **continuous** curve:
one point **below** the line, the other point **above** the line,
then there will be at least one place where the curve crosses the line!

![image](https://user-images.githubusercontent.com/14041622/40359266-b30d756a-5df4-11e8-92be-474ac99a08d4.png)

[Refer to Maths if fun: Intermediate Value Theorem](https://www.mathsisfun.com/algebra/intermediate-value-theorem.html)
[Refer to video: Intermediate Value Theorem Explained](https://www.youtube.com/watch?v=9wEHwFrUyOU)

### Find roots by using IVT
`IVT` is often to find `roots` of a function, which means to find the `x value when f(x)=0`.
So for finding a root, the definition will be:
> If `f(x)` is continuous and has an interval `[a, b]`, which leads the function that `f(a)<0 & f(b)>0` , then it MUST has a point `f(c)=0` between interval `[a,b]`, which makes a root `c`.

Example:
Tell whether the function `f(x) = x² - x - 12` in interval `[3,5]` has a root.
Solve:
- We got that at both sides of intervals: `f(3)=-6 < 0`, and `f(5)=8 > 0`
- So according to the Intermediate Value Theorem, there IS a root between `[3,5]`.
- Calculate `f(c)=0` get the root `c=4`.

## `Extreme Value Theorem (EVT)`
![image](https://user-images.githubusercontent.com/14041622/40359648-16501adc-5df6-11e8-87df-67f066ec8235.png)

[Refer to Khan lecture: Extreme value theorem](https://www.khanacademy.org/math/ap-calculus-ab/ab-existence-theorems/modal/v/extreme-value-theorem)
[Refer to video: Extreme Value Theorem](https://www.youtube.com/watch?v=Sx2lPZlnWfs)

## `Mean Value Theorem (MVT)`

[Refer to Khan academy article: Establishing differentiability for MVT](https://www.khanacademy.org/math/ap-calculus-ab/ab-existence-theorems/modal/a/review-establishing-differentiability-for-mvt)

> The `MVT` is saying: 
If your function is **CONTINUOUS** over `[a,b]` and **DIFFERENTIABLE** over `(a,b)`, 
then there **MUST BE** a **tangent line** has the same slope with the **Secant line**.

Which also means that, if the conditions are satisfied, then there **MUST BE** a number `c` makes the **derivative** is equal to the **`Average Rate of Change`** between the two end points.
![image](https://user-images.githubusercontent.com/14041622/40409998-308d166c-5e9f-11e8-9871-829dc7f66658.png)


![image](https://user-images.githubusercontent.com/14041622/40409764-6e6c566a-5e9e-11e8-8d5a-42441f4bb351.png)


![image](https://user-images.githubusercontent.com/14041622/40409012-13197ff6-5e9c-11e8-8d3b-b0933d62d2bb.png)


# `L'Hopital's Rule`
`L`Hopital's Rule helps us to find the limit of an `Undefined` limits, like `0/0`, `∞/∞` and such.
It's quite simple to apply and very convenient to solve some problems.

[Refer to `L'Hôpital's rule`](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule)

![image](https://user-images.githubusercontent.com/14041622/40418356-bb326906-5eb4-11e8-9255-c5987bc96b5e.png)

### Example of `0/0`

### Example of `∞/∞`
1. Find the limit:
![image](https://user-images.githubusercontent.com/14041622/40541839-161e29bc-6050-11e8-8847-f627079e4f7e.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/40541894-46865052-6050-11e8-8124-5bfac0cf2141.png)

2. Find the limit:
![image](https://user-images.githubusercontent.com/14041622/40541969-9f1617f2-6050-11e8-9a73-8fa268b14f35.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/40541992-b64715b6-6050-11e8-9627-bb49ea149954.png)



# `Critical points`

[Refer to PennCalc Main/Optimization](http://calculus.seas.upenn.edu/?n=Main.Optimization)

For analyzing a function, it's very efficient to have a look at its `Critical points`, which could be classified as `Extrema`, `Inflection`, `Corner`, and `Discontinuity`.

![image](https://user-images.githubusercontent.com/14041622/40529990-a0dc454c-6029-11e8-9ea0-d1c77536f227.png)

## `How to find critical points`
Strategy:
- Knowing that `f(x)` has critical point `c` when `f'(c) = 0` or `f'(c) is undefined`
- Differentiate `f(x)` to get `f'(x)`
- Solve `c` for `f'(c)=0 & f'(c) undefined`

[Refer to Symbolab's step-by-step solution.](https://www.symbolab.com/solver/step-by-step/critical%20points%2C%20f%5Cleft(x%5Cright)%3Dx%5Ccdot%20sqrt%5Cleft(4-x%5Cright))

### Example
![image](https://user-images.githubusercontent.com/14041622/40605709-d4ec9d1e-6295-11e8-9706-4348337b8bb6.png)
Solve:
- See that original function `f(x)` is undefined at `x = 2 or -2`
- Differentiate `f(x)` to get `f'(x)`:
![image](https://user-images.githubusercontent.com/14041622/40605772-02625298-6296-11e8-8626-02696b7ddbcb.png)
- Solve `f'(x)=0` only when `x=0`.
- `f'(x)` is undefined when `x=2 or -2`, as the same with `f(x)` so it's not a solution.


### Example
![image](https://user-images.githubusercontent.com/14041622/40605182-10435260-6294-11e8-8dbf-96b12ef0be19.png)
Solve: [Refer to Symbolab step-by-step solution.](https://www.symbolab.com/solver/step-by-step/critical%20points%2C%20f%5Cleft(x%5Cright)%3Dx%5Ccdot%20sqrt%5Cleft(4-x%5Cright))
- Differentiate `f(x)` to get `f'(x)`:
![image](https://user-images.githubusercontent.com/14041622/40605364-c42d5c30-6294-11e8-84e8-c4026d2550f2.png)
- `f'(x)` is **undefined** when `x > 4`
- Solve `f'(x)=0` get `x = 8/3`
- So under the given condition, only `x=8/3` is the answer.


# `Extrema: Maxima & Minima`
`Extrema` are one type of Critical points, which includes `Maxima` & `Minima`.
And there're two types of Max and Min, `Global Max & Local Max`, `Global Min & Local Min`.
We can all them `Global Extrema` or `Local Extrema`.

And actually we can call them in different ways, e.g.:
- `Global Max` & `Local Max` or in short of `glo max` & `loc max`
- `Absolute Max` & `Relative Max` or in short of`abs max` & `rel max`

![image](https://user-images.githubusercontent.com/14041622/40529128-14cde61c-6026-11e8-8ebc-3dadc933afac.png)

### How to identify Extrema

We need two kind of conditions to identify the Max or Min. 
Now If we have a Non-Endpoint Minimum or Maximum point at `a`, then it must satisfies these conditions:
- **Geometric condition:** (It should be understood in a more intuitive way)
    - in the interval `[a-h, a+h]` there's no point above or below `f(a)` or
    - `f'(a-h)` & `f'(a+h)` have different sign, one negative another positive.
- **Derivative condition:**
    - `f'(a) = 0` or 
    - `f'(a) is undefined`

### How to find Extrema
[Refer to Khan academy lecture: Finding critical points](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/finding-critical-numbers)

We just need to assume `f'(x) = 0` or `f'(x) is undefined`, and solve the equation to see what `x` value makes it then.


## `Increasing & Decreasing Intervals`
We can easily tell at a point of a function, it's at the trending of increasing or decreasing, by just looking at the `instantaneous slope` of the point, aka. the derivate. 
If the derivative, the slope is positive, then it's increasing. Otherwise it's decreasing.

### Finding the trending at a point
Just been said above, we assume at point `a`, it's value is `f(a)`. So the slope of it is `f'(a)`.
And if `f'(a) < 0`, then it's decreasing; If `f'(a) > 0`, then it's increasing.

### `Finding a decreasing or increasing interval`
[Refer to Khan lecture.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/increasing-decreasing-intervals-given-the-function)

It's just doing the same thing in the opposite way.
For find a decreasing interval, we assume `f'(x) < 0`, and by solving the inequality equation we will get the interval.

Strategy:
- Get Critical points.
- Separate intervals according to `critical points`, `undefined points` and `endpoints`.
- Try easy numbers in EACH intervals, to decide its TRENDING (going up/down):
    - If `f'(x) > 0` then the trending of this interval is **Increasing**.
    - If `f'(x) < 0` then the trending of this interval is **Decreasing**.

Example:
![image](https://user-images.githubusercontent.com/14041622/40609152-624738b8-62a0-11e8-8725-509e4e5a78a3.png)
Solve:
- Set `f'(x) = 0 or undefined`, get `x = -2 or -1/3`
- Separate intervals to `(-∞, -2, -1/3, ∞)`
![image](https://user-images.githubusercontent.com/14041622/40609259-ad80e068-62a0-11e8-81cd-f4bdb5070dbe.png)
- Try some easy numbers in each interval: `-3, -1, 0`:
![image](https://user-images.githubusercontent.com/14041622/40609319-ddc615cc-62a0-11e8-90e5-8829f92d6e04.png)

## `How to find Relative Extrema`
> Remember that an `Absolute extreme` is also a `Relative extreme`.

[Refer to khan: Worked example: finding relative extrema](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/finding-relative-maximum-example)
[Refer to Khan Academy article: Finding relative extrema](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/a/applying-the-first-derivative-test-to-find-extrema)

![image](https://user-images.githubusercontent.com/14041622/40531186-21ecfd44-602e-11e8-8018-0409609a6167.png)

Strategy:
- Get Critical points.
- Separate intervals according to `critical points`, `undefined points` and `endpoints`.
- Try easy numbers in EACH intervals, to decide its TRENDING (going up/down).
- Decide each critical point is Max, Min or Not Extreme.

Example:
![image](https://user-images.githubusercontent.com/14041622/40608781-3c071840-629f-11e8-90b1-0225538eb324.png)
Solve:
- Set `f'(x)=0 or undefined`, get `x=0 or -2 or 1`
- Separate intervals to `(-∞, -2, 0, 1, ∞)`
![image](https://user-images.githubusercontent.com/14041622/40608852-752ce6ea-629f-11e8-8b65-d15ac105fb52.png)
- Try easy number in each interval: `-3, -1, 0.5, 2` and get the trendings:
![image](https://user-images.githubusercontent.com/14041622/40608921-af3594c2-629f-11e8-9cc4-a39b476a14e4.png)
- Identify critical points' **concavity**:
![image](https://user-images.githubusercontent.com/14041622/40608947-c1bfb44c-629f-11e8-9e7b-b4e38185c1ec.png)

## `How to find Absolute Extrema`
[Refer to Khan academy article: Absolute minima & maxima review](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/a/absolute-minima-and-maxima-review)
[Refer to Khan academy lecture: Finding absolute extrema on a closed interval](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/using-extreme-value-theorem)

Strategy:
- Find all `Relative extrema`
    - Get Critical points.
    - Separate intervals according to critical points & endpoints.
    - Try easy numbers in EACH intervals, to decide its TRENDING (going up/down).
    - Decide each critical point is Max, Min or Not Extreme.
- Input all the extreme point into original function `f(x)` and get extreme value.

Example:
![image](https://user-images.githubusercontent.com/14041622/40609657-e09e250e-62a1-11e8-9e43-f1a69c217231.png)
Solve:
- Set `g'(x) = 0 or undefined` get `x=0`
- Separate intervals to `[-2, 0, 3]` according to the critical point & endpoints of the given condition.
- Try some easy numbers of each interval `-1, 2` into `g'(x)`
- Get the trending of each interval: `(+, +)`
- So the minimum must be the left endpoint of the given condition, which is `x=-2`.


Example:
![image](https://user-images.githubusercontent.com/14041622/40618317-bbc9bb7c-62c3-11e8-9723-962c727c7d4d.png)
Solve:
- Differentiate to set `f'(x)=0` and got `x=0, -1, 1`
- Separate intervals to `(-∞, -1, 0, 1, +∞)`
- Try some easy numbers in each interval for `f'(x)` and got the signs: `-, +, -, +`
- According to the signs we know that `-, +` gives us a `Relative maximum`
- But at the end it's `+` again, and the interval is going up to `+∞`, means `f(x)` will go infinitely high.
- So there's NO Absolute maximum.


# `Concavity`

[Refer to Khan academy: Concavity introduction](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/concavity-concave-upwards-and-concave-downwards-intervals)

Two types of concavity: `Concave Up` & `Concave Down`.

## `Understand function by 1st & 2nd Derivative`
![image](https://user-images.githubusercontent.com/14041622/40534451-a64de72e-6038-11e8-9a03-f665509c404e.png)


## `Identify concavity by using Second Derivative`

![image](https://user-images.githubusercontent.com/14041622/40619904-73253d6e-62c9-11e8-8e2d-96b755d9e3f5.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/40620047-ef5a6486-62c9-11e8-90cc-8ab64633f1ff.png)
Solve:
- `f'(x) > 0` means we're to find the INCREASING interval on the graph
- `f''(x) < 0` means we'll be focusing on the CONCAVE UP shape only
- So it's about the interval of`(-4, -3)` and `(3, 4)`.




# `Inflection Point`
> An inflection point is a point where the graph of the function **changes** CONCAVITY (from up to down or vice versa).

It could be seen as a `Switching point`, which means the point that the `Slope` of function switch from increasing and decreasing. 
e.g., the function might be **still going up**, but at such a point **it suddenly increases slower and slower**. And we call that point an `inflection point`.
![image](https://user-images.githubusercontent.com/14041622/40535579-13277fba-603c-11e8-93e5-c09a446700e7.png)

[Refer to Khan academy video for more intuition rapidly: Inflection points from graphs of function & derivatives](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/identifying-inflection-points-from-graphs-of-function-and-derivatives)


Algebraically, we identify and express this point by the function's `First Derivative` OR `Second Derivative`.
![image](https://user-images.githubusercontent.com/14041622/40535447-b9081cec-603b-11e8-812c-89d7c77ab6c3.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/40620823-de14fa26-62cc-11e8-9584-b4d2adf1b774.png)
Intuitive way to solve:
- Draw a **tangent line** in imagination and move it on the function from left to right
- Notice the tangent line's slope, does it go faster or slower or suddenly change its pace at a point?
- We found it suddenly changed at point `c`.

More definitional way to solve:
- Looking for the `parts of concavity shapes`
- Seems that `B-C` is a part of `Concave Down`, and `C-D` is a part of `Concave Up`
- So `C` is a SWITCHING POINT, it's a `inflection point`.

### Example
![image](https://user-images.githubusercontent.com/14041622/40620305-e8f336b2-62ca-11e8-94b1-1d03ac18651a.png)
Solve:
- Looking for the `parts of concavity shapes`
- There's no changing of concavity shapes, there's only one shape: Concave down.

### Example
![image](https://user-images.githubusercontent.com/14041622/40632882-29c5d444-631e-11e8-9bd6-986593b53471.png)
Solve:
- Notice that's the graph of **`f'(x)`**, which is the First Derivative.
- Checking `Inflection point` from 1st Derivative is easy: just to look at the change of direction.
- Obviously there're only two points changed direction: -1 & 2

### Example
![image](https://user-images.githubusercontent.com/14041622/40632978-e07bc612-631e-11e8-96ed-7cab4ca16c84.png)
Solve:
- Mind that this is the graph of **`f''(x)`**, which is the Second derivative.
- Checking `inflection points` from 2nd derivative is even easier: just to look at when it changes its sign, or say crosses the X-axis.
- Obviously, it crosses the X-axis 5 times. So there're 5 inflection points of `f(x)`.



### Example: Finding Inflection points
![image](https://user-images.githubusercontent.com/14041622/40635878-dd2785ae-632e-11e8-914e-73cee5899f50.png)
Solve:
- Function has **POSSIBLE** inflection points when `f''(x) = 0`.
- Set `f''(x) =0 ` and solve for `x`, got `x=-3`. 
- We now know the possible point, but don't know its **CONCAVITY**. This need to try some numbers from its both sides:
![image](https://user-images.githubusercontent.com/14041622/40636008-899e2cca-632f-11e8-9d10-08f56c81631f.png)
- So it didn't change the concavity at point `-3`, means there's no inflection point for function.

### Example: Finding Inflection points
![image](https://user-images.githubusercontent.com/14041622/40636182-71f4ce5c-6330-11e8-9fc1-93e94a01c93b.png)
Solve:
- Function has **POSSIBLE** inflection points when `f''(x) = 0`.
- Set `f''(x) =0 ` and solve for `x`, got `x=0 or 6`. 
[Refer to Symbolab for `f''(x)`.](https://www.symbolab.com/solver/step-by-step/%5Cfrac%7Bd%5E%7B2%7D%7D%7Bdx%5E%7B2%7D%7D%5Cleft(3x%5E%7B5%7D-30x%5E%7B4%7D%5Cright))
[Refer to Symbolab for `f''(x)=0`.](https://www.symbolab.com/solver/step-by-step/60x%5E%7B3%7D-360x%5E%7B2%7D%3D0)
- We now know the possible point, but don't know its **CONCAVITY**. This need to try some numbers from its both sides:
![image](https://user-images.githubusercontent.com/14041622/40636258-bfbf09ae-6330-11e8-962e-3b9f5f4d6a19.png)
- So it didn't change the concavity at point `0`, means only `6` is the inflection point.


# `Second Derivative Test`
![image](https://user-images.githubusercontent.com/14041622/40632918-6eb231ba-631e-11e8-89f6-68f3c347ac24.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/40633285-589b4a8a-6321-11e8-8d8d-f0564c51e91d.png)
Solve:
- `f'(c) = 0` means `c` is a critical point, could be max, min, inflection.
- `f''(c) < 0` means around point `c` it's a Downward Concave.
- Conclusion then is that `c` is a maximum point.

### Example
![image](https://user-images.githubusercontent.com/14041622/40633351-c39c421c-6321-11e8-8e23-0137876de182.png)
Solve:
- `f'(c) = 0` means `c` is a critical point, could be max, min, inflection.
- `f''(c) = 0` means it's either a Concave up or down, we don't know yet.
- So the answer is "No enough information to tell."

### Example
![image](https://user-images.githubusercontent.com/14041622/40635208-81c09776-632b-11e8-8e16-b1ba89b6bf54.png)
Solve:
- It's Concave Down when `f''(x) < 0`
- Find formula of `f''(x)` and set inequality equation `f''(x)<0` and solve to get `x > 2`.


# `Anti-derivative`
Looks like a fancy word, but it just means: Use the **Derivative function** describe the **Original function**.

Notice that: There might be multiple possible anti-derivatives.

## The graphical relationship between a function & its derivative

[Refer to Khan academy: The graphical relationship between a function & its derivative (Part 1)](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/intuitively-drawing-the-derivative-of-a-function)

![image](https://user-images.githubusercontent.com/14041622/40538009-040c93d8-6043-11e8-9b2b-2179a6bda6df.png)


## How to draw the function's Anti-derivative

[Refer to Khan academy: The graphical relationship between a function & its derivative (part 2)](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/v/intuitively-drawing-the-anitderivative-of-a-function)

![image](https://user-images.githubusercontent.com/14041622/40538272-d9650844-6043-11e8-8e53-6e60b4207b86.png)


### Example
[Refer to Khan academy.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-analyze-functions/modal/e/connecting-function-and-derivatives)
![image](https://user-images.githubusercontent.com/14041622/40636691-09851536-6333-11e8-9dd6-38292db4afdb.png)




# Analyze Function Behaviors with Derivatives
Analyzing function's behaviors is one of the Core Purposes of studying Calculus.

> **AND THE CORE PURPOSE OF ANALYZING FUNCTION, IS FOR COMPUTER TO UNDERSTAND IT `"BLINDLY"`, OR SAY "ALGEBRAICALLY"! BECAUSE IT CAN'T BE LIKE HUMAN TO "EYE BALL" IT!**

`First Derivative`
- Function has `critical points` when `f'(x) = 0`
- Function has `relative extrema` when `f'(x) crosses X-axis`:
    - It has `relative maxima` when `f'(x)` crosses **UP**.
    - It has `relative minima` when `f'(x)` crosses **DOWN**.

`Second Derivative`
- Function has `inflection points` when `f''(x)=0` and `f''(x)` **crosses** X-axis.
- It's `concave up` if `f''(x) > 0`
- It's `concave down` if `f''(x) < 0`

`1st & 2nd Derivative`
- It has a `relative maximum` when `f'(x)=0` & `f''(x) < 0`
- It has a `relative minimum` when `f'(x)=0` & `f''(x) > 0`
- It has an `inflection point` when `f'(x)` changes direction, **OR** `f''(x)` changes sign.
- It has a possible `inflection point` when `f'(x) = 0` & `f''(x) = 0`.


# `Optimization`

Once you've mastered the Derivatives, you would know the `optimization problems` are easy.
It's just a progress to get **the Maximum or Minimum points of a given function.** 

### `Example: Max product`
![image](https://user-images.githubusercontent.com/14041622/40716539-ed6c3942-643b-11e8-82e5-da4411eecf7a.png)
Solve:
- It's bit tricky to understand the question.
- Form a function: `P(x) = x(a-x) = ax - x²`
- To get a maximum, need to find the critical points first.
- Set `P'(x) = 0` then get `x = a/2`.
- To perform a 2nd Derivative Test: `P''(x) = -2`, means it's Concave Down
- So the critical point `a/2` is a maximum.

### `Example: Max Area of Trapezoid Inscribed in a Semicircle`
```
What is the area of the largest trapezoid that can be inscribed in a semicircle with radius `r = 1`?
```
[Refer to Kristaking's video: Largest area of a rectangle inscribed in a semicircle](https://www.youtube.com/watch?v=wNMK92GVTO8&t=10s)


# `Applications of Derivatives`

## Lose of bears
![image](https://user-images.githubusercontent.com/14041622/40659562-2f88308a-6381-11e8-8f0d-8c2253a56bb2.png)
Solve:
- Just take the derivative `B'(t)` and input `t=2` to get the value `B'(2) ≈ -361 bears/year`.

