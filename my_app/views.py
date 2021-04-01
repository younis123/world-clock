from requests_html import HTMLSession
from bs4 import BeautifulSoup
session = HTMLSession()

from django.shortcuts import render

# Create your views here.


def index(request):

    response = session.get("https://www.timeanddate.com/worldclock/?sort=1")
    soup = BeautifulSoup(response.content, 'html.parser')
    main_div = soup.find_all('tr')

    data_list = []
    for i in main_div:
        try:
            row1 = i.find('a').text
        except:
            row1 = ''

        try:
            time1 = i.find('td', 'rbi').text
        except:
            time1 = ''

        try:
            row2 = i.find('td').find_next('td').find_next('td').contents[0].text
        except:
            row2 = ''

        try:
            time2 = i.find('td').find_next('td', 'rbi').find_next('td').find_next(
            'td', 'rbi').text  # .find_next('td').find('td', 'rbi').text
        except:
            time2 = ''

        if (row1 and time1) or (row2 and time2):
            data_list.append({'row1': row1, 'time1': time1,
                        'row2': row2, 'time2': time2})

    print(data_list)
    return render(request, 'my_app/home.html', {'data_list':data_list})
