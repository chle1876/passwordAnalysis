
# coding: utf-8

# In[109]:


import scipy as sp
from scipy import stats
import numpy as np
import pandas as pd
import re


# In[73]:


df = pd.read_excel("passwords.xlsx", names = ["Passwords"])


# In[74]:



df.head()


# In[186]:


prepasses = np.array(df['Passwords'])
passes = []
for xx in range(0,len(prepasses)):
    if(len(str(prepasses[xx])) >= 8):
        passes.append(prepasses[xx])
passes = np.array(passes)
df = pd.DataFrame(passes)


# In[182]:


def charCount(passes):
    lengthFreqs = [0]*100
    lengths = []
    for xx in range(0,len(passes)):
        l = len(str(passes[xx]))
        lengths.append(l)
    return lengths


# In[183]:


df.head()


# In[187]:


lengths = np.array(charCount(passes))
dfwPasswords = df.assign(charCount=lengths)


# In[188]:


dfwPasswords.head()


# In[189]:


dfCharFreq = pd.DataFrame(stats.itemfreq(lengths),columns=['Length','Frequency'])


# In[200]:



percentages = []

tot = dfCharFreq['Frequency'].sum()
for item in dfCharFreq['Frequency']:
    percentages.append("{0:.4f}%".format((item/tot) * 100))

dfCharFreq = dfCharFreq.assign(percents = np.array(percentages))


# In[205]:


dfTop = dfCharFreq.sort_values(by='Frequency',ascending = False)
dfTop.head(10)


# In[192]:


def lettersymbol(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == False):
            if(bool(re.search('[a-zA-Z]', item)) == True):
                if(item.isalpha() == False):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def letternumber(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == True):
            if(bool(re.search('[a-zA-Z]', item)) == True):
                if(item.isalnum() == True):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def numbersymbol(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == True):
            if(bool(re.search('[a-zA-Z]', item)) == False):
                if(item.isdigit() == False):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def symbol(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == False):
            if(bool(re.search('[a-zA-Z]', item)) == False):
                isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def letter(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == False):
            if(bool(re.search('[a-zA-Z]', item)) == True):
                if(item.isalpha() == True):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def number(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == True):
            if(bool(re.search('[a-zA-Z]', item)) == False):
                if(item.isdigit() == True):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot

def hasall(passes):
    tot = len(passes)
    number = 0
    isValid = False
    for item in passes:
        item = str(item)
        if(bool(re.search(r'\d',item)) == True):
            if(bool(re.search('[a-zA-Z]', item)) == True):
                if(item.isalnum() == False):
                    isValid = True
        if(isValid):
            number += 1
        isValid = False
    return number,tot


# In[193]:


num, tot = lettersymbol(passes)
print("{0:.2f}% of Passwords contain a letter and a symbol, but no number".format(num/tot * 100))
num, tot = letternumber(passes)
print("{0:.2f}% of Passwords contain a letter and a Number, but no symbol".format(num/tot * 100))
num, tot = numbersymbol(passes)
print("{0:.2f}% of Passwords contain a symbol and a Number, but no letter".format(num/tot * 100))


# In[194]:


num, tot = symbol(passes)
print("{0:.6f}% of Passwords contain only symbols".format(num/tot * 100))
num, tot = letter(passes)
print("{0:.2f}% of Passwords contain only letters".format(num/tot * 100))
num, tot = number(passes)
print("{0:.2f}% of Passwords contain only numbers".format(num/tot * 100))


# In[195]:


num, tot = hasall(passes)
print("{0:.2f}% of Passwords contain all constraints".format(num/tot * 100))


# In[223]:


val = ["Hello","GoodBye","Hello"]
#print(stats.itemfreq(val))
valfreq = np.unique(val,return_counts=True)
print(valfreq)

