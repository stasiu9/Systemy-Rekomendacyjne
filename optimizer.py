import random
import json
from datetime import datetime, timedelta
from pandas import DataFrame


class Optimizer:

    def __init__(self):
        self.days = []
        self.seen_so_far = []
        self.partner_id = None
        self.day_before = None
        self.profit_gain = None
        self.sustained_profit = None
        self.profitsList = []
        self.sustainedList = []
        self.acumulated_profit_gain = 0
        self.acumulated_profit_gainList = []
        self.acumulated_sustained_profit = 0
        self.acumulated_sustained_profitList = []
        self.acumulated_ratio=0
        self.acumulated_ratioList=[]

    def next_day(self, dfToday, clickCost):
        self.addMissingDays(dfToday['click_timestamp'].iloc[0])

        products_today = set(dfToday['product_id'])
        products_excluded = self.__get_excluded_products_pseudorandomly(3.1, 12)
        products_excluded_set = set(products_excluded)
        products_actually_exluded = sorted(list(products_excluded_set.intersection(products_today)))

        products_actually_exludedDatframe = DataFrame(products_actually_exluded, columns=['product_id'])
        products_actually_exluded_merged = products_actually_exludedDatframe.merge(dfToday, how='left')
        self.profit_gain = self.calculate_profit(products_actually_exluded_merged, clickCost)
        productsAfter = dfToday[~dfToday['product_id'].isin(products_actually_exluded)]
        self.sustained_profit = self.calculate_profit(productsAfter, clickCost)


        self.checkMissingDays(dfToday['click_timestamp'].iloc[0])

        day = {
            "day": dfToday['click_timestamp'].iloc[0],
            "productsSeenSoFar": self.seen_so_far,
            "productsToExclude": sorted(products_excluded),
            "productsActuallyExcluded": products_actually_exluded
        }

        self.profitsList.append(self.profit_gain)
        self.sustainedList.append(self.sustained_profit*-1)
        self.acumulated_profit_gain += self.profit_gain
        self.acumulated_profit_gainList.append(self.acumulated_profit_gain)
        self.acumulated_sustained_profit += self.sustained_profit*-1
        self.acumulated_sustained_profitList.append(self.acumulated_sustained_profit)

        if (self.acumulated_profit_gain != 0):
            self.acumulated_ratio = (self.acumulated_profit_gain/self.acumulated_sustained_profit)
        self.acumulated_ratioList.append(self.acumulated_ratio)



        self.days.append(day)
        seenSoFarSet = set(self.seen_so_far)
        seenSoFarSet.update(products_today)
        self.seen_so_far = sorted(list(seenSoFarSet))
        self.day_before = dfToday['click_timestamp'].iloc[0]


        return self.profitsList, self.sustainedList,self.acumulated_profit_gainList, self.acumulated_sustained_profitList,self.acumulated_ratioList

    def __get_excluded_products_pseudorandomly(self, ratio, seed):
        dummy_list_of_potentially_excluded_products = self.seen_so_far
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / ratio)
        random.seed(seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products,
                                          dummy_how_many_products)
        return excluded_products

    def createLogs(self):
        log = {
            "strategy": "random",
            "days": self.days
        }
        fileName = f'logs/log_for_{self.partner_id}.json'
        with open(fileName, 'w') as f:
            json.dump(log, f, ensure_ascii=False, indent=3)

    def checkMissingDays(self, dt_today):
        if (self.day_before == None):
            return

        strip_today_date = datetime.strptime(dt_today, "%Y-%m-%d")
        strip_before_day = datetime.strptime(self.day_before, "%Y-%m-%d")
        difference = strip_today_date - strip_before_day
        if (difference.days >= 2):
            for i in range(1, difference.days):
                newDate = strip_today_date - timedelta(difference.days - i)
                self.fillDate(newDate)

    def fillDate(self, date):
        day = {
            "day": datetime.strftime(date, "%Y-%m-%d"),
            "productsSeenSoFar": [],
            "productsToExclude": [],
            "productsActuallyExcluded": []
        }
        self.days.append(day)

    def calculate_profit(self, df, clickCost):
        if (len(df) == 0):
            return 0
        clicks = len(df)
        partner_income = df[df['Sale'] == True]['SalesAmountInEuro'].sum()
        return clicks * clickCost - partner_income * 0.22

    def addMissingDays(self, dt_today):
        if (self.day_before != None):
            strip_today_date = datetime.strptime(dt_today, "%Y-%m-%d")
            strip_before_day = datetime.strptime(self.day_before, "%Y-%m-%d")
            difference = strip_today_date - strip_before_day
            if (difference.days >= 2):
                for i in range(1, difference.days):
                    self.profit_gain = 0
                    self.sustained_profit = 0
                    self.profitsList.append(self.profit_gain)
                    self.sustainedList.append(self.sustained_profit)
                    self.acumulated_profit_gainList.append(self.acumulated_profit_gain)
                    self.acumulated_sustained_profitList.append(self.acumulated_sustained_profit)
                    self.acumulated_ratioList.append(self.acumulated_ratio)



# profit gain= products_actualyy exluded z dnia dzisiejszeg
# sustained_profit=dzisiejsze po wywyaunie zoptymalizatora
# jakie przekazujesz clickcost
