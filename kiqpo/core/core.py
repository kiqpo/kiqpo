from turtle import goto, st
from core.Head import HeadCore
from core.compile import HTMLFile


global windowswindowRendersJs
windowswindowRendersJs = ""
HeadTag = ""
global topleavelscript
topleavelscript = ""


def body(*data):
    file = open('./native/index.html', 'w+')

    HtmlTagsList = [*data]
    HtmlTags = ""
    for ele in HtmlTagsList:
        HtmlTags += ele
    file.write(HTMLFile(Body=HtmlTags, Head=HeadTag,
               Topleavel=topleavelscript, WindowswindowRender=windowswindowRendersJs))
    file.close()

    # save same index.html to desktop native dir

    DesktopHTML = open('./desktop/native/index.html', 'w+')

    HtmlTagsList = [*data]
    HtmlTags = ""
    for ele in HtmlTagsList:
        HtmlTags += ele
    DesktopHTML.write(HTMLFile(Body=HtmlTags, Head=HeadTag,
                      Topleavel=topleavelscript, WindowswindowRender=windowswindowRendersJs))
    DesktopHTML.close()


def head(title="Kiqpo", style="./style.css", css=True, themeColor="#119f7f", siteUrl="www.hey.com", image_description="this is an image description", imageurl="#", Type="Landing-page", keywords="Bionic", description="Bionic is Python Framework for crafting beautiful, fast user experiences for web and is free and open source.", author="shajin-sha", icon="./src/icon.ico"):
    global HeadTag
    HeadTag = HeadCore(Title=title, Style=style,  Css=css, ThemeColor=themeColor, SiteUrl=siteUrl, Image_description=image_description,
                       Imageurl=imageurl, Type=Type, Keywords=keywords, Description=description, Author=author, Icon=icon)


def TopLeavelScript(data):
    global topleavelscript
    topleavelscript = data


def Window(*window):
    windows = len(window)
    global windowswindowRendersJs
    Renderingwindow = ""
    for i in range(windows):
        if(Renderingwindow == ""):
            Renderingwindow = Renderingwindow + '"'+window[i]+'"'
        else:
            Renderingwindow = Renderingwindow + "," + '"'+window[i]+'"'

    Renderingwindow = "["+Renderingwindow+"]"

    windowswindowRendersJs = f"""
    const main = document.getElementsByTagName("main")[0];
    let windowRenders = {Renderingwindow}
    main.insertAdjacentHTML('afterbegin',windowRenders[0])"""

    return ""
