from app_engine.budgets.budgets_preprocessing import BudgetService

class BudgetsGraphics : 
    def __init__(self):
        self.BudgetService = BudgetService()

    def getGraphs(self):
        dataFrame, desc, sum_by_budget, sumAll_by_budget =  self.BudgetService.budget_dataFrame_processing(3)
        if dataFrame is not None and not dataFrame.empty:
            fig0 = self.BudgetService.budgets_aggregate(dataFrame)
            fig1 = self.BudgetService.graph_categoryname_budgetamountfix(dataFrame)
            fig2 = self.BudgetService.graph_budgetamount_budgetamountfix_by_periods(dataFrame)
            fig3 = self.BudgetService.graph_budgetamountfix_sppends(dataFrame)
            fig4 = self.BudgetService.graph_mean_min_max_byBudget(dataFrame)
            fig5 = self.BudgetService.graph_pairplot(dataFrame)
            fig6 = self.BudgetService.graph_correlation(dataFrame)
            fig7 = self.BudgetService.graph_budgets_spends_monthly(dataFrame)
            fig = self.BudgetService.graph_test(dataFrame)
        return dataFrame, desc, sum_by_budget, sumAll_by_budget, fig0, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig