#!/usr/bin/env python
# coding: utf-8

# In[1]:


numexhfan = int(input("How many EXH fans are there? "))
if numexhfan <= 1:
    cfm1 = int(input("What is the CFM of EF1? "))
    d1_1 = (cfm1/1800*144)
    d1_2 = d1_1 ** 0.5
    d1_2 = round(d1_2)
    m1 = round(cfm1 * .80)
    m1_1 = (m1/1500*144)
    m1_2 = round(m1_1 ** 0.5)
    print("EF1 Set to {} cfm" .format(cfm1))
    print("MUA1 Set to {} cfm" .format(m1))
    print("Recommended Exhaust Duct Size for {} cfm = {} square".format(cfm1,d1_2))
    print("Recommended MUA Duct Size for {} cfm = {} square".format(m1,m1_2))
else:
    efanlist = [0]
    efanlist2 = [0]
    for cfms in range(0,numexhfan):
        cfms = int(input("Please Enter the CFM's of your EXH fans :"))
        efanlist.append(cfms)
        duct = (cfms/1800*144)
        duct = duct ** 0.5
        duct = round(duct)
        efanlist2.append(duct)
    for ecfms in efanlist2:
        if ecfms > 0:
            print("Exhaust Duct Size is:",ecfms,)
    nummuafan = int(input("How many MUA fans are there? "))
    mfanlist = [0]
    mfanlist2 = [0]
    if nummuafan >= 1:
        for cfms2 in range(0,nummuafan):
            cfms2 = int(input("Please Enter the CFM's of your MUA fans: "))
            mfanlist.append(cfms2)
            mduct = (cfms2/1500*144)
            mduct = mduct ** 0.5
            mduct = round(mduct)
            mfanlist2.append(mduct)
        for mcfms2 in mfanlist2:
            if mcfms2 > 0:
                print("Make-Up Air Duct Size is:",mcfms2,)

            
    
 
       
 
   


# In[ ]:





# In[ ]:





# In[ ]:




