from andrew_lo_test import lo_test
import pandas as pd
import numpy as np



data=pd.DataFrame({'returns':np.random.normal(0,1,10000)})



value, decision =lo_test(data['returns'],q=int( 4*(data.shape[0]/100)**(2/9))  )  # barlett kernel 


print(value,decision)



