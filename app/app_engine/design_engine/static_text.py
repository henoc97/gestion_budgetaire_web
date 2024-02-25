
import streamlit as st
from app_engine.design_engine.app_design_engine import MyColors, myFontFamily, myFontSize, myTextStyle


class TextStatics : 
    def __init__(self):
        self.MyColors = MyColors()
        self.myFontFamily = myFontFamily()
        self.myFontSize = myFontSize()
        self.myTextStyle = myTextStyle()

    def header(self):
        st.markdown(
            f'''<h1 style="color:{self.MyColors.myGreen};
                    font-size:{self.myFontSize.titlesize};
                    font-family:{self.myFontFamily.Helvetica};">
                    Gestion budgétaire
                </h1>''', unsafe_allow_html=True)

        st.write('Dominez vos finances et libérez-vous du stress et atteignez vos objectifs financiers en toute simplicité !')
