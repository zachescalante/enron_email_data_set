import os
import sys
import csv
import numpy as np
import pandas as pd
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

class Enron():
    
    def __init__(self):
        self.columns = ['time', 'message_id', 'sender', 'recepient', 'topic', 'mode']
        self.df = pd.read_csv(sys.argv[1], names=self.columns)
        #self.df = pd.read_csv('enron-event-history-all.csv', names=self.columns) #pd.read_csv(sys.argv[1], names=self.columns)
        
        # There are a handful of 'nan' values for the recepient. As opposed to 
        # simply deleting them, I'll substitute the value with 'blank' so we can 
        # still use string functionality on the cells
        self.df['recepient'].fillna('blank', inplace=True)
        self.df['time'] = self.df['time'].astype(str).str[:-3].astype(np.int64)
        self.df['time'] = pd.to_datetime(self.df['time'], unit='s')
        
        # Data analysis indicates I should delete the 'notes' and 'announcements'
        # as senders, since they are two of the top 10 most prolific, but 
        # probably give us less information about the actions of specific individuals
        # than do people. 
        
        self.df = self.df[~self.df['sender'].isin(['announcements', 'notes', 'schedule'])]
        self.df.set_index('time', inplace=True)
        self.top = []
        
    def senders(self):
        count = defaultdict(int)
        for name in self.df['sender']:
            count[name] += 1
        return count
    
    def receivers(self):
        count = defaultdict(int)
        for recepient in self.df['recepient']:
            if '|' in recepient:
                for email in recepient.split('|'):
                    count[email] += 1
            else:
                count[recepient] += 1
        return count
    
    def question_one(self):
        
        _dict = {}
        
        # set the 'sender' and 'receivers' dictionary to variables so that
        # we don't call these functions for every iteration of the loop
        senders = self.senders()
        receivers = self.receivers()
        unique_names = list(set(list(self.senders()) + list(self.receivers())))
        for name in unique_names:
            _dict[name] = {'senders': senders[name], 'receivers': receivers[name]}
        df = pd.DataFrame.from_dict(_dict, orient='index').sort_values('senders', axis=0, ascending=False)
        
        # Find the top n - accounts to graph
        self.top = list(df.index[:10])

        return df
    
    def question_two(self):
        # data = self.df[self.df['sender'].isin(self.top)]

        plt.figure(figsize=(10,10))
        for person in self.top:
            plt.plot(self.df['sender'][self.df['sender'] == person].resample('M').count(), label=person)
        plt.xticks(rotation=45)
        plt.legend(loc='upper left')
        plt.title("Most Prolific Senders")
        #plt.savefig('question_2.png')

        return plt
    
    def question_three(self):
        
        plt.figure(figsize=(10,10))
        
        for person in self.top:
            plt.plot(self.df['recepient'][self.df['recepient'].str.contains(person)].resample('M').nunique(), label=person)
        plt.xticks(rotation=45)
        plt.legend(loc='upper left')
        plt.title("Relative Recepient Numbers")
        #plt.savefig('question_3.png')
        
        return plt
    
    
if __name__=='__main__':
    
    enron = Enron()
    
    # Question 1: 
    enron.question_one().to_csv('question_1.csv')
    
    # Question 2:
    enron.question_two().savefig('question_2.png')
    
    # Question 3:
    enron.question_three().savefig('question_3.png')