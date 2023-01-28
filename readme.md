#### A simple script used to gather data like the number of submissions and accuracies of all problems in a codechef contest. 

# Usage

```$ python main.py ${link to a codechef contest}```

The script will run indefinitely, it will log the values in it's CSV every 300 seconds or 5 minutes (controlled by "Timeout" in main.py).

# Output
The output will be stored in a CSV file with the name of the contest (eg. START34B.csv)

# Libraries used
```
1. Selenium
2. Beautiful soup
3. Pandas 
```
# Purpose

- This script was made to log the number of submissions and accuracies, I wanted to plot them in a graph to show the spikes. 
- My theory was that the spikes would coincide with a large influx of copied submissions. 
- With some simple pattern recognition, we can identify the cheaters easily.
