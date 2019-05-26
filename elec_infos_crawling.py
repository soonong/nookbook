import time
from libs.elec_info_crawl import elec_info_crawl
from libs.elec_info_parser import elec_info_parse
from libs.elec_info_re_code import elec_info_code
from libs.elec_info_save import elec_info_save

# 전기공사협회 업체정보 수집
result = elec_info_code()

start = 2000
end = 2999

infos = []
for info in result[start:end]: #리절트 리스트안에 1~11까지만 돌려라-0:10]
    time.sleep(0.01)
    pageString = elec_info_crawl(info)
    lists = elec_info_parse(pageString)
    infos.append(lists)

print(len(infos))
elec_info_save(infos)

