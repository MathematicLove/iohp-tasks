from fastapi import APIRouter, HTTPException
from app.schemas.converter import ConversionRequest, ConversionResponse
from app.services.unit_converter import UnitConverter

router = APIRouter(prefix="/api", tags=["converter"])

@router.get("/categories")
async def get_categories():
    return UnitConverter.get_categories()

@router.get("/units/{category}")
async def get_units(category: str):
    units = UnitConverter.get_units(category)
    if not units:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return {"units": units}

@router.post("/convert", response_model=ConversionResponse)
async def convert(request: ConversionRequest):
    try:
        result = UnitConverter.convert(
            request.category,
            request.from_unit,
            request.to_unit,
            request.value
        )
        return ConversionResponse(
            value=request.value,
            from_unit=request.from_unit,
            to_unit=request.to_unit,
            result=result,
            category=request.category,
            formatted_result=f"{result:.6g}"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера")