# Meeting Summary

## 1.17.2024 Wednesday (Professor Zheng, Professor Lang, Mingze Xu)
 - Finding the data description of scholars.
 - Finding publication data from the past 5 years and relative publication citing the scholar's publication.
 - Potential research objective:
     - Claimed interest & Measured interest.
     - Scholar's convergence. If two scholars having different research interests, and they do research together, their research interest might be influenced by each other.
 - Research Plan:
     - Data collection and text mining.
     - Co-author network: weight and frequency
     - Association mining: market basket analysis to find association between topics and keywords in these scholars' works.
     - How scholar's profile change over time.

## 1.25 Thursday (Professor Lang, John Park, Mingze Xu)
 - Data: Scholar's information
     - Institution
     - Fields of interest
 - Scraping Steps
     - Name of publications
     - Go to scopus
     - Scrape the DOI
     - Scrape the abstract
- Notes
     - Pull the abstract, to be able to associated with the scholars
     - Mingze: use the software, read the textbook


## 1.31 Wednesday (Professor Zheng, Professor Lang, Mingze Xu)
 - DOI cannot be obtained with Google Scholar or POP, so Crossref can be used.
 - With the obtained DOI, we use Corpus to scrape the obstact.
 - Works:
     - Keep scraping the data

## 2.1 Thursday (Professor Lang, John Park, Mingze Xu)
 - Set the goal to keep finishing the data
 - Mingze Xu:
     - Manually add the missing information of UCAR scholars
     - Working on the LDA
 - John Park:
     - Finishing the scraping and try to finalize the dataset

  ## 2.7 Wednesday (Professor Zheng, Professor Lang, Mingze Xu)
 - Notes:
     - For each author, do the profile
     - Average the authors
     - author level topic profile, similar to the finished LDA
     - compare authors, create distance, make network
     - topic profile of paired authors
     - how people change their interest as they know each other
