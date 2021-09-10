# -*- coding: utf-8 -*-

import bs4

def GetTextFromNode(node):
    """
    """
    if node is None:
        return ""

    bodytext = ""
    for content in node.contents:
        if isinstance(content, bs4.NavigableString):
            text = content.string.strip("\r\n\t ")
            if text != "":
                bodytext += text
                if content.parent.name != "a":
                    bodytext += "\r\n"
        else:
            bodytext += GetTextFromNode(content)
            
    return bodytext

def IsTheOnlyString(s):
    """
    """
    return (s == s.parent.string)

def GetMaxTagParentNode(soup):
    """
    """
    stringlist = soup.find_all(string=IsTheOnlyString)
    
    tagdict = {}  # parents tags dict
    for tag in stringlist:
        parent = tag.parent.parent
        if parent not in tagdict.keys():
            tagdict[parent]=0
        tagdict[parent] += len(tag.parent.get_text())

    # we find out the node which contains the most tags
    taglist = sorted(tagdict.items(),key = lambda x:x[1],reverse = True)
    maxnode, maxtexts = taglist[0]

    return maxnode
                           
def GetTitle(soup):
    """
    """
    title=""
    if soup is None:
        return title
    
    try:
        h1title = soup.find("h1").get_text().strip("\r\n\t ")
    except:
        h1title = ""
        
    try:
        titletitle = soup.find("title").get_text().strip("\r\n\t ")
    except:
        titletitle = ""

    if h1title != "" and titletitle != "":
        if len(h1title)>len(titletitle):
            shorts = titletitle
            longs = h1title
        else:
            shorts = h1title
            longs = titletitle

        if longs.startswith(shorts):
            title = shorts
        else:
            title = longs
    else:
        title = h1title+titletitle
        
    return title

def RemoveTag(soup, tagname):
    """
    """
    for tag in soup.find_all(tagname):
        tag.extract()
    return soup

def RemoveUselessTags(soup):
    """
    """
    if soup is None:
        return None
    
    soup = RemoveTag(soup, "style")
    soup = RemoveTag(soup, "script")
    
    # remove comments
    comments = soup.findAll(text=lambda text:isinstance(text, bs4.Comment))
    [comment.extract() for comment in comments]

    return soup

def HTMLText(html):
    """
    """
    if html is None:
        return "", ""
    
    soup = bs4.BeautifulSoup(html, "lxml")
    soup = RemoveUselessTags(soup)
    title = GetTitle(soup)
    mainbodynode = GetMaxTagParentNode(soup)
    htmlmainbodytext = GetTextFromNode(mainbodynode)

    return title, htmlmainbodytext

