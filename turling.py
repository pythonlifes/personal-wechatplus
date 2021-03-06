'''图灵机器人'''


#coding=utf8
import requests
'''
图灵机器人接口
函数的参数：  微信聊天的时候输入的内容
函数的返回值：图灵机器人的回应
'''
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
def baidu(info):
    page = requests.get('https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word={}'.format(info),headers=headers)
    if page.ok:
        page.encoding = 'gbk'
        from lxml import etree
        tree = etree.HTML(page.text)
        answer = ''.join(tree.xpath('//*[@id="wgt-list"]/dl[1]/dd[1]//text()'))
        if '答：' not in answer:
            answer = ''.join(tree.xpath('//*[@id="wgt-list"]/dl[1]/dd[2]//text()'))
        return answer[2:]


def jqr(info):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : 'ad0c5d0594ce42f1b5c7a8547eb947e4','info'   : info,'userid' : '陈小奇',#
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    # 让我们打印一下返回的值，看一下我们拿到了什么
    print(r)
    try:
        result = r['text']+r['url']
    except KeyError:
        result = r['text']
    try:
        ls = r['list']
        for i in ls[:5]:
            result+=i['article']
            result+='\n'
            result+=i['detailurl']
            result+='\n'
    except KeyError:
        pass
    return result
# print(jqr('qinaide'))
