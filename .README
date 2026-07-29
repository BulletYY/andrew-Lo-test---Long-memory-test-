## Lo's Modified R/S Test

The project includes an implementation of **Lo's modified rescaled range test**, also known as the **modified R/S test**.

The test is used to investigate whether a financial time series exhibits long-range dependence after accounting for short-term autocorrelation.

The implementation is based on:

> Lo, A. W. (1991).  
> *Long-Term Memory in Stock Market Prices*.  
> Econometrica, 59(5), 1279–1313.  
> JSTOR: https://www.jstor.org/stable/2938368

### Function

```python
lo_test(log_returns, q)
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `log_returns` | array-like | A one-dimensional series of logarithmic returns or another numerical time series. |
| `q` | `int` | Maximum lag used in the long-run variance estimator. It determines how many short-term autocovariances are included in the correction. |

### Methodology

The function performs the following steps:

1. Converts the input series into a NumPy array.
2. Calculates the sample mean.
3. Centers the observations around the sample mean.
4. Computes cumulative deviations from the mean.
5. Calculates the range of cumulative deviations.
6. Estimates the variance for lag zero.
7. Calculates autocovariances for lags from `1` to `q`.
8. Applies Bartlett weights to the autocovariances.
9. Constructs the long-run variance estimator.
10. Calculates Lo's modified R/S statistic.
11. Compares the statistic with asymptotic critical values.

The long-run variance estimator is defined as:

```text
S_q² = γ₀ + 2 Σ[w_k(q) × γ_k]
```

where the Bartlett weight is:

```text
w_k(q) = 1 - k / (q + 1)
```

The modified R/S statistic is calculated as:

```text
V_T(q) = R_T / (S_q × √T)
```

where:

- `R_T` is the range of cumulative deviations,
- `S_q` is the estimated long-run standard deviation,
- `T` is the number of observations,
- `q` is the maximum included lag.

### Hypotheses

The test evaluates:

```text
H₀: The series does not exhibit long-range dependence.
H₁: The series exhibits behavior inconsistent with a short-memory process.
```

The implementation uses the following asymptotic critical values for a two-sided test at the 5% significance level:

```text
Lower critical value: 0.809
Upper critical value: 1.862
```

### Interpretation

| Statistic value | Interpretation |
|---|---|
| `V_T(q) < 0.809` | Reject `H₀` in the lower tail. |
| `0.809 ≤ V_T(q) ≤ 1.862` | Do not reject `H₀`; there is insufficient evidence of long-range dependence. |
| `V_T(q) > 1.862` | Reject `H₀` in the upper tail; the result may indicate persistent long-range dependence. |
