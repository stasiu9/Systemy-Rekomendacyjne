import matplotlib.pyplot as plt



class Simulator_Core:
    def __init__(self,optimizer,partner_reader):
        self.optimizer=optimizer
        self.partner_reader=partner_reader
        self.optimizer.partner_id=self.partner_reader.partner_id
        self.profits=[]
        self.sustaineds=[]
        self.acumulated_profit=[]
        self.acumulated_sustained=[]
        self.acumulated_ratio=[]

    def simulate_Partner(self):
        self.partner_reader.calcluate_partner()
        self.partner_reader.grouping()
        for i in range(len(self.partner_reader.groupedByDay) - 1):
            profit,sustained,acumulated_profit_gain,acumulated_sustained_profit,acm_ratio=self.optimizer.next_day(dfToday=self.partner_reader.groupedByDay[i],clickCost=self.partner_reader.clickCost)
            self.profits=profit
            self.sustaineds=sustained
            self.acumulated_profit=acumulated_profit_gain
            self.acumulated_sustained=acumulated_sustained_profit
            self.acumulated_ratio=acm_ratio

        self.optimizer.createLogs()

        print('Profits gain list', self.profits)
        print('Profits gain list length', len(self.profits))

        print('Sustained  list', self.sustaineds)
        print('Sustained list length', len(self.sustaineds))

        print('Acumlated profit_gain list', self.acumulated_profit)
        print('Acumlated profit_gain list length', len(self.acumulated_profit))

        print('Acumlated Sustained  list', self.acumulated_sustained)
        print('Acumlated Sustained  list length', len(self.acumulated_sustained))

        print('Ratio list',self.acumulated_ratio)
        print('Ratio length',len(self.acumulated_ratio))




        self.createChart(self.profits,self.sustaineds)
        self.createAcumulatedChart(self.acumulated_profit,self.acumulated_sustained)
        self.createAcumulatedRatio(self.acumulated_ratio)

    def createChart(self,profit,sustained):
        plt.plot(profit,label='profit_gain')
        # plt.plot(sustained,label='sustained')
        plt.show()

    def createAcumulatedChart(self,gain,sustained):
        # plt.plot(sustained, label='sustained')
        plt.plot(gain, label='profit_gain')
        plt.show()

    def createAcumulatedRatio(self,acm_ratio):
        plt.plot(acm_ratio, label='acm')
        plt.show()
