import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = "death_valley_2018_simple.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
		
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2], "%Y-%m-%d")	
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(current_date, "missing data")
		else:
			highs.append(high)
			lows.append(low)
			dates.append(current_date)
		

# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.plot(dates, highs, c="red", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot
plt.title("Daily high and low temps - 2018\nDeath Valley, CA", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
	
