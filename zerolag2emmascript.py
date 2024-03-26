//@version=5
//Indicator created by elliot who ever makes a copy will have the curse of been liquidated 
indicator("Zero Lag EMA v2 (2 EMAs)", overlay = true)

// Parámetro de entrada 1: período de la EMA1
Period1 = input.int(title="Period 1", defval=30, minval=1)

// Parámetro de entrada 2: período de la EMA2
Period2 = input.int(title="Period 2", defval=30, minval=1)

// Calcula EMA1 y EMA2
EMA1 = ta.ema(close, Period1)
EMA2 = ta.ema(EMA1, Period2)

// Calcula la diferencia entre las EMAs
Difference = EMA1 - EMA2

// Calcula la Zero Lag EMA
ZeroLagEMA = EMA1 + Difference

// Traza la EMA1 en la gráfica
plot(EMA1, color=color.red, linewidth=2)

// Traza la EMA2 en la gráfica
plot(EMA2, color=color.green, linewidth=2)
