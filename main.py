from json_comparator import Json_Comparator
from optimizer import Optimizer
from partner_reader import Partner_Reader
from simulator_core import Simulator_Core

if __name__ == "__main__":
    partner_id="C0F515F0A2D0A5D9F854008BA76EB537"
    opt = Optimizer()
    p1 = Partner_Reader(partner_id)
    s1 = Simulator_Core(opt,p1)
    s1.simulate_Partner()

    # comparator=Json_Comparator()
    # comparator.compare("logs/log_for_C0F515F0A2D0A5D9F854008BA76EB537.json",
    #                    "logs/partner_C0F515F0A2D0A5D9F854008BA76EB537_random_products.json")
    #
    # comparator=Json_Comparator()
    # comparator.compare("logs/log_for_04A66CE7327C6E21493DA6F3B9AACC75.json",
    #                    "logs/partner_04A66CE7327C6E21493DA6F3B9AACC75_random_products.json")



