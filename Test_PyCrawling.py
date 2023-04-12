import requests
from bs4 import BeautifulSoup
import pymysql
import re

def getBookInfo(book_tag):
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text

    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text

    bookPub = book_tag.find("span", {"class": "goods_pub"}).text

    # 날짜 값을 'YYYY-MM-DD' 형식으로 변환
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    year, month = re.findall(r'\d+', bookDate)
    bookDate = f'{year}-{month.zfill(2)}-01'

    # 가격 값을 쉼표 없이 숫자로 변환
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    bookPrice = int(bookPrice.replace(',', ''))

    bookRead = book_tag.find("div", {"class": "goods_read"}).text.strip()

    img_tag = book_tag.find("p", {"class": "goods_img"}).find("img")
    
    img_url = img_tag['src']
    return [bookName, bookAuth, bookPub, bookDate, bookPrice, bookRead, img_url]

def save_book_info_to_db(book_info):
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="k404",
            database="book",
            charset="utf8"
        )

        cursor = conn.cursor()

        sql = """
        INSERT INTO Webtoon (name, author, publisher, date, price, description, image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, book_info)
        conn.commit()

        print("Mysql에 데이터가 입력되었습니다.") 

        cursor.close()
        conn.close()
    except Exception as e:
        print("에러가 발생했습니다:", e)



url = 'http://www.yes24.com/24/Category/Display/001001008020?ParamSortTp=05'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ccont_goods_set = soup.find_all('div', {'class': 'cCont_goodsSet'})

    for div in ccont_goods_set:
        book_info = getBookInfo(div)
        # print(book_info)
        save_book_info_to_db(book_info)
else:
    print("Error: Unable to fetch data from the URL.")