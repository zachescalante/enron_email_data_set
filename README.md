# enron_email_data_set

Here's my analysis for the Enron email data set and the ouputs I'm asked to generate:

1. A .csv file with three columns---"person", "sent", "received"---where the final two columns contain the number of emails that person sent or received in the data set. This file should be sorted by the number of emails sent.

2. A PNG image visualizing the number of emails sent over time by some of the most prolific senders in (1). There are no specific guidelines regarding the format and specific content of the visualization---you can choose which and how many senders to include, and the type of plot---but you should strive to make it as clear and informative as possible, making sure to represent time in some meaningful way.

3. A visualization that shows, for the same people, the number of unique people/email addresses who contacted them over the same time period. The raw number of unique incoming contacts is not quite as important as the relative numbers (compared across the individuals from (2) ) and how they change over time.

__Analysis__:

__Data Preprocessing__: I do some light data preprocessing by eliminating emails originating from generic email addresses ('announcements' and 'notes). I also massaged the unix timestamps to find the actual dates (they appear to be 1998 - 2002). This was confirmed as I researched the data set and found this paper:

https://www.stat.berkeley.edu/~aldous/Research/Ugrad/HarishKumarReport.pdf 

I could have spent multiple days conducting data pre-processing, but given the specific outputs requested, I decided this was enough. Additional data pre-processing could have included: filtering emails by subject, removing email addressses that have obvious spam email sender addresses.

__Question 1__: This is straightforward - I count the number of emails for each sender and sort the data set in descending order.

__Question 2__: We're asked to visualize the number of emails sent by the most prolific senders over time. I decided to sum the number of emails sent by the 10 most frequent senders (10 is an arbitrary number, but I feel this balances the top senders with a readable number for graphing purposes). I use monthly totals, since I believe this allows for smoothing of vacation days and sick days among the senders - plus our sums will be meaningful and not frequently close to zero (vacations weeks, etc). 

__Question 3__: For this question I filter the email data set by whether one of the top 10 most prolific senders was the recepient of an email from another person. We're asked to evaluate the __relative__ number of __unique__ incoming contacts compared to the other 10 most prolific senders. We generate this graph by changing __count()__ to __nunique()__ (lines 72 and 85). 

You can run the file with the command:

***python summarize-enron.py enron-event-history-all.csv***
