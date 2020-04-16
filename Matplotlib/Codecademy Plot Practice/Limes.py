from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12, 6))

# setting the basic x values for all subplots
x_values = range(len(months))

# creating and plotting the left subplot
ax1 = plt.subplot(1, 2, 1)
plt.plot(x_values, visits_per_month, marker="s")
# labeling the two axes for this subplot
plt.xlabel("Months")
plt.ylabel("Page Visits")
# using ticks on x axis
ax1.set_xticks(x_values)
# labeling x ticks
ax1.set_xticklabels(months)
# adding a title
plt.title("Page visits per month")

# creating and plotting the right subplot
ax2 = plt.subplot(1, 2, 2)
plt.plot(x_values, key_limes_per_month, color="red")
plt.plot(x_values, persian_limes_per_month, color="skyblue")
plt.plot(x_values, blood_limes_per_month, color="green")
# setting up the legend for this subplot
plt.legend(["Key Limes", "Persian Limes", "Blood Limes"])
# using ticks on x axis
ax2.set_xticks(x_values)
# labeling x ticks
ax2.set_xticklabels(months)
# labeling the two axes
plt.xlabel("Months")
plt.ylabel("Limes sold")
# adding a title
plt.title("Different limes sold per month")

plt.show()