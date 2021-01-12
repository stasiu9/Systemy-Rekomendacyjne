import json

class Json_Comparator():

    def compare(self,my_log,diff_log):
            with open(diff_log) as f:
                diff_log = json.load(f)
            with open(my_log) as g:
                my_log = json.load(g)

            if(diff_log==my_log):
                print('Logs are equal')
            else:
                print('Logs are not equal')