#!/usr/bin/env python
# coding: utf-8

# In[30]:


"""Birtday Paradox Simulation,by Al sweigart al@inventwithpython.com.
Explore the surpriding probabilities of the "Birthday Paradox". 
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com.big-book-small-python-projects
Tags: short, math, simulation"""


# In[17]:


import datetime,random


# In[18]:


def getBirthdays(number0fBirthdays):
    """Returns a list of numberr random date objects for birthdays."""
    birthdays=[]
    for i in range(number0fBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        start0fYear = datetime.date(2001, 1,1)
        
        # Get a random day into the year:
        randomNumber0fDays = datetime.timedelta(random.randint(0,364))
        birthday=start0fYear + randomNumber0fDays
        birthdays.append(birthday)
    return birthdays


# In[19]:


def getMatch(birthdays):
    """Returns the dte object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.
    
    #compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA #Return the matching birthday.


# In[20]:


# Display the intro:
print('''Birthday Paradox,by Al weigart al@inventwithpython.com
The Birtday Paradox shows us that in a group of N people, The odds
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept
(It is not actually a paradox, it is just a surprising result.)''')


# In[21]:


# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


# In[22]:


while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate?(Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount.
print()


# In[23]:


# Generate and display the birhdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        #Display a comma for each birthday after the first birthday.
        print(',', end='')
    monthName = MONTHS[birthday.month-1]
    dateText = '{} {}'.format(monthName,birthday.day)
    print(dateText,  end='')
print()
print()


# In[24]:


# Determine if there are two birthdays that match.
match = getMatch(birthdays)


# In[25]:


# Display the results:
print('In this simulation,', end='')
if match !=None:
    monthName = MONTHS[match.month -1]
    dateText= '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('There are no matching birthdays.')
print()


# In[27]:


# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')


# In[28]:


print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    #Report on the progress every 10,000 simulations:
    if i% 10_000==0:
        print(i, 'simulations run...')
    birthdays= getBirthdays(numBDays)
    if getMatch(birthdays)!= None:
        simMatch = simMatch +1
print('100,000 simulations run.')


# In[29]:


# Display simulation results:
probability = round(simMatch / 100_000*100,2)
print('Out of 100,000 simulations of', numBDays, 'people,there was a')
print('matching birthday in that group', simMatch,'times.This means')
print('that',numBDays, 'people have a', probability,'% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')


# In[ ]:




