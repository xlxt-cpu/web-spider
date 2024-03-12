from selenium import webdriver
from lxml import etree

chrome = webdriver.Chrome()
chrome.get("https://www.huya.com/g/lol")
chrome.implicitly_wait(10)

i = 1
while True:
    e = etree.HTML(chrome.page_source)
    # rooms = chrome.find_elements_by_class_name('title')
    # names = chrome.find_elements_by_class_name('nick')
    # counts = chrome.find_elements_by_class_name('js-num')
    rooms = e.xpath('//a[@class="title"]/text()')
    names = e.xpath('//i[@class="nick"]/text()')
    counts = e.xpath('//i[@class="js-num"]/text()')
    print("---------第%d页数据---------" % i)
    # for r, n, c in zip(rooms, names, counts):
    #     print(f'{r} : {n} : {c}')
    print(len(rooms))
    print(len(names))
    print(len(counts))
    i += 1
    try:
        has_next = chrome.page_source.find('laypage_next')
        if has_next != -1:
            chrome.find_element_by_class_name('laypage_next').click()
        else:
            break
    except:
        chrome.switch_to.frame('UDBSdkLgn_iframe')
        chrome.find_element_by_class_name('close-layer').click()
        chrome.switch_to.parent_frame()
        print("出现异常")

chrome.quit()
