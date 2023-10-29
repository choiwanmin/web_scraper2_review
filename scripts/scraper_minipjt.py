# 웹 스크래핑 코드
import requests
from bs4 import BeautifulSoup
from tenten.models import Recommend


def run():
        for i in range(1,4):
                urls = "https://www.10x10.co.kr/shoppingtoday/shoppingchance_saleitem.asp?sflag=sc&disp=&srm=be&cpg="+str(i)+"&psz=32&chkr=&sP=&flo1=&flo2=&reset="
                urls2 = "https://www.10x10.co.kr/"
                res = requests.get(urls)
                soup = BeautifulSoup(res.text, "html.parser")
                items = soup.select("div.pdtBox")
                for item in items:
                        try:
                                image_link = item.select("img")[0].get("src").strip()
                                title = item.select("img")[0].get("alt").strip()
                                
                                price2 = item.select("span.finalP")[0].text.strip()
                                price = price2.replace(",","").replace("원","")
                                
                                link2 = item.select("a")[0].get("href").strip()
                                link = urls2 + link2
                                
                                dc_rate2 = item.select("strong.cRd0V15")[0].text.strip()
                                dc_rate = dc_rate2.replace("[","").replace("]","").replace("%","")
                                
                                reply_cnt = item.select("li.postView")[0].text.strip()
                                like_cnt = item.select("li.wishView")[0].text.strip()

                                if int(dc_rate) > 10 and int(reply_cnt) > 30 and int(like_cnt) > 100 :
                                        db_link_cnt = Recommend.objects.filter(link__iexact=link).count()

                                        if(db_link_cnt==0):
                                                Recommend(image_link=image_link,link=link,price=price,
                                                        title=title,dc_rate=dc_rate,reply_cnt=reply_cnt,like_cnt=like_cnt).save()
                        except Exception as e:
                                continue