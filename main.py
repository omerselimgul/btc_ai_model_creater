import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib


df = pd.read_excel("binance_new_15min.xlsx")

# X = df.drop(["close_price","high_price","low_price","volume","Unnamed: 0","short_EMA","long_EMA","CCI","slow_MA","middle_MA","long_MA"],axis=1)

X = df.drop(["Close","High","Low","Volume"],axis=1)
X = X[201:]
y = df["High"]
y = y[201:]
# X = X[:len(X)-1]
# y = df["High"]
# y = y[1:]
y.index = range(0,0+len(y))
X.index = range(0,0+len(X))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()


model.fit(X_train, y_train)
#
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print("Ortalama Kare Hata (MSE):", mse)
#
joblib.dump(model, 'high_price_15min.joblib')
# print("Model başarıyla kaydedildi.")


#-----------------------------------------------------------
# short_rsi	middle_rsi	long_rsi	short_EMA	long_EMA	CCI	slow_MA	middle_MA	long_MA	Open	Close	High	Low	Volume
# 45,23997653	47,19889838	49,07694125	69457,75848	69460,17178	-35,65445811	69467,5506	69712,1859	70059,61535	69444,6	69379,12	69449,4	69360,38	105,73063
# 50,88608295	48,27104734	49,55248556	69461,00948	69461,55831	-10,63228562	69451,9944	69710,975	70050,5898	69379,13	69478,89	69478,89	69348	135,63135



# veri_noktasi =[[50.88608295,48.27104734,49.55248556,69461.00948,69461.55831,-10.63228562,69451.9944,69710.975,70050.5898,69379.13]]
#
# prediction = model.predict(veri_noktasi)
#57275,80078125
# print(prediction)