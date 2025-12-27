from pydantic import BaseModel
# Importerar BaseModel från pydantic för att skapa data-modeller

class ErrorResponse(BaseModel): # Modell för felmeddelanden
    error: str # Felmeddelande som text