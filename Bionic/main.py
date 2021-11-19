from view import *


def RunApp():
    Head(themeColor='#ffffff'),
    Body(
        Text("Craft Beautiful, Fast User Experience", classname='Welcome-text'),
        Text('| Bionic is Python Framework for crafting beautiful, fast user experiences for web and is free and open source', classname='info-text'),
        Img('./src/iMac.png', classname='iMac'),
        Img('./src/iPhone.png', classname='iPhone'),
        Img('./src/iPad.png', classname='iPad'),
        Img('./src/Processor.png', classname='Processor'),

    ),
