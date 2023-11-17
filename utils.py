import numpy as np


def add_trend(periods=2000, trend_type=1, coeff=0.4):
  time = np.arange(periods)
  values = (time**trend_type)*coeff
  
  return values

def add_pattern(periods=2000, exp1=3, exp2=2):
  # Just a random pattern
  time = np.arange(50)
  values = np.where(time < 10, time**exp1, (time-9)**exp2)
  # Repeat the pattern 5 times
  seasonal = []
  for i in range(periods//50):
      for j in range(50):
          seasonal.append(values[j])
  
  return seasonal

def add_white_noise(periods=2000, mean=0, std=1, mul=100):
  noise = np.random.normal(mean, std, size=periods)*mul

  return noise

def event(periods=2000, cd_begin=-500, cd_end=-600, trend_type=1, coeff=-10):
  event = np.zeros(periods)
  event[min(cd_begin, cd_end):max(cd_begin, cd_end)] = add_trend(abs(cd_end-cd_begin), trend_type, coeff)

  return event