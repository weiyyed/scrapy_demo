"""
@author:weiyongyou
@date:2019/12/15:23:34
"""
TARGET_URL = 'https://www.zhipin.com/web/common/security-js/' #这个是文件的
INJECT_TEXT = 'Object.defineProperties(navigator,{webdriver:{get:() => false}});' #js执行文件

def response(flow):
    # if flow.request.url.startswith(TARGET_URL):
    #     flow.response.text = INJECT_TEXT + flow.response.text
    #     print('注入成功')
    if 'security-js' in flow.request.url or 'ka.js' in flow.request.url:
        # 屏蔽selenium检测
        # flow.response.text = flow.response.text + INJECT_TEXT
        # 屏蔽selenium检测
        for webdriver_key in ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate',
                              '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped',
                              '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium',
                              'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw', 'driver-evaluate',
                              'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand',
                              'webdriver-evaluate-response', '__webdriverFunc', '__webdriver_script_fn',
                              '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm',
                              '__lastWatirPrompt', '$chrome_asyncScriptInfo', '$cdc_asdjflasutopfhvcZLmcfl_']:
            ctx.log.info('Remove "{}" from {}.'.format(webdriver_key, flow.request.url))
            flow.response.text = flow.response.text.replace('"{}"'.format(webdriver_key), '"NO-SUCH-ATTR"')
        flow.response.text = flow.response.text.replace('t.webdriver', 'false')
        flow.response.text = flow.response.text.replace('ChromeDriver', '')