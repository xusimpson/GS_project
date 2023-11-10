# scrapy_GS

## functions:

### scholar_info
Description: 
Input: a list of URL strings
Output: a dictionary: 
'Google Scholar ID': scholar_gsid
'Scholar Name': scholar_name
'Institution': scholar_institution
'Research Interests': scholar_interests


### scholar_articles_url
Description: 
Input: a list of URL strings
Output: a dictionary
'article_urls_dict': URLs

### article_info
Description: 
Input: a list of URL strings
Output: a dictionary:
'Google Scholar ID': scholar_gsid,
'Title': title
'Publication Date': publication_date
'Journal': journal
'Publisher': publisher
'Abstract': abstract_text

### USE
By function scholar_info, we acquire the information of the scholars.
By function scholar_articles_url, we acquire the articles of the scholar.
By function article_info, we input the URL acquired from 'scholar_articles_url', and output the information.
