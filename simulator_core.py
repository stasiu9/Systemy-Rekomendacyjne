import matplotlib.pyplot as plt
import pandas as pd


class Simulator_Core:
    def __init__(self,optimizer,partner_reader):
        self.optimizer=optimizer
        self.partner_reader=partner_reader
        self.optimizer.partner_id=self.partner_reader.partner_id
        self.profits=[]
        self.sustainded=[]
        self.acumulated_profit=[]
        self.acumulated_sustained=[]
        self.acumulated_ratio=[]

    def simulate_Partner(self):
        self.partner_reader.calcluate_partner()
        self.partner_reader.grouping()
        for i in range(len(self.partner_reader.groupedByDay) - 1):
            profit,sustained,acumulated_profit_gain,acumulated_sustained_profit,acm_ratio=self.optimizer.next_day(dfToday=self.partner_reader.groupedByDay[i],clickCost=self.partner_reader.clickCost)
            self.profits=profit
            self.sustainded=sustained
            self.acumulated_profit=acumulated_profit_gain
            self.acumulated_sustained=acumulated_sustained_profit
            self.acumulated_ratio=acm_ratio

        self.optimizer.createLogs()

        print('Profits gain list', self.profits)
        print('Profits gain list length', len(self.profits))

        print('Sustained  list', self.sustainded)
        print('Sustained list length', len(self.sustainded))

        print('Acumlated profit_gain list', self.acumulated_profit)
        print('Acumlated profit_gain list length', len(self.acumulated_profit))

        print('Acumlated Sustained  list', self.acumulated_sustained)
        print('Acumlated Sustained  list length', len(self.acumulated_sustained))

        print('Ratio list',self.acumulated_ratio)
        print('Ratio length',len(self.acumulated_ratio))

        all_data={
            'profit_gain':self.profits,
            'sustained_profit':self.sustainded,
            'accumulated_profit_gain':self.acumulated_profit,
            'accumulated_sustained_profit':self.acumulated_sustained,
            'accumulated_profit_gain_ratio':self.acumulated_ratio
        }

        all_data_dataframe=pd.DataFrame(all_data)

        all_data_dataframe.to_csv('all_data.csv')

        self.createChartProfitAndSustained(self.profits,self.sustainded)
        self.createAcumulatedChart(self.acumulated_profit,self.acumulated_sustained)
        self.createSustainedChart(self.sustainded)
        self.createAccSustainedChart(self.acumulated_sustained)
        self.createProfitChart(self.profits)
        self.createAccProfit(self.acumulated_profit)
        self.createAcumulatedRatio(self.acumulated_ratio)

    def createChartProfitAndSustained(self,profit,sustained):
        plt.plot(profit,label='Profit gain')
        plt.plot(sustained,label='Sustained profit')
        plt.legend()
        plt.grid()
        plt.show()

    def createAcumulatedChart(self,gain,sustained):
        plt.plot(gain, label='Accumulated profit gain')
        plt.plot(sustained, label='Accumulated sustained profit')
        plt.legend()
        plt.grid()
        plt.show()

    def createSustainedChart(self,sustained):
        plt.plot(sustained, label=self.partner_reader.partner_id)
        plt.title('Sustained profit')
        plt.legend()
        plt.grid()
        plt.show()

    def createAccSustainedChart(self,acc_sustained):
        plt.plot(acc_sustained, label=self.partner_reader.partner_id)
        plt.title('Accumulated sustained profit')
        plt.legend()
        plt.grid()
        plt.show()

    def createProfitChart(self,profit):
        plt.plot(profit, label=self.partner_reader.partner_id)
        plt.title('Profit gain')
        plt.legend()
        plt.grid()
        plt.show()

    def createAccProfit(self,acc_profit):
        plt.plot(acc_profit, label=self.partner_reader.partner_id)
        plt.title('Accumulated profit gain')
        plt.legend()
        plt.grid()
        plt.show()

    def createAcumulatedRatio(self,acm_ratio):
        plt.plot(acm_ratio, label=self.partner_reader.partner_id)
        plt.legend()
        plt.title('Accumulated profit gain ratio')
        plt.grid()
        plt.show()
