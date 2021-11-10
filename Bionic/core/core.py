from core.Head import HeadCore
from core.compile import HTMLFile


HeadTag = ""


def body(*data):
    file = open('./native/index.html', 'w+')

    HtmlTagsList = [*data]
    HtmlTags = ""

    for ele in HtmlTagsList:
        HtmlTags += ele

    file.write(HTMLFile(Body=HtmlTags, Head=HeadTag))
    file.close()


def head(title="Bionic-Ui", css=True, themeColor="#0000000", siteUrl="www.hey.com", image_description="this is an image description", imageurl="", Type="", keywords="", description="", author="", icon="./src/icon.ico"):
    global HeadTag
    HeadTag = HeadCore(Title=title, Css=css, ThemeColor=themeColor, SiteUrl=siteUrl, Image_description=image_description,
                       Imageurl=imageurl, Type=Type, Keywords=keywords, Description=description, Author=author, Icon=icon)
