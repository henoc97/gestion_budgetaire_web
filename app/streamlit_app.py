import streamlit as st
from app_engine.design_engine.static_text import TextStatics
from app_engine.budgets.visualization_service.budgetview import BudgetsView


BudgetsView = BudgetsView()
TextStatics = TextStatics()

# Interface utilisateur Streamlit
TextStatics.header()
# Demander à l'utilisateur d'entrer l'identifiant du client

BudgetsView.budget_view()
    
