#!/usr/bin/env python
# coding: utf-8

# In[6]:


num_exh_fan = int(input("How many EXH fans are there? "))
if num_exh_fan <= 1:
    exh_cfm = int(input("What is the CFM of EF1? "))
    exh_duct_size = (exh_cfm/1800*144)
    exh_duct_size = exh_duct_size ** 0.5
    exh_duct_size = round(exh_duct_size)
    mua_cfm = round(exh_cfm * .80)
    mua_duct_size = (mua_cfm/1500*144)
    mua_duct_size = round(mua_duct_size ** 0.5)
    print("EF1 Set to {} cfm" .format(exh_cfm))
    print("MUA1 Set to {} cfm" .format(mua_duct_size))
    print("Recommended Exhaust Duct Size for {} cfm = {} square".format(exh_cfm,exh_duct_size))
    print("Recommended MUA Duct Size for {} cfm = {} square".format(mua_cfm,mua_duct_size))
else:
    exh_cfm_list = [0]
    exh_duct_list = [0]
    for exh_cfms in range(0,num_exh_fan):
        exh_cfms = int(input("Please Enter the CFM's of your EXH fans :"))
        exh_cfm_list.append(cfms)
        exh_duct_size = (exh_cfms/1800*144)
        exh_duct_size = exh_duct_size ** 0.5
        exh_duct_size = round(exh_duct_size)
        exh_duct_list.append(exh_duct_size)
    for final_exh_duct_size in exh_duct_list:
        if final_exh_duct_size > 0:
            print("Exhaust Duct Size for", " is:",final_exh_duct_size,)
    num_mua_fan = int(input("How many MUA fans are there? "))
    mua_cfm_list = [0]
    mua_duct_list = [0]
    if num_mua_fan >= 1:
        for mua_cfms in range(0,num_mua_fan):
            mua_cfms = int(input("Please Enter the CFM's of your MUA fans: "))
            mua_cfm_list.append(mua_cfms)
            mduct = (mua_cfms/1500*144)
            mduct = mduct ** 0.5
            mduct = round(mduct)
            mua_duct_list.append(mduct)
        for final_mua_duct_size in mua_duct_list:
            if final_mua_duct_size > 0:
                print("Make-Up Air Duct Size is:",final_mua_duct_size,)

            
    
 
       
 
   


# In[ ]:





# In[ ]:





# In[ ]:




