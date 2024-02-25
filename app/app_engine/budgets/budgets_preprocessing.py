from app_engine.app_endpoints_engine import MyEndpoints
import pandas as pd
import matplotlib.pyplot as plt
from app_engine.design_engine.app_design_engine import MyColors
import seaborn as sns
sns.set_theme(color_codes=True)
import numpy as np
from ydata_profiling import ProfileReport

class BudgetService:
    def __init__(self):
        self.MyEndpoints = MyEndpoints()
        self.MyColors = MyColors()

    def budget_dataFrame_processing(self, client_id):
        result = self.MyEndpoints.get_client_budgets(int(client_id))
        if result:
            dataFrame = pd.DataFrame(result["result"])
            dataFrame.drop(["id", "userid"], axis=1, inplace=True)
            dataFrame['categoryname'] = dataFrame['categoryname'].astype(str)
            dataFrame.set_index('begindate', inplace=True)
            dataFrame.index.name = "Date"
            dataFrame.rename(columns=
                {"categoryname":"Nom du budget",
                "budgetamount":"Montant restant",
                "periods":"Durée du budget",
                "budgetamountfix":"Montant du budget"}, inplace=True)
            dataFrame['Nom du budget'] = dataFrame['Nom du budget'].astype(str)
            dataFrame.index = pd.to_datetime(dataFrame.index)
            dataFrame["Montant dépensé"] = dataFrame["Montant du budget"]-dataFrame["Montant restant"]
            sum_by_budget =  dataFrame.groupby('Nom du budget').agg(Montant_du_budget=('Montant du budget', 'sum'),
                                                       Montant_dépensé=('Montant dépensé', 'sum'),
                                                       Montant_restant=('Montant restant', 'sum'),
                                                       Durée_du_budget=('Durée du budget', 'sum'))

            sumAll_by_budget = sum_by_budget.sum().drop("Durée_du_budget", axis=0)
            sum_by_budget['Nombre'] =  dataFrame["Nom du budget"].value_counts()
            description = dataFrame.describe()

            return dataFrame, description, sum_by_budget, sumAll_by_budget
        
    def budgets_aggregate(self, df):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        df["Montant dépensé"].resample("2W").agg(["mean", "min", "max"]).plot(kind='bar',ax=axes[0])
        axes[0].set_title("Montant dépensé")

        df["Montant du budget"].resample("2W").agg(["mean", "min", "max"]).plot(kind='bar',ax=axes[1])
        axes[1].set_title("Montant du budget")

        df["Durée du budget"].resample("2W").agg(["mean", "min", "max"]).plot(kind='bar',ax=axes[2])
        axes[2].set_title("Durée du budget")
        return fig
        
    def graph_categoryname_budgetamountfix(self, df):
        if df is not None and not df.empty:
            largeur_barre = 0.35
            axe_x_budget = np.arange(len(df["Nom du budget"]))
            axe_x_depense = [x + largeur_barre for x in axe_x_budget]
            
            fig, ax = plt.subplots()
            ax.bar(axe_x_budget, df["Montant du budget"], largeur_barre, label='Budgeté', color=self.MyColors.myGreen )
            ax.bar(axe_x_depense, df["Montant dépensé"], largeur_barre, label='Dépensé', color=self.MyColors.myRed )
            ax.set_xlabel("Nom du budget")
            ax.set_ylabel("Montant")
            ax.set_title("Bar Chart de  Montant par budget")
            # Rotation des étiquettes de catégorie à 90 degrés
            ax.set_xticks(axe_x_budget + largeur_barre / 2)
            ax.set_xticklabels(df["Nom du budget"], rotation=90)
            ax.legend()
            return fig
        
    def graph_budgetamount_budgetamountfix_by_periods(self, df):
        if df is not None and not df.empty:
            df = df.sort_values(by="Durée du budget")
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))

            axes[0].bar(df["Durée du budget"], df["Montant dépensé"], 
                         alpha=0.7,
                          label="Montant dépensé", color=self.MyColors.myRed)
            
            axes[1].bar(df["Durée du budget"], df["Montant du budget"], 
                         alpha=0.7,
                            label="Montant budgété", color=self.MyColors.myGreen)
            
            axes[2].bar(df["Durée du budget"], df["Montant restant"], 
                        alpha=0.7,
                            label="Montant restant", color=self.MyColors.myBlack)
            axes[2].plot(df["Durée du budget"], np.zeros(len(df["Durée du budget"])), color = self.MyColors.myRed)
            axes[0].set_ylabel("Montant")
            
            axes[0].set_xlabel("Durée en jour")
            axes[1].set_xlabel("Durée en jour")
            axes[2].set_xlabel("Durée en jour")

            axes[0].set_title("Les dépenses")
            axes[1].set_title("Les budgets")
            axes[2].set_title("Les restants")
            
            

            return fig


    def graph_budgetamountfix_sppends(self, df):
        if df is not None and not df.empty:
            
            fig, ax = plt.subplots()
            df["Montant du budget"].plot(ax = ax, marker='*', linestyle = "dashed",
                          label="Montant budgeté", color=self.MyColors.myGreen)
            df["Montant dépensé"].plot(ax = ax, marker='o', linestyle = "dashed",
                          label="Montant dépensé", color=self.MyColors.myRed)
            

            ax.fill_between(df.index, df["Montant du budget"], 
                        where=df["Montant du budget"] >= df["Montant dépensé"],
                         color='lightgreen', alpha=0.3)
            ax.fill_between(df.index, df["Montant du budget"], 
                        where=df["Montant du budget"] <= df["Montant dépensé"],
                         color=self.MyColors.myRed, alpha=0.3)
        
            ax.set_xlabel("Date")
            ax.set_ylabel("Montant du budget")
            ax.set_title("Budgets et dépenses en fonction du temps") 
            ax.legend()
            
            return fig
        
    def graph_mean_min_max_byBudget(self, df):
        if df is not None and not df.empty:
            newDf = df.groupby('Nom du budget').agg(["mean", "min", "max"])
            fig, axes = plt.subplots(2, 2)
            newDf['Montant du budget'].plot(kind='bar',ax=axes[0, 0], fontsize=8)
            newDf['Montant dépensé'].plot(kind='bar',ax=axes[0, 1], fontsize=8, legend=False)
            newDf['Montant restant'].plot(kind='bar',ax=axes[1, 0], fontsize=8, legend=False)
            newDf['Durée du budget'].plot(kind='bar',ax=axes[1, 1], fontsize=8, legend=False)

            for i in [0, 1]:
                axes[0, i].set_xlabel("")
                axes[0, i].set_xticklabels("")
            
            for i, j in zip([axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]], 
                            ["Montant du budget", "Montant dépensé", "Montant restant", 
                             "Durée du budget"]):
                i.set_title(j)

            return fig
        
    def graph_pairplot(self, df):
        if df is not None and not df.empty:
            return sns.pairplot(df)
        
        
    def graph_correlation(self, df):
        if df is not None and not df.empty:
            df = df.drop("Nom du budget", axis=1)
            fig = plt.figure()  # Créez une nouvelle figure
            sns.heatmap(df.corr(), annot=True, cmap="BrBG")  # Dessinez le heatmap sur la figure
            return fig  # Passez la figure à st.pyplot()
    
    def graph_budgets_spends_monthly(self, df) : 
        if df is not None and not df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))

            df["Montant du budget"].resample("M").agg(["sum"]).plot(kind='bar',
                                                                     ax=ax, position=1.5, 
                                                                     width=0.2, color=self.MyColors.myGreen, 
                                                                     label='Montant du budget')

            df["Montant dépensé"].resample("M").agg(["sum"]).plot(kind='bar', 
                                                                  ax=ax, position=0.5, 
                                                                  width=0.2, color=self.MyColors.myRed, 
                                                                  label='Montant dépensé')

            ax.legend(["Budget", "Dépenses"])

            return fig
        

        
    def graph_test(self, df):
        if df is not None and not df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))

            df["Montant du budget"].resample("M").agg(["sum"]).plot(kind='bar',
                                                                     ax=ax, position=1.5, 
                                                                     width=0.2, color=self.MyColors.myGreen, 
                                                                     label='Montant du budget')

            df["Montant dépensé"].resample("M").agg(["sum"]).plot(kind='bar', 
                                                                  ax=ax, position=0.5, 
                                                                  width=0.2, color=self.MyColors.myRed, 
                                                                  label='Montant dépensé')

            
            # Ajouter une légende
            ax.legend(["Budget", "Dépenses"])

            return fig