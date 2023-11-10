from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse, parse_qs
import csv


def scholar_info(urls):
    all_scholar_info = {}
    for url in urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        html_str = response.text
        soup = BeautifulSoup(html_str, 'html.parser')

        # Scholar's Name
        title_tag_name = soup.find("title")
        scholar_name = title_tag_name.text.split(' - ')[0].strip('\u202a\u202c') if title_tag_name else None

        # Scholar's ID
        parsed_url = urlparse(url)
        url_query_params = parse_qs(parsed_url.query)
        scholar_gsid = url_query_params.get('user', [None])[0]

        # Meta tag: affiliation & research interests
        meta_tag = soup.find('meta', attrs={"name": "description"})
        if meta_tag and meta_tag.has_attr('content'):
            meta_tag_content = meta_tag['content']
            meta_tag_content_split = meta_tag_content.split(' - ')
            scholar_institution = meta_tag_content_split[0].strip("\u202a\u202c")
            scholar_interests = meta_tag_content_split[2:]
            scholar_interests = [interest.strip('\u202a\u202c') for interest in scholar_interests]
        else:
            scholar_institution = 'No Institution Found'
            scholar_interests = ['No Research Interest Found']

        # Dictionary
        all_scholar_info[url] = {
            'Google Scholar ID': scholar_gsid,
            'Scholar Name': scholar_name,
            'Institution': scholar_institution,
            'Research Interests': scholar_interests
        }
    return all_scholar_info



def scholar_articles_url(urls):
    article_urls_dict = {}
    base_url = "https://scholar.google.com"

    for url in urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            html_str = response.text
            soup = BeautifulSoup(html_str, 'html.parser')

            article_urls = []
            for tr in soup.find_all('tr', {"class": "gsc_a_tr"}):
                a_tag = tr.find('a', class_='gsc_a_at')
                if a_tag and a_tag.has_attr('href'):
                    full_url = f"{base_url}{a_tag['href']}"
                    article_urls.append(full_url)

            # Dictionary
            article_urls_dict[url] = article_urls

        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            continue

    return article_urls_dict


def article_info(urls):
    article_info_dict = {}
    for url in urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        html_str = response.text
        soup = BeautifulSoup(html_str, 'html.parser')

        # Author profile Google Scholar ID
        parsed_url = urlparse(url)
        url_query_params = parse_qs(parsed_url.query)
        scholar_gsid = url_query_params.get('user', [None])[0]

        # Title
        title = soup.find('meta', property="og:title")['content'] if soup.find('meta', property="og:title") else None
        title = title.replace('\u202a', '').replace('\u202c', '')
        # Publication date
        publication_date_field = soup.find('div', class_='gsc_oci_field', string='Publication date')
        publication_date = publication_date_field.find_next_sibling('div',
                                                                    class_='gsc_oci_value').text if publication_date_field else None

        # Journal
        journal_field = soup.find('div', class_='gsc_oci_field', string='Journal')
        journal = journal_field.find_next_sibling('div', class_='gsc_oci_value').text if journal_field else None

        # Publisher
        publisher_field = soup.find('div', class_='gsc_oci_field', string='Publisher')
        publisher = publisher_field.find_next_sibling('div', class_='gsc_oci_value').text if publisher_field else None

        # Abstract
        abstract_div = soup.find('div', class_='gsh_csp')
        abstract_text = abstract_div.text if abstract_div else None

        # Dictionary
        article_info_dict[url] = {
            'Google Scholar ID': scholar_gsid,
            'Title': title,
            'Publication Date': publication_date,
            'Journal': journal,
            'Publisher': publisher,
            'Abstract': abstract_text
        }
    return article_info_dict



testing_prof = scholar_info(['https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=YpVDDP8AAAAJ'])
print(testing_prof)