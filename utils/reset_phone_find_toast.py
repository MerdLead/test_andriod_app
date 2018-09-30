import urllib3
# from pprint import pprint
from conf.decorator import teststeps


@teststeps
def verify_find(phone, var='editPhone'):
    http = urllib3.PoolManager()
    r = http\
        .request('GET', "http://dev.apirebuild.manage.vanthink.cn/api/utils/get/userCaptcha?user=13511111111&pw=123123&phone=%s&project_type=core&action_type=%s" % (phone, var))
    value = r._body.decode('utf-8')
    print(value)
    return value
