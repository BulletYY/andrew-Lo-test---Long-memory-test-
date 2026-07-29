import numpy as np

def lo_test(log_returns, q):
    """
    q = liczba opóźnień do newey-westa 
    
    Q : statystyka Lo
   
    """
    
    r = np.asarray(log_returns)
    T = len(r)
    r_bar = np.mean(r)
    
    # skumulowane sumy  
    cumulative = np.cumsum(r - r_bar)
    R = np.max(cumulative) - np.min(cumulative)
    
    # estymator wariancji  
    gamma_0 = np.mean((r - r_bar)**2)
    
    S_q = gamma_0
    
    for k in range(1, q+1):
        gamma_k = np.sum((r[k:] - r_bar) * (r[:-k] - r_bar)) / T
        weight = 1 - k/(q+1)
        S_q += 2 * weight * gamma_k
    
    S_q = np.sqrt(S_q)
    
    # statystyka Lo
    Q = R / (S_q * np.sqrt(T))
    
    # 5 % 
    lower = 0.809
    upper = 1.862
    
    if Q < lower or Q > upper:
        decision = "Odrzucamy H0 (występuje długa pamięć)"
    else:
        decision = "Nie odrzucamy H0 (brak dowodów na długą pamięć)"
    
    return Q, decision