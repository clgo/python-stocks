import pandas as pd 
# to correct is_list_like method which as change from pandas.core.common to pandas.api.types
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr 
import fix_yahoo_finance as yf 
yf.pdr_override()

# download dataframe
start_date  = '2007-01-01'
end_date 	= '2018-07-26'

firstreits 	= 'AW9U.SI'
silverlake 	= '5CP.SI'
perennial  	= 'P22.SI'
oue 		= 'LJ3.SI'

mystocklist = [firstreits, silverlake, perennial, oue]



for stock in mystocklist:
	try:
		print('Reading stock code {0}'.format(stock))
		sdata = pdr.get_data_yahoo(stock, start_date, end_date)		
		sdata.to_csv(stock + '.csv')
	except Exception as e:
		sdata.to_csv(stock + '.csv')
		print("{0} encounter problem {1}".format(stock, e.args))