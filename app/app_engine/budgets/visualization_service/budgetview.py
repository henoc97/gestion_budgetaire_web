import streamlit as st
from app_engine.design_engine.app_design_engine import MyColors, myFontFamily, myFontSize, myTextStyle
from app_engine.budgets.visualization_service.budgets_graph import BudgetsGraphics

class BudgetsView : 
    def __init__(self):
        self.graph =BudgetsGraphics()
        self.MyColors = MyColors()
        self.myFontFamily = myFontFamily()
        self.myFontSize = myFontSize()
        self.myTextStyle = myTextStyle()
        
    def budget_view(self):
        dataFrame, desc, sum_by_budget, sumAll_by_budget, fig0, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig = self.graph.getGraphs()
        self.myTextStyle.curve_title("Table budgétaire")
        st.write(dataFrame)
        
        self.myTextStyle.curve_title("Table récapitulative")
        st.write(desc)

        self.myTextStyle.curve_title("Table de somme par catégorie de budget")
        st.write(sum_by_budget)

        self.myTextStyle.curve_title("Table de somme totale")
        st.write(sumAll_by_budget)

        # self.myTextStyle.curve_title("Test")
        # st.pyplot(fig)

        self.myTextStyle.curve_title('''Diagrammes à bandes de la moyenne, du minimum, 
                                     du maximum pour chaque catégorie de budget''')
        self.myTextStyle.curve_description('''Ces diagrammes permettent d'avoir une vision claire sur
                                           la moyenne, le minimum, le maximum du montant budgeté, 
                                            dépensé, restant et de la durrée du budget en 
                                           fonction des catégories de budget ''')
        st.write(fig4, unsafe_allow_html=True)
        
        self.myTextStyle.curve_title("Graphiques résultants du tableau récapitulatif")
        self.myTextStyle.curve_description('''Ces graphiques nous donne l'évolution de la moyenne, 
                    du minimum et du maximum au bout de chaque 2 semaines''')
        st.pyplot(fig0)

        self.myTextStyle.curve_title("Diagramme à bandes des budgets et dépenses mensuels")
        self.myTextStyle.curve_description('''Ce graphique permet de faire une comparaison 
                                           entre les budgets et les dépenses mensuels''')
        st.pyplot(fig7)
        
        self.myTextStyle.curve_title("Diagramme à bandes des budgets")
        self.myTextStyle.curve_description('''Ce diagramme nous donnne des informations sur
                                    les catégories de budgets que vous avons en fonction
                                    des montants budgetés''')
        st.pyplot(fig1)

        self.myTextStyle.curve_title('''Analyse comparative des dépenses réelles et budgétées en 
                                fonction de la durée du budget''')
        self.myTextStyle.curve_description('''Ces points représentent la fréquence respective des dépenses, 
                                           budgets et restes par durée du budget. <br/>
                                           Attention : au cas 3, tous points situés en dessous de la 
                                           ligne rouge  est une dépenses > au montant budgeté. ''')   
        st.pyplot(fig2)

        self.myTextStyle.curve_title('''Distribution des variables et les corrélations entre elles''')
        self.myTextStyle.curve_description('''La dispersion des points et les tendances visuelles entre 
                                           les variables peuvent nous donner des informations sur la 
                                           corrélation ou l'absence de corrélation entre elles.''')
        st.pyplot(fig5)

        self.myTextStyle.curve_title('''Corrélations entre les variables''')
        self.myTextStyle.curve_description('''La carte nous donne les niveaux sur une échelle 
                                           de 0 à 1 des liens entre les variables.''')
        st.pyplot(fig6)

        # self.myTextStyle.curve_title("Evolution comparative du montant du budget et les dépenses")
        # self.myTextStyle.curve_description('''Ce graphique montre le comportement du montant budgeté 
        #                             et du montant dépensé réel  au fil du temps''')
        # st.pyplot(fig3)
