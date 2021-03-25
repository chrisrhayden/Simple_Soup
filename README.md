# basic BeautifulSoup project

## resources

requests is a library to interact with html/the web, we will use to to download
the web page we want to work with

https://requests.readthedocs.io/en/latest/user/quickstart/

BeautifulSoup will be how we parse the html once we have it

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start


## project layout

```text
.
├── .git/             -- the git directory, dont worry to much about this
├── .gitignore        -- a file to tell git what to ignore when asking git to
|                        save your project
├── README.md         -- a file to describe your project and let people know
|                        how to use to use it, github will look for this file and
|                        render it, this is what your seeing now
└── Simple_Soup/      -- its python convention to name the directory containing
    |                    the source files by the name of the project
    ├── __init__.py   -- this is more internal python stuff, dont worry too much
    └── main.py       -- the entry point in to the project
                         while the name 'main' is arbitrary it can help people know
                         where to start looking when reading the source files
```
