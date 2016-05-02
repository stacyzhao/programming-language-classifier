from bs4 import BeautifulSoup
import requests
import csv


def get_main_website():
    url = 'http://rosettacode.org/mw/index.php?title=Special:Ask&offset=15&limit=20&q=%5B%5BIs+task%3A%3Atrue%5D%5D&p=format%3Dbroadtable%2Fsearchlabel%3Dmore...&sort=Modification+date&order=desc'
    # requests to get contents
    res = requests.get(url)
    res.raise_for_status()
    # return text into BeautifulSoup object
    return BeautifulSoup(res.content)


def get_links(soup):
    find_link = soup.select('td')
    return ['http://rosettacode.org' + line.a['href'] for line in find_link]


def loop_links(links):
    master = dict((x, []) for x in get_languages())
    for link in links:
        soup = get_website(link)
        get_code_examples(soup, master)
    return master


def get_website(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content)
    return soup


def get_languages():
    languages = ['C', 'Csharp', 'lisp', 'Clojure', 'Haskell', 'Java',
                 'JavaScript', 'OCaml', 'Perl', 'PHP', 'Python', 'Ruby',
                 'Scala', 'Scheme']
    return languages


def get_code_examples(soup, dictionary):
    lines = soup.select('pre')
    for line in lines:
        if line.has_attr("class"):
            for key, value in dictionary.items():
                if line['class'][0] == key.lower():
                    dictionary[key].append(line.text)


def get_characters():
    characters = ['[', ']', '{', '}', '()', 'var', 'public', 'class', 'java',
                  'fib', 'static', 'print', 'println', 'int', 'return']
    return characters


def check_frequency(dictionary):
    frequency_count = dict((lang, {char: 0 for char in get_characters()}) for lang in get_languages())
    for lang in get_languages():
        for snippet in dictionary[lang]:
            for char in get_characters():
                frequency_count[lang][char] += snippet.count(char)
    return frequency_count



soup = get_main_website()
get_links(soup)
master = loop_links(get_links(soup))
print(check_frequency(master))

def create_csv(dict):
    with open("data.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(master.keys())
        writer.writerows(zip(*master.values()))
