import requests
import bs4 as bs
import webbrowser
import re

amazon_name_list = []
amazon_price_list = []
amazon_rating_list = []
flipkart_product_list = []
flipkart_price_list = []
flipkart_rating_list = []


item = input("enter product:")
value = item.replace(" ", "")

#model_name = input("Enter model:")
payload = {'k': value}
payload1 = {'q': value}
#r = {'k':'samsung'}
amazon_url = 'https://www.amazon.in/s'
flipkart_url = 'https://www.flipkart.com/search'
#weburl = requests.get(url,params=payload)
# print(weburl.headers)
# for i in weburl.headers:
# print(i)
# print(weburl.cookies)
# print(html)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
amazon_response = requests.get(amazon_url, headers=headers, params=payload)
flipkart_response = requests.get(flipkart_url, headers=headers, params=payload1)
amazon_html = amazon_response.content
flipkart_html = flipkart_response.content
# print(response.content)
#html = weburl.text
print(amazon_response.url)
soup = bs.BeautifulSoup(amazon_html, 'lxml')
soup1 = bs.BeautifulSoup(flipkart_html, 'lxml')
print(soup.title)

# print(soup.title.parent.name)
#divtags = soup.find_all('span')
# print(weburl.status_code)
# print(soup.prettify)
amazon_product_div = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
amazon_price_div = soup.find_all('span', class_='a-price-whole')
amazon_rating_div = soup.find_all('span', class_='a-icon-alt')
if value == 'watch':
        #watch_div = soup.find_all('div',class_='a-size-base-plus a-color-base a-text-normal')
    watch_price = soup.find_all('span', class_='a-price-whole')
    for j in watch_price:
        print(j.text)
    # for i in watch_div:
        # print(i.text)
for name_set in amazon_product_div:
    amazon_name_list.append(name_set.text)
for price_set in amazon_price_div:
    amazon_price_list.append(price_set.text)
for rating_set in amazon_rating_div:
    amazon_rating_list.append(rating_set.text)

# html list 
li_to_title = "<li class='list-group-item'><div class='container'><div class='row'><div class='col-md-12 text-justify'><span class='list-heading'>"
title_to_rating = "</span></div></div><div class='row'><div class='col-md-8 pt-2 font-italic'><span class='list-rating'>"
rating_to_price = "</span></div><div class='col-md-4 pt-2'><span class='list-price'>"
price_to_li = "</span></div></div></div></li>"
data_not_found = "<li class='list-group-item'>Data Not Found Due To Some Reason</li>"


amazon_str = ""
if len(amazon_name_list)>0:
    for amazon_index in range(1, len(amazon_name_list)):
        amazon_str = amazon_str + li_to_title + amazon_name_list[amazon_index] + title_to_rating + \
            amazon_rating_list[amazon_index]+ rating_to_price+'<td>' + \
            amazon_price_list[amazon_index] + price_to_li
else:
    amazon_str = amazon_str + data_not_found

# for amazon_index in range(1,len(amazon_name_list)):
    # print(amazon_name_list[amazon_index])
    # print(amazon_price_list[amazon_index])
    # print(amazon_rating_list[amazon_index])
print('*'*70)
# for rating in spantags:
# print(rating.text)
print('*'*70)
# for price_count in spantags1:
# print(price_count.text)
# print(divtags.next_sibling)

# for flipkart
print(flipkart_response.url)
print(soup1.title)
flipkart_product_div = soup1.find_all('div', class_='_3wU53n')
flipkart_price_div = soup1.find_all('div', class_='_1vC4OE _2rQ-NK')
flipkart_rating_div = soup1.find_all('div', class_='hGSR34')
for product_set in flipkart_product_div:
    flipkart_product_list.append(product_set.text)
for price_set in flipkart_price_div:
    flipkart_price_list.append(price_set.text)
for rating_set in flipkart_rating_div:
    flipkart_rating_list.append(rating_set.text)
# for flipkart_index in range(1,len(flipkart_product_list)):
    # print(flipkart_product_list[flipkart_index])
    # print(flipkart_price_list[flipkart_index])
    # print(flipkart_rating_list[flipkart_index])


flipkart_str = ""
if len(flipkart_product_list)>0:
    for flipkart_index in range(1, len(flipkart_product_list)):
        flipkart_str = flipkart_str + li_to_title + flipkart_product_list[flipkart_index] + title_to_rating + \
            flipkart_rating_list[flipkart_index] + rating_to_price + \
            flipkart_price_list[flipkart_index] + price_to_li
else:
    flipkart_str = flipkart_str + data_not_found

html_code = """
<!doctype html>
<html lang="en">
    <head>
        <title>Product Comparison</title>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
            integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h3 class="display-3 text-center">Product:"""+str(item)+"""</h3>
                </div>
            </div>
        </div>

		<!--Amazon-->
        <div class="container">
            <div class="row">
                <div class="col-md-1"></div>
                <div class="col-md-5">
                    <div class="content">
                        <ul class="list-group">
                            <li class="list-group-item bg-info"><span class="font-weight-bold">Amazon</span>
                                
                            </li>
                            <div class="scroll-list">
								"""+str(amazon_str)+"""
                            </div>
                            <li class="list-group-item bg-info">
                                <a href="""+str(amazon_response.url)+""" class="btn btn-success">Go to Website</a>
                            </li>
                        </ul>
                    </div>
                </div>

				<!--Flipkart-->
				
                <div class="col-md-5">

                    <ul class="list-group">
                        <div class="content">
                            <li class="list-group-item bg-info"><span class="font-weight-bold">Flipkart</span>
                                
                            </li>
                            <div class="scroll-list">
                                """+str(flipkart_str)+"""
                            </div>
                            <li class="list-group-item bg-info">
                                <a href="""+str(flipkart_response.url)+""" class="btn btn-success">Go to Website</a>
                            </li>
                        </div>
                    </ul>

                </div>
                <div class="col-md-1"></div>
            </div>
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
            integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
            crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"></script>
    </body>

</html>

"""

# write on a file
myfile = open('output.html', 'w', encoding="utf-8")
myfile.write(html_code)
myfile.close()
# view on browser
webbrowser.open('output.html')
