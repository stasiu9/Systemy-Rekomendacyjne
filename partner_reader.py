import pandas as pd

from optimizer import Optimizer


class Partner_Reader:

    def __init__(self, partner_id):
            self.df = pd.read_csv("/Users/stasiu/Desktop/studia/sem7/criteo/partners/partner_id_" + str(partner_id)+".csv")
            self.clicks=0
            self.groupedByDay=[]
            self.partner_id=partner_id
            self.clickCost=0

    def calcluate_partner(self):
        self.clicks=len(self.df)
        profit_PerDaySum=self.df[self.df['Sale'] ==True]['SalesAmountInEuro'].sum()
        self.clickCost=(profit_PerDaySum*0.12)/self.clicks

    def grouping(self):
        for index,group in self.df.groupby('click_timestamp'):
            self.groupedByDay.append(group)



