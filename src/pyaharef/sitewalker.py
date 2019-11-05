#!/usr/bin/python
"""
############################################################################
# TITLE       : sitewalker
# PROJECT     : pyaharef
# ENGINEER    : Jeremiah D. Powell
# PROGRAM     : sitewalker library
# FILE        : sitewalker
# CREATED     : 12-SEPT-2008 JDPOWELL
# DESCRIPTION : Walk a site.
# ASSUMPTIONS : Familiarity with HTTP, Python, urllib2, BeautifulSoup
############################################################################
#                          RELEASE LISCENSE
#
# 	This file is available under copyright
#       2008 Jeremiah D. Powell. For internal
#       use only, keep out of young children.
#
# 	Copyrights to their respective owners.
#
#  Current version : $Ver:0.2$
#  Latest version  : 0.1
#  Bugs, Comments  : waveclaw@waveclaw.net
############################################################################
#                          RELEVANT DOCUMENTS
#                           (REFERENCES)
#
#  Name                            Comment
#  ------------------------------- -------------------------------------
#  ActiveState scraper.py           http://code.activestate.com/recipes/286269/
#  linky.py                         Copyright Michael Foord, 2005,
#   http://voidspace.org.uk/mailman/listinfo/pythonutils_voidspace.org.uk
#
############################################################################
#                          REVISION HISTORY
#Date         Version(Build) SCM      Engineer Comment/Description
#DD-MMM-YYYY  Rel.Patch.Pnt  Reason
#-----------  -------------- -------- -------- -------------------------
#16-SEP-2008  0.1/0.1(1)     WWW00661 Jeremiah Copied from other scripts
############################################################################
#
Sitewalker is a class that walks a website,
optionally doing something at each page.
This is a Web crawler for a single site or related sites.

The useful methods of a Sitewalker instance are :

badurl(expression)  -   set urls to avoid.

walk(url, optionalcommand) - walk a site, using optionalcommand on each page.


The constants defined by a Sitewalker are:

MEDIAURL - a regular expression that limits the walk to only html pages

The following methods are the methods called to handle various parts of walking
the site. In a normal Scraper instance they do nothing and are intended to be
overridden.


findurls(page)
    Called to parse urls

todo(url,page)
    Called on each page as loaded

Typical usage :

  mypage = sitewalker()
  mypage.walk(myurl)

"""
import re, urllib2
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup, SoupStrainer

# use these and add an optional one to restrict bellow start base/root
NOTMEDIAURL = re.compile(r'.*[.](?!html$|htm$|aspx$|pl$|php$|/$).*$')
STARTWITHHTTP = re.compile(r'http://.*')
PROTOCOL = 0
HOST = 1
PATH = 2


def isbad(qlink):
    """
    filter out bad links.
    """
    if None == qlink or '' == qlink:
        return True
    if (qlink.startswith('http://') and (
                            qlink.endswith('.html') or
                            qlink.endswith('.htm') or
                        qlink.endswith('.php') or
                    qlink.endswith('.pl') or
                qlink.endswith('/'))):
        return False
    else:
        return True


def isgood(rlink):
    """
    opposite of isbad
    """
    return not isbad(rlink)


def openlink(link):
    """
    Wrapper for open to filter out bad links.
    """
    if isbad(link):
        return None
    try:
        pagehandle = urllib2.urlopen(link)
    except urllib2.HTTPError, err:
        # serious error, retry the link again then give up?
        print " "
        print "HTTPError:", str(err)
        print "At url:", link
        # ? purge this url from nexurls?
        return None
    except urllib2.URLError, err:
        # bad page, 404 or 302.
        # maybe provide a function to do something like note a dead link
        print " "
        print "HTTPError:", str(err)
        print "At url:", link
        # ? purge this url from nexurls?
        return None
    except IOError:
        return None
    return pagehandle


class SiteWalker:
    """
    Single-site web crawler that walks a site, optionally doing something
         to each page.
    """

    def __init__(self, starturl='http://localhost/'):
        """Initialise a sitewalker."""
        self.url = starturl
        self.baseurl = urlparse(starturl).geturl()
        self.currentbase = self.baseurl
        self.urlfilters = [NOTMEDIAURL, STARTWITHHTTP]

    def reset(self):
        """This method clears the url lists and page content, retaining url,
           bad filter and todo process."""
        self.url = ''
        self.baseurl = ''
        self.currentbase = self.baseurl

    def badurl(self, filterexp=''):
        """
        express what kind of url to avoid
        """
        self.urlfilters.extend([filterexp, ])
        return self


    def fixurl(self, uglyurl):
        """ turn all urls into absolute urls """
        # print "Fixing:", self.currentbase, "and", uglyurl
        uglyurl = uglyurl.strip(" \t\n\r")
        checkdomain = urlparse(uglyurl)[HOST]
        if None == checkdomain or '' == checkdomain:
            fixedurl = urljoin(self.currentbase, urlparse(uglyurl).geturl())
            fixedurl = fixedurl.replace('%7E', '~')
        else:
            if urlparse(self.currentbase)[HOST] == checkdomain:
                fixedurl = uglyurl.replace('%7E', '~')
            else:
                fixedurl = None
        if ( None != fixedurl and fixedurl.endswith('/') ):
            fixedurl = fixedurl + 'index.html'
        return fixedurl

    def findurls(self, rawpage):
        """
        find the page's urls
        """
        newurls = []
        try:
            newurls.extend([self.fixurl(tag['href']) for tag in
                            BeautifulSoup(rawpage, parseOnlyThese=SoupStrainer('a'))
                            if tag.has_key('href')])
        except (ValueError, KeyError):
            print "tag without href"
        return newurls

    def walk(self, url='', visitor=None):
        """
        find all the urls in this page.
        perform the optional cmd if present
        move onto the next page
        """
        if None == url or '' == url:
            url = self.url
        if not url.startswith('http://'):
            url = 'http://' + url
        self.baseurl = urlparse(url).geturl()
        urls = [url, ]
        visited = []

        while 0 < len(urls):
            current = urls.pop()
            while ((current in visited) or
                       (current.replace('index.html', '') in visited)):
                print "Defective list: Attempt to revisit " + current
                current = urls.pop()

            visited.append(current)
            visited.append(current.replace('index.html', ''))
            page = openlink(current)
            if None == page:
                continue
            self.currentbase = page.geturl()
            for link in self.findurls(page):
                if None == link:
                    pass
                else:
                    fixedurl = self.fixurl(link)
                    if isgood(fixedurl):
                        if fixedurl in visited or fixedurl in urls or link in visited or link in urls:
                            pass
                        else:
                            urls.append(fixedurl)
            if visitor:
                page.close()
                page = openlink(current)  # re: links are streamIO, not files
                visitor.visit(page)
            page.close()


class Whereami:
    """
    diagnostic class for Sitewalker
    """
    def __init__(self, page=None):
        """ in the future, retain the page
        :type page: object
        """
        if None != page and '' != page:
            self.page = page

    def reset(self):
        """
        function to clear page
        """
        self.page = None

    def visit(self, page=None):
        """
        tattle on my location
        :type page: object
        """
        if None != page and '' != page:
            self.page = page
        if None == self.page or '' == self.page:
            print "Visited a Null page!"
        else:
            print "Visiting", self.page.geturl()


if __name__ == '__main__':
    TESTWALKER = SiteWalker()
    TESTWALKER.walk("http://localhost/", Whereami)
