import numpy as np

def check_over_cont_window(data, window=14, tol=2):

  size = len(data)
  if size<window+1:
    print(f"Needs atleast {window+1} days previous data")
    return False

  # Calculate mean and standard deviation
  mean_value = np.mean(data[-(window+1):-1])
  std_deviation = np.std(data[-(window+1):-1])

  # Check if the last value is 3 standard deviations away from the mean
  last_value = data[-1]
  deviation_threshold = tol * std_deviation

  if abs(last_value - mean_value) > deviation_threshold:
      return True
  else:
      return False


def check_over_same_day(data, window=15, tol=2):
  cur_data = data[-1]
  data = data[:-1]
  size = len(data)
  if size < 105:
    print("Not enough data to make a prediction. Need at least 105 days of data.")
    return False

  days = (size) - np.arange(1, 105, 7)
  days = np.sort(days)
  # Calculate mean of values from the same day of the week 7 days before
  window_mean = data[days].mean()
  window_std = data[days].std()


  # Check if the last value is greater than the mean of values from the same day of the week 7 days before
  if abs(cur_data-window_mean) > tol*window_std:
    return True
  else:
    return False