from django.shortcuts import render
from django.http import JsonResponse


def china_wuhan_static(request):
    return render(request, 'china-wuhan-static.html')


def china_wuhan(request):
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver

    try:
        target = 'https://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579579384&enterid=1579579384&from=groupmessage&isappinstalled=0'
        # req = requests.get(url=target)
        # req.encoding = 'urf-8'
        # html = req.text
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option,后台运行
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(target)
        js = "var q=document.documentElement.scrollTop=1500"
        driver.execute_script(js)
        selenium_page = driver.page_source
        driver.quit()
        soup = BeautifulSoup(selenium_page, 'html.parser')
        cities = soup.find('div', {'class': 'areaBox___3jZkr'})
        # 每个省
        protocols = cities.find_all('div')
        data = {}

        for i in protocols:
            try:
                first = i.find('div', {'class': 'areaBlock1___3V3UU'})
                content = first.find_all('p')
                name = content[0].get_text()
                num = content[1].get_text()
                if num == "":
                    num = 0
                data['{}'.format(name)] = num
            except AttributeError as e:
                continue
    except:
        data = {}


    protocols = ["南海诸岛",'北京','天津','上海','重庆','河南',
                 '云南','辽宁','黑龙江','湖南','安徽','山东',
                 '新疆','江苏','浙江', '江西','湖北','广西',
                 '甘肃', '山西', '内蒙古','吉林', '福建','贵州',
                 '广东','青海','西藏', '四川','宁夏','海南',
                 '台湾','香港','澳门'
                 ]
    context = {
        'protocols': protocols,
        'data': data
    }
    return render(request, 'china-wuhan.html', context=context)


def china_wuhan_virus(request):
    if request.method == 'GET':
        import requests
        from bs4 import BeautifulSoup
        from selenium import webdriver

        target = 'https://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579579384&enterid=1579579384&from=groupmessage&isappinstalled=0'
        req = requests.get(url=target)
        req.encoding = 'urf-8'
        html = req.text
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option,后台运行
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(target)
        js = "var q=document.documentElement.scrollTop=1500"
        driver.execute_script(js)
        selenium_page = driver.page_source
        driver.quit()
        soup = BeautifulSoup(selenium_page, 'html.parser')
        cities = soup.find('div', {'class': 'areaBox___3jZkr'})
        # 每个省
        protocols = cities.find_all('div')
        # data = []
        data = {}
        for i in protocols:
            try:
                # protocol = {}
                first = i.find('div', {'class': 'areaBlock1___3V3UU'})
                content = first.find_all('p')
                name = content[0].get_text()
                num = content[1].get_text()
                if num == "":
                    num = 0
                data['{}'.format(name)] = num
                # data.append(protocol)
            except AttributeError as e:
                continue

        # return HttpResponse(json.dumps(data), content_type='application/json')
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
# Create your views here.
