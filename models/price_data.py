from datetime import date
import pandas as pd


class SalesRecords:
    def __init__(self):
        self.df = pd.read_csv('./models/data.csv')
        self.df['parseddate'] = pd.to_datetime(self.df["date"]).dt.date

    def getProductsInRange(self, start_date: date, end_date: date, department: str):
        productsInRange = self.df[(self.df['parseddate'] > start_date) & (self.df['parseddate']
                                                                          < end_date) & (self.df['department'] == department)]
        grouped_data = productsInRange.groupby('department')['seats'].sum()
        return (grouped_data[0])

    def getNthMostItem(self, item_by, start_date, end_date, n):
        productsInRange = self.df[(self.df['parseddate'] > start_date) & (self.df['parseddate']
                                                                          < end_date)]

        cond = 'seats' if item_by == 'quantity' else 'amount'
        grouped_data = productsInRange.groupby('software')[cond].sum()
        return (grouped_data[n-1])

    def getDepartmentWiseSoldPercentage(self, start_date, end_date):
        productsInRange = self.df[(self.df['parseddate'] > start_date) & (self.df['parseddate']
                                                                          < end_date)]
        department_sales = productsInRange.groupby('department')[
            'amount'].sum()
        total_sales = department_sales.sum()
        department_sales_percentage = (department_sales / total_sales) * 100
        department_sales_percentage = department_sales_percentage.round(2)
        return (department_sales_percentage.to_dict())

    def getMonthlyProductSales(self, product, year):
        self.df['date'] = pd.to_datetime(self.df['date'])
        productsInRange = self.df[(self.df['date'].dt.year == year) & (
            self.df['software'] == product)]
        grouped_data = productsInRange.groupby(pd.Grouper(key='date', freq='M'))[
            'amount'].sum()
        grouped_data_sorted = grouped_data.sort_index()

        month_names_dict = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }
        grouped_data_dict = grouped_data_sorted.to_dict()
        grouped_data_dict_with_month_names = {
            month_names_dict[key.month]: value for key, value in grouped_data_dict.items()}

        # Adding months with 0 sales at the end of the dictionary
        for month in range(1, 13):
            month_name = month_names_dict[month]

            if month_name in grouped_data_dict_with_month_names:
                value = grouped_data_dict_with_month_names[month_name]
            else:
                value = 0

            grouped_data_dict_with_month_names[month_name] = value

        return (grouped_data_dict_with_month_names)
