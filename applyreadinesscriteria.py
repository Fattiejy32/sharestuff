
# coding: utf-8

# In[ ]:


#ApplyReadinessCriteria
clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Ready to Migrate - Replace' if x['Operating System'] !='Windows 10' and  x['Keep-Refresh/Replace'].notnull() and x['W10Mig: Application Readiness']=='Green' else x['Win10 Overall Readiness'], axis=1)

clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Pending - Machine Readiness' if x['Operating System'] !='Windows 10' and x['W10Mig: Application Readiness']=='Green' and x['replace3']==0 and x['Memory (GB)']>8 and x['Win10 Overall Readiness']!= Pending_MachineReadiness  or x['HDD Total Size (GB)']>200  else x['Win10 Overall Readiness'], axis=1)

clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Pending - Application and Machine Readiness' if x['Operating System']!='Windows 10' and x['Memory (GB)']<8 and x['HDD Total Size (GB)']<200 and x['W10Mig: Device Owner Readiness']=='Green' or x['W10Mig: Device Owner Readiness'].isna() else x['Win10 Overall Readiness'], axis=1)

clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Pending - Application Readiness and Replace' if x['Operating System']!='Windows 10' and x['replace3']==1 and x['W10Mig: Application Readiness']=='Red' or x['W10Mig: Application Readiness']=='Blue' or x['W10Mig: Application Readiness'].isna()  or x['Win10 Overall Readiness']!= Pending_ApplicationReadinessandReplace else x['Win10 Overall Readiness'],axis=1)

clean['Win10 Overall Readiness']=clean.apply(lambda x: 'Ready to Migrate' if x['Operating System'] !='Windows 10' and  x['Keep-Refresh/Replace'].notnull() and x['W10Mig: Application Readiness']=='Green' or x['Win10 Overall Readiness']!= ReadytoMigrate  else x['Win10 Overall Readiness'], axis=1)
clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Pending - Application Readiness' if x['Operating System'] !='Windows 10' and x['W10Mig: Device Owner Readiness']=='Green' and x['Memory (GB)']<=8  and x['HDD Total Size (GB)']<=200 and x['W10Mig: Application Readiness']=='Red' or x['Win10 Overall Readiness']!=Pending_Application_Readiness or x['W10Mig: Application Readiness']=='Blue' or x['W10Mig: Application Readiness'].isna() else x['Win10 Overall Readiness'], axis=1)

clean['Win10 Overall Readiness'] = clean.apply(lambda x: 'Migrated to Win10' if x['Operating System']=='Windows 10' else x['Win10 Overall Readiness'], axis=1)

clean['Win10 Overall Readiness']=clean.apply(lambda x: 'Migrated to Win10 - Refresh' if x ['Operating System'] =='Windows 10' and x['Keep-Refresh/Replace']=='Refresh/Replace' else x['Win10 Overall Readiness'], axis=1)

