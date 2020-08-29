#!/usr/bin/env python
# coding: utf-8

# In[52]:


#                                                                        #


# In[23]:


# INTEREST RATE CALCULATOR


# In[24]:


# AVERAGE DAILY BALANCE


# In[25]:


avgDailyBalance = 0


# In[26]:


# INPUT BALANCE SHOWN ON BILL FROM USER


# In[27]:


netBalance = float(input('Please enter balance shown on bill: \n'))


# In[28]:


# INPUT PAYMENT MADE FROM USER


# In[29]:


payment = float(input('Please enter payment amount: \n'))


# In[30]:


# INPUT NUMBER OF DAYS IN BILLING CYCLE FROM USER


# In[31]:


d1 = int(input('Please enter number of day(s) in billing cycle: \n'))


# In[32]:


# INPUT NUMBER OF DAYS PAYMENT WAS MADE BEFORE BILLING CYCLE


# In[33]:


d2 = int(input('Please enter number of day(s) payment was made before billing cycle: \n'))


# In[34]:


# INPUT MONTHLY RATE OF INTEREST FROM USER


# In[35]:


monthly_interest = float(input('Please enter monthly interest: \n'))


# In[36]:


# CALCULATE THE INTEREST 


# In[37]:


avgDailyBalance = (netBalance * d1 - payment * d2) / d1


# In[38]:


# REVIEW RESULT OF AVGDAILYBALANCE CALCULATION


# In[39]:


avgDailyBalance


# In[40]:


interest =  avgDailyBalance * monthly_interest


# In[41]:


# REVIEW RESULT OF INTEREST CALCULATION


# In[42]:


interest 


# In[47]:


# OUTPUT INTEREST TO USER


# In[ ]:


print('Calculating....10%')


# In[ ]:


print('Calculating 20%')


# In[ ]:


print('Calculating 30%')


# In[ ]:


print('Calculating 40%')


# In[ ]:


print('Calculating 50%')


# In[ ]:


print('Calculating 60%')


# In[ ]:


print('Calculating 70%')


# In[ ]:


print('Calculating 80%')


# In[ ]:


print('Calculating 90%')


# In[ ]:


print('Calculating 100%')


# In[55]:


print('Your interest is: $', end = '')


# In[56]:


print('{0:.2f}'.format(interest))


# In[ ]:





# In[ ]:




