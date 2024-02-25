import streamlit as st

class MyColors : 
    def __init__(self):
        self.myGreen = "#{:02x}{:02x}{:02x}".format(31, 124, 115)
        self.myBlack = "#{:02x}{:02x}{:02x}".format(14, 20, 21)
        self.myRed = "#{:02x}{:02x}{:02x}".format(233, 41, 7)


class myFontFamily:
    def __init__(self):
        self.Helvetica = "HelveticaNeue-Light"


class myFontSize:
    def __init__(self):
        self.titlesize = "50px"

class myTextStyle : 
    def __init__(self):
        self.myFontFamily = myFontFamily()
        self.MyColors = MyColors()

    def curve_title(self, the_text) : 
        return st.write(f'''<h3 style="color:{self.MyColors.myGreen};
                font-family:{self.myFontFamily.Helvetica};">
                {the_text}
            </h3>''',unsafe_allow_html=True, )

    def curve_description(self, the_text) : 
        return st.write(f'''<p style="color:{self.MyColors.myBlack};
                font-family:{self.myFontFamily.Helvetica};">
                    {the_text}
            </p>''', unsafe_allow_html=True, )