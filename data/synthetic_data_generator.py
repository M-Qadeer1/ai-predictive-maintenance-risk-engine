
import pandas as pd
import numpy as np

np.random.seed(42)
n=500
df=pd.DataFrame({
 'temperature':np.random.normal(70,10,n),
 'vibration':np.random.normal(5,1,n),
 'load':np.random.uniform(0.5,1.0,n)
})
df['failure']=((df.temperature*0.03+df.vibration*0.4+df.load)>5).astype(int)
df.to_csv('sensor_data.csv',index=False)
print('Synthetic data generated')
