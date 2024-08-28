#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


bitmap="""
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


# In[3]:


print('Enter the message to display with the bitmap.')


# In[4]:


message = input('> ')
if message== '':
    sys.exit()


# In[6]:


#Loop over each line in the bitmap:
for line in bitmap.splitlines():
    #Loop over each caracter in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            #Print an empty space since there's a space in the bitmap:
            print(' ',end='')
        else:
            #Print a caracter from the message:
            print(message[i % len(message)],end='')
    print() #Print a newline.


# In[ ]:




