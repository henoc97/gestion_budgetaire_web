from fastapi import FastAPI, HTTPException
import asyncpg

app = FastAPI()


# Configurer les informations de connexion à la base de données PostgreSQL
PG_DSN = "postgresql://postgres:henoc2004@127.0.0.1/gestion_budgetaire"


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Fonction pour exécuter la requête personnalisée vers la fonction PostgreSQL
async def execute_query(query: str, *args):
    conn = await asyncpg.connect(PG_DSN)
    try:
        result = await conn.fetch(query, *args)
        return result
    finally:
        await conn.close()

# Route pour exécuter la fonction PostgreSQL et récupérer le résultat
@app.post("/client/budgets")
async def execute_custom_query(client_id: int):
    query = "SELECT * FROM show_mybudget($1)"
    try:
        result = await execute_query(query, client_id)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))