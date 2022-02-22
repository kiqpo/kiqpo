def HeadCore(Title="Bionic-Ui", Css=True, Style="./css/core.css", ThemeColor="#119f7f", SiteUrl="www.hey.com", Image_description="this is an image description", Imageurl="", Type="Landing-page", Keywords="", Description="", Author="", Icon="./src/icon.ico"):
    if Css == True:
        return f"""<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="{ThemeColor}" />
    <meta name="description" content="{Description}" />
    <meta name="keywords" content="{Keywords}">
    <meta name="author" content="{Author}" />
    <meta property="og:title" content="{Title}" />
    <meta property="og:url" content="{SiteUrl}" />
    <meta property="og:description" content="{Image_description}" />
    <meta property="og:image" itemprop="image" content="{Imageurl}" />
    <meta property="og:type" content="{Type}"/>
    <link rel="stylesheet" href="./css/material-components.min.css">
    <link href="./css/core.css" rel="stylesheet" />
    <link rel="stylesheet" href="./css/theme.css" />
    <link rel="icon" href="{Icon}" sizes="16x16" type="image/ico" />
      <title>{Title}</title>"""
    else:
        return f"""<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0 /">
    <meta name="theme-color" content="{ThemeColor}" />
    <meta name="description" content="{Description}" />
    <meta name="keywords" content="{Keywords}" />
    <meta name="author" content="{Author}" />
    <meta property="og:title" content="{Title}" />
    <meta property="og:url" content="{SiteUrl}" />
    <meta property="og:description" content="{Image_description}" />
    <meta property="og:image" itemprop="image" content="{Imageurl}" />
    <meta property="og:type" content="{Type}"/>
    <link rel="stylesheet" href="./css/material-components.min.css">
    <link rel="icon" href="{Icon}" sizes="16x16" type="image/ico" />
    <link rel="stylesheet" href="./css/core.css" />
    <link rel="stylesheet" href="./css/theme.css" />
    <title>{Title}</title>"""
