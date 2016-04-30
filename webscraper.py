from bs4 import BeautifulSoup
import urllib3
import requests


def get_website():
    url = 'http://rosettacode.org/wiki/Copy_a_string'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content)
    return soup


# def get_language(soup):
#     languages = []
#     posts = soup.select("h2 > span")
#     for post in posts:
#         if post.text != "[edit]":
#             languages.append(post.text)
#     return languages


def get_code_examples(soup, languages):
    language_list = dict((x, []) for x in languages)
    lines = soup.select('pre')
    for line in lines:
        if line.has_attr("class"):
            for key, value in language_list.items():
                if line['class'][0] == key.lower():
                    language_list[key].append(line.text)
    return language_list


def get_languages():
    languages = ['C', 'Csharp', 'lisp', 'Clojure', 'Haskell', 'Java',
                 'JavaScript', 'OCaml', 'Perl', 'PHP', 'Python', 'Ruby',
                 'Scala', 'Scheme']
    return languages


soup = get_website()
get_language(soup)
get_code_examples(get_website(), get_languages())
# c = soup.find_all('pre', class_='c highlighted_source')
#
# pre_class = soup.select("pre")
# span_class = soup.select("pre > span")
# h2 = soup.select("h2")

# for p in pre_class:
#     for s in span_class:
#         print(p.string)
#         print(s.string)

# for p in pre_class:
    # if p.string == None:
    #     for s in span_class:
    #         print(s.string)
    # else:
    # print(p.string)


# span = soup.select("pre > span")
# for s in span_class:
#     print(s.string)
