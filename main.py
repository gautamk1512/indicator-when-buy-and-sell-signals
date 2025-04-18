//@version=5
strategy("Gautam  singh moves Style Strategy V1", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// === INPUTS ===
fastMA = input.int(9, title="Fast MA", minval=1)
slowMA = input.int(21, title="Slow MA", minval=1)
trendMA = input.int(100, title="Trend MA (Long-Term)", minval=1)
rsiPeriod = input.int(14, title="RSI Period")
rsiOverbought = input.int(70, title="RSI Overbought")
rsiOversold = input.int(30, title="RSI Oversold")
volumeMultiplier = input.float(1.5, title="Volume Spike Multiplier")

// === INDICATORS ===
fast = ta.ema(close, fastMA)
slow = ta.ema(close, slowMA)
trend = ta.ema(close, trendMA)
rsi = ta.rsi(close, rsiPeriod)
avgVolume = ta.sma(volume, 20)
volSpike = volume > avgVolume * volumeMultiplier

// === CONDITIONS ===
buyCond = ta.crossover(fast, slow) and close > trend and rsi < rsiOverbought and volSpike
sellCond = ta.crossunder(fast, slow) and close < trend and rsi > rsiOversold

// === STRATEGY EXECUTION ===
if buyCond
    strategy.entry("Buy", strategy.long)

if sellCond
    strategy.close("Buy")

// === PLOTTING ===
plot(fast, color=color.green, title="Fast EMA")
plot(slow, color=color.red, title="Slow EMA")
plot(trend, color=color.orange, title="Trend EMA")

plotshape(buyCond, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.labelup, text="BUY")
plotshape(sellCond, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.labeldown, text="SELL")
