import requests
import json
import pandas as pd
import time

def get_page_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    url = "	https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN";
    data = {"pageNo": "0", "pageSize": "15",
            "isin": "", "bondCode": "",
            "ssueEnty": "", "bondType": "100001",
            "couponType": "", "issueYear": "", "rtngShrt": "", "bondSpclPrjctVrty": ""}
    response = requests.post(url, data=data,headers=headers)
    js_obj = json.loads(response.text)
    page_total = js_obj["data"]["pageTotal"]

    columns = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]
    df = pd.DataFrame()
    for i in range(page_total):
        data["pageNo"] = i
        response = requests.post(url, data=data,headers=headers)
        js_obj = json.loads(response.text)
        temp = pd.DataFrame(js_obj["data"]["resultList"])
        temp = temp[["isin", "bondCode", "entyFullName", "bondType", "issueStartDate", "debtRtng"]]
        df = pd.concat([df,temp])
        time.sleep(2)
    df.columns = columns
    return df

if __name__ == '__main__':
    result = get_page_data()
    result.to_csv("./pageData.csv")
    print(result)

