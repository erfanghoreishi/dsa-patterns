# Master Theorem

A shortcut for the Big-O of **divide-and-conquer** recurrences:

$$T(n) = a\,T\!\left(\frac{n}{b}\right) + f(n)$$

- $a$ = how many recursive calls
- $b$ = how much $n$ shrinks per call
- $f(n)$ = work done outside the recursion

**The whole idea:** compare $f(n)$ with $n^{\log_b a}$. The bigger one wins.

| If $f(n)$ is... | then $T(n) =$ |
|---|---|
| **smaller** than $n^{\log_b a}$ | $\Theta(n^{\log_b a})$ |
| **equal** to $n^{\log_b a}$ (up to a $\log^k n$ factor, $k \ge 0$) | $\Theta(n^{\log_b a} \log^{k+1} n)$ |
| **bigger** than $n^{\log_b a}$ | $\Theta(f(n))$ |

("smaller/bigger" mean by a polynomial factor $n^{\varepsilon}$.)

## Mental model (intuition)

Picture the recursion tree:

| Part | Meaning |
|---|---|
| $n^{\log_b a}$ | the size/shape of the tree (how many leaves) |
| $f(n)$ | the cost at each level |
| the comparison | tells you *where* the total cost piles up |

A simple picture:

- $f(n)$ **smaller** → the **leaves** dominate
- $f(n)$ **equal** → **every level** costs the same (so multiply by the height, $\log n$)
- $f(n)$ **bigger** → the **root** dominates

## Examples

| Recurrence | $n^{\log_b a}$ | $f(n)$ vs it | $T(n)$ |
|---|---|---|---|
| $2T(n/2)+n$ (merge sort) | $n$ | equal | $\Theta(n\log n)$ |
| $T(n/2)+1$ (binary search) | $1$ | equal | $\Theta(\log n)$ |
| $4T(n/2)+n$ | $n^2$ | smaller | $\Theta(n^2)$ |
| $T(n/2)+n$ | $1$ | bigger | $\Theta(n)$ |
