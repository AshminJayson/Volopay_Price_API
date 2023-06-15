from fastapi import APIRouter
from datetime import date, datetime

from models.price_data import SalesRecords


router = APIRouter(prefix="/api")
ob = SalesRecords()


@router.get("/")
async def get_basic():
    return {'hey': 1}


@router.get("/total_items")
async def get_total_items(start_date: str, end_date: str, department: str) -> int:
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    count = ob.getProductsInRange(start_date, end_date, department)
    return count


@router.get("/nth_most_total_item")
async def get_nth_most_total_item(item_by: str, start_date: str, end_date: str, n: int) -> str:
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    item = ob.getNthMostItem(item_by, start_date, end_date, n)
    return item


@router.get("/percentage_of_department_wise_sold_items")
async def get_percentage_of_department_wise_sold_items(start_date: str, end_date: str):
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    departments_sales_percentage = ob.getDepartmentWiseSoldPercentage(
        start_date, end_date)

    return departments_sales_percentage


@router.get("/monthly_sales")
async def get_monthly_sales(product: str, year: int):
    monthlyProductSales = ob.getMonthlyProductSales(product, year)
    return monthlyProductSales
