import csv
import requests
import json
# headers = ['name', 'password']
# rows = [['linao', '123456']
#         , ['wansahijian', '654321']]
#
# with open('test.csv', 'w') as f:
#     f = csv.writer(f)
#     f.writerow(headers)
#     f.writerows(rows)

with open('test.csv', 'r') as f:
    f = csv.reader(f)
    for row, i, j in f:
        r = requests.get('https://www.baidu.com/s?ie=utf-8&csq=1&pstg=22&mod=2&isbd=1&cqid=cb3ef66c00108ffb&istc=4949&ver='
                     'RglwSNMJPLTajeybmfCGnu9W1bh9ZSuMDIO&chk=5d81edf2&isid=A2D0C971ABF36900&wd=%s'
                     '&rsv_spt=1&rsv_iqid=0xbf346c43000a3358&issp=1&f=8&rsv_bp=1&rsv_idx=2&'
                     'ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&_ck=1579.1.48.59.14.720.25&'
                     'rsv_isid=1422_21121_29523_29519_29721_29568_29221_26350&isctg=5&rsv_stat=-2' % row[0])
        print(row, i, j)
