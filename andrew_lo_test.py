import numpy as np

def lo_test(log_returns, q):
    """
    q =  newey-west lags 
    
    Q : Lo statistics
   
    """
    
    r = np.asarray(log_returns)
    T = len(r)
    r_bar = np.mean(r)
    
    # cummulative sum  
    cumulative = np.cumsum(r - r_bar)
    R = np.max(cumulative) - np.min(cumulative)
    
    # variance estimator  
    gamma_0 = np.mean((r - r_bar)**2)
    
    S_q = gamma_0
    
    for k in range(1, q+1):
        gamma_k = np.sum((r[k:] - r_bar) * (r[:-k] - r_bar)) / T
        weight = 1 - k/(q+1)
        S_q += 2 * weight * gamma_k
    
    S_q = np.sqrt(S_q)
    
    # Lo statistics
    Q = R / (S_q * np.sqrt(T))
    
    # 5 % 
    lower = 0.809
    upper = 1.862
    
    if Q < lower or Q > upper:
        decision = "Reject H0 (evidence of long-range dependence)"
    else:
        decision = "Do not reject H0 (no evidence of long-range dependence)"
    
    return Q, decision