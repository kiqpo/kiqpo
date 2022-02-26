import json
from core.Head import HeadCore
from core.compile import HTMLFile


global windowswindowRendersJs
windowswindowRendersJs = ""
HeadTag = ""
global topleavelscript
topleavelscript = ""
global getTheme
getTheme = ""


def body(*data):
    file = open('./kiqpo/native/index.html', 'w+')

    HtmlTagsList = [*data]
    HtmlTags = ""
    for ele in HtmlTagsList:
        HtmlTags += ele
    file.write(HTMLFile(Body=HtmlTags, Head=HeadTag,
               Topleavel=topleavelscript, WindowswindowRender=windowswindowRendersJs, Theme=getTheme))
    file.close()

    # save same index.html to desktop native dir

    DesktopHTML = open('./kiqpo/desktop/native/index.html', 'w+')

    HtmlTagsList = [*data]
    HtmlTags = ""
    for ele in HtmlTagsList:
        HtmlTags += ele
    DesktopHTML.write(HTMLFile(Body=HtmlTags, Head=HeadTag,
                      Topleavel=topleavelscript, WindowswindowRender=windowswindowRendersJs, Theme=getTheme))
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
            Renderingwindow = Renderingwindow + '`'+window[i]+'`'
        else:
            Renderingwindow = Renderingwindow + "," + '`'+window[i]+'`'

    Renderingwindow = "["+Renderingwindow+"]"

    windowswindowRendersJs = f"""
    const main = document.getElementsByTagName("main")[0];
    let windowRenders = {Renderingwindow}
    main.insertAdjacentHTML('afterbegin',windowRenders[0])"""

    return ""


def setTheme(Theme=""):
    if(Theme == ""):
        with open('./kiqpo/config.json') as fp:
            data = json.load(fp)
            primary = data['theme']["primary"]
            secondary = data['theme']["secondary"]
            background = data['theme']['background']
            error = data['theme']['error']
            textSecondary = data['theme']['text-secondary']

        global getTheme
        getTheme = f"""
        document.documentElement.style.setProperty('--primary', '{primary}');
        document.documentElement.style.setProperty('--error', '{error}');
        document.documentElement.style.setProperty('--secondary', '{secondary}');
        document.documentElement.style.setProperty('--background', '{background}');
        document.documentElement.style.setProperty('--textSecondary', '{textSecondary}');

        document.documentElement.style.setProperty('--mdc-theme-on-primary', '{secondary}');
        document.documentElement.style.setProperty('--mdc-theme-primary', '{primary}');
        document.documentElement.style.setProperty('--mdc-theme-error', '{error}');
        """

        return ""
    else:
        with open('./kiqpo/core/themes/const/themes.json') as fp:
            data = json.load(fp)[Theme]
            primary = data["primary"]
            secondary = data["secondary"]
            background = data['background']
            error = data['error']
            textSecondary = data['text-secondary']

            getTheme = f"""
            document.documentElement.style.setProperty('--primary', '{primary}');
            document.documentElement.style.setProperty('--error', '{error}');
            document.documentElement.style.setProperty('--secondary', '{secondary}');
            document.documentElement.style.setProperty('--background', '{background}');
            document.documentElement.style.setProperty('--textSecondary', '{textSecondary}');

            document.documentElement.style.setProperty('--mdc-theme-on-primary', '{secondary}');
            document.documentElement.style.setProperty('--mdc-theme-primary', '{primary}');
            document.documentElement.style.setProperty('--mdc-theme-error', '{error}');
            
            
            """

        return ""
