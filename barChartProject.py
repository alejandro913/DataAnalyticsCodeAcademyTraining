important matplotlib
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]
yearstring = [str(i) for i in years]

# Make your chart here

plt.figure(figsize=(10,8))
plt.bar(range(len(years)), past_years_averages, yerr = error, capsize = 5, color = 'blue')


ax = plt.subplot()
ax.set_xlim([-0.5,6.5])
ax.set_ylim([70,95])
ax.set_xticks(range(len(years)))
ax.set_xticklabels(yearstring)

ax.set_title("Final Exam Averages")
ax.set_xlabel("Year")
ax.set_ylabel("Test Average")

ax.savefig("my_bar_chart.png")

plt.show()


# this is the end of the bar chart

# this is where the other bar chart project begins


from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here

plt.figure(figsize = (10,8))

plt.hist(exam_scores1, bins = 12, normed = True, histtype = 'step', linewidth = 2)
plt.hist(exam_scores2, bins = 12, normed = True, histtype = 'step', linewidth = 2)

plt.legend(["1st Yr Teaching", "2nd Yr Teaching"], loc = 1)
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.title("Final Exam Score Distribution")
plt.savefig("my_histogram.png")

plt.show()



####################################################


'''

One other useful labeling tool for pie charts is adding the percentage of the total that each slice occupies. Matplotlib can add this automatically with the keyword autopct. We pass in string formatting instructions to format the labels how we want. Some common formats are:

'%0.2f' — 2 decimal places, like 4.08
'%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
'%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.

'''

from matplotlib import pyplot as plt

hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

plt.figure(figsize=(10,8))

# Create your hours_lower_bound and hours_upper_bound lists here

# Make your graph here

#fillbetween chart

plt.plot(exam_scores, hours_reported, linewidth =2)

hours_lower_bound = [i*0.8 for i in hours_reported]
hours_upper_bound = [i*1.2 for i in hours_reported]
plt.fill_between(exam_scores, hours_reported, hours_lower_bound, hours_upper_bound, alpha = 0.2)

plt.title("Time spent studying vs final exam scores")
plt.xlabel("Score")
plt.ylabel("Hours studying (self-reported)")
plt.savefig("my_line_graph.png")

plt.show()



####################################################
