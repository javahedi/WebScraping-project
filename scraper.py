'''
respect the data site owner, 
make reasonable rewquest rate
'''


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    url = 'https://news.ycombinator.com/item?id=29782099'
    response = requests.get(url)

    

    #print(response)
    #print(response.content)


    soup = BeautifulSoup(response.content, "html.parser")
    '''
    go to page 
    right-click--> inspection element-->..
    '''
    elements = soup.find_all(class_="ind", indent=0)  # synatx class already reseved by PYTHON :-)
    comments = [e.find_next(class_="comment") for e in elements]

    keywords = {
        'python'     : 0,
        'javascript' : 0,
        'typescript' : 0,
        'ruby'       : 0,
        'java'       : 0,
        'rust'       : 0,
        'c#'         : 0,
        'c++'        : 0,
        'matlab'     : 0
    }

    for comment in comments:
        comment_tex = comment.get_text().lower()
        words = comment_tex.split(' ')
        #words = [w.strip('.,/:;!@|') for w in words]
        words = {w.strip('.,/:;!@|') for w in words} # is faster :-)

        '''
        - The major and most important difference between sets and list is 
          that unlike lists, Sets cannot store multiple occurrences of the 
          same elements. All elements are unique in a set. 
          If u try to store a duplicate element they will replace the previously 
          stored similar element.

        - Another difference is sets are unordered. Unlike lists when you print 
        a set you wont get the element in the order they were inserted.

        - Sets are unchangeable, once you create a set element cannot be deleted 
        but can only be added.

        companies = {"Apple", "Samsung", "Google", "Amazon", "Walmart"}
        print(companies)
        '''
    

        for k in keywords:
            if k in words:
                keywords[k] +=1

    print(keywords)

    plt.bar(keywords.keys(), keywords.values())
    plt.xticks(rotation=45)
    plt.xlabel('Languages')
    plt.ylabel('# of mentions')
    plt.show()

if __name__=='__main__':
    main()