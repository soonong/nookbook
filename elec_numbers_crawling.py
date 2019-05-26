import time
from libs.elec_num_parser import elec_num_parse
from libs.elec_num_save import elec_num_save
from libs.elec_num_crawl import elec_num_crawl


# 전기공사협회 코드 수집
codes = []
for num in range(1, 1713):
    try :
        time.sleep(0.5)
        pageString = elec_num_crawl(num)
        lists = elec_num_parse(pageString)
        codes.append(lists)
    except:
        print("----end------")

