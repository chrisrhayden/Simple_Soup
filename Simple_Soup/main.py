# this is a way to conveniently import a single part of a bigger library
from bs4 import BeautifulSoup

# we could do the same here but is not really a big deal and requests.get() is
# very informative compared to just get()
import requests


# this is a very simple function, while it looks a bit useless its nice to be
# able to think about things like lego blocks,
# once we know this function works we can forget about how it was implemented
# and treat get_html_text(the_url) as if it was the text itself
def get_html_text(url):
    """
    get the raw html text to give to BeautifulSoup

    this is a doc string, its an official way to document how a function works

    the cool thing is that many tools will show this to the user when they ask
    for documentation of a given function

    while its silly for such a simple function its good practise to add them

    see here for more https://www.python.org/dev/peps/pep-0257/
    """
    # use the requests library to download the given web page
    #
    # get corresponds to the http GET method but you can otherwise ignore that,
    # see here https://www.w3schools.com/tags/ref_httpmethods.asp for more
    r = requests.get(url)

    # now we just return the raw text
    return r.text


def get_bio(soup):
    """ extract the text from a computerhistory.org biography """

    # while you could use BeautifulSoup to sift through the raw html its more
    # easy to use your browses built in tools
    # 1. right click the web page in question and find `inspect element`
    # 2. find the `pick element` icon click it
    # 3. then click the part of the web page you want to get at, in this case we
    # are getting the basic description so we find the element that contains the
    # info we want
    # 4. find the elements you want to extract and then use BeautifulSoup to pull
    # them out

    # in this case we are lucky that the only `<p>` tags in the
    # web page are the content we want but it is usually much harder, so just as
    # an example we are searching for the element that contains the info then
    # getting all of the data form that

    # get the wrapping div element that contains the biography
    content = soup.find("div", class_="content")
    # print(content)

    # now get all the paragraph tags from that elemnt
    p_tags = content.find_all("p")
    # print(p_tags)

    # i didn't realize that find_all gave back a list not another `soup` object
    # so i got a syntax error, i kinda assumed that was this was the case so i
    # tried to index it and it worked
    # print(p_tags.get_text())
    # print(p_tags[0].get_text())

    # these two lines are equivalent but i prefer function calls when i can
    # full_text = ""
    full_text = str()

    for p in p_tags:
        # print(text)
        # now concat (concatenate) all the text from the p tags together
        full_text += p.get_text()

    # print(full_text)
    return full_text


# while python doesn't have such a notion a lot of programing languages use a
# `main` function as the main entry point in to the program so it makes sens to
# do the same here even if its arbitrary
def main():
    """
    the main entry point in the program

    the whole program will weave in and out of this function
    """

    # the web page to use
    url_to_web_page = "https://www.computerhistory.org/babbage/adalovelace/"

    # testing the get_html_text function
    # print(get_html_text(url_to_web_page))

    # get the web page as raw html text
    html_text = get_html_text(url_to_web_page)

    # get the web page as a python `object` the name soup is just for fun and to
    # stay consistent with the BeautifulSoup docs (documentation)
    soup = BeautifulSoup(html_text, "html.parser")

    # checking the soup
    # print(soup)

    text = get_bio(soup)

    # now just print the text we just got to the console
    print(text)


# this is an internal python thing that basically says
# do this if this was the file given on the cli (command line interface)
# dont worry to much about it now but you will start to see this around
if __name__ == "__main__":
    main()
