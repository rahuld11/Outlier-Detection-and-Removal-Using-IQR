Lets Understand Recently i have Placement Dataset I have performed Outlier removal IQR Method on it to know the data well and get insights from the data using Python in simple way 

-  Author : Rahul11
-  importing intianl stages of python requried libraries
-  Reading the csv file using pandas


-  Whar is IQR?
- The Interquartile Range (IQR) is a measure of statistical dispersion that is particularly useful for identifying outliers in a dataset.
- The IQR is the range between the first quartile (Q1) and the third quartile (Q3) and represents the middle 50% of the data.

- Here’s how to use the IQR to identify and handle outliers:

-  Steps for Outlier Removal using
- The median of the lower half of the dataset (25th percentile or Q1).
- The median of the upper half of the dataset (75th percentile or ).
-  Compute the IQR value :IQR  = Q3-Q1

-  Calculate the lower and upper bounds for outliers.
   Upper limit : Upper Bound = Q3+1.5(IQR)
   Lower limit : Lower Bound = Q1-1.5(IQR)
