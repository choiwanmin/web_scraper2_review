# 웹 스크래핑 코드
import requests
from bs4 import BeautifulSoup
import re
# https://koreapy.tistory.com/692
from tenten.models import Recommend

# https://stackoverflow.com/questions/38489386/python-requests-403-forbidden
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# urls = "https://www.10x10.co.kr/shoppingtoday/shoppingchance_saleitem.asp?gaparam=main_menu_sale"

def run():
        for i in range(1,4):
                urls = "https://www.10x10.co.kr/shoppingtoday/shoppingchance_saleitem.asp?sflag=sc&disp=&srm=be&cpg="+str(i)+"&psz=32&chkr=&sP=&flo1=&flo2=&reset="
                urls2 = "https://www.10x10.co.kr/"
                res = requests.get(urls)
                # print(res)
                soup = BeautifulSoup(res.text, "html.parser")
                # print(soup)
                # print(items)
                items = soup.select("div.pdtBox")
                for item in items:
                        try:
                                image_link = item.select("img")[0].get("src").strip()
                                title = item.select("img")[0].get("alt").strip()
                                price2 = item.select("span.finalP")[0].text.strip()
                                # price = re.sub(r"[^a-zA-Z0-9]","", price)
                                price = price2.replace(",","").replace("원","")
                                print(price)
                                link2 = item.select("a")[0].get("href").strip()
                                link = urls2 + link2
                                dc_rate2 = item.select("strong.cRd0V15")[0].text.strip()
                                # dc_rate = re.sub(r"[^a-zA-Z0-9]","", dc_rate)
                                dc_rate = dc_rate2.replace("[","").replace("]","").replace("%","")
                                reply_cnt = item.select("li.postView")[0].text.strip()
                                like_cnt = item.select("li.wishView")[0].text.strip()

                                # if int(dc_rate) >=10 and int(reply_cnt) >= 30 and int(like_cnt) >= 100 :
                                print('image_link:', image_link)
                                print('title:', title)
                                print('link:', link)
                                print('price', price)
                                print('dc_rate:', dc_rate)
                                print('reply_cnt:', reply_cnt)
                                print('like_cnt:', like_cnt)
                                print('------------------------------------------------------------------------------------------------------------------------')
                                
                                if int(dc_rate) > 10 and int(reply_cnt) > 30 and int(like_cnt) > 100 :
                                        db_link_cnt = Recommend.objects.filter(link__iexact=link).count()

                                        if(db_link_cnt==0):
                                                Recommend(image_link=image_link,link=link,price=price,
                                                        title=title,dc_rate=dc_rate,reply_cnt=reply_cnt,like_cnt=like_cnt).save()
                        except Exception as e:
                                continue