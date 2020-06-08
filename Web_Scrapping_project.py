#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import bs4


# In[15]:


res = requests.get("https://en.wikipedia.org/wiki/Certified_Ethical_Hacker")
type(res)


# In[16]:


res.text


# In[71]:


soup = bs4.BeautifulSoup(res.text,"lxml")
scrp1 = soup.select("title")
scrp2 = soup.select(".mw-headline")
scrp3 = soup.select(".div")


# In[72]:


for i in scrp1:
    print(i.getText())
for i in scrp2:
    print(i.getText())


# In[88]:


print("Links scrapped from the Website")
b = "https://en.wikipedia.org"
for link in soup.find_all("a",href = True):
    a = link["href"]
    #removing the hashed links
    if(a[0]!="#"):
        print(a)
    if(a[1]=="/"):
        c = b+a
        print(c)


# In[ ]:




