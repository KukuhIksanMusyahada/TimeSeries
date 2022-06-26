import os
import pandas as pd
import numpy as np
import yfinance as yf


from LSTM.Essential import path_handling as ph
from LSTM.Essential import global_params as gp


def retrieve_data(names= 'AAPL',path= ph.GetDataSource()):
    data = yf.download(names,
        start= gp.START_DATE,
        end= gp.END_DATE,
        progress= False)
    data.to_csv(os.path.join(path, names, '.csv'))
    return data

def data_process(data= retrieve_data()):
    data['Date'] =  data.index
    data = data[["Date", "Open", "High", "Low", "Close", 
             "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace= True)
    return data
    
