# coding=utf-8
import os
from conf.base_config import GetVariable as gv
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Devices:
    """获取连接的设备的信息"""
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        # self.GET_IOS = "instruments -s devices"

    def get_devices(self):
        value = os.popen(self.GET_ANDROID)

        devices = []
        for v in value.readlines():
            android = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                android['deviceName'] = s_value[:s_value.find('device')].strip()
                android['platformName'] = 'Android'
                android['platformVersion'] = gv.PLATFORM_VER
                android['app'] = PATH(gv.APP)
                # android['package'] = gv.PACKAGE
                # android['appActivity'] = gv.ACTIVITY
                # android["automationName"] = "uiautomator2"
                android["unicodeKeyboard"] = True
                android["resetKeyboard"] = True
                # android["noReset"] = True

                devices.append(android)
        return devices

    def start_android_devices(self):
        """启动安卓模拟器"""
        command = r'start C:\Program" "Files" "^(x86^)\Nox\bin\Nox.exe'
        os.system(command)
        # time.sleep(10)
        print('模拟器启动成功')
        adb = 'adb devices'
        os.system(adb)
        print('\n')

    def stop_android_devices(self):
        """结束安卓模拟器进程"""
        command = r'taskkill -f -im Nox.exe'
        os.system(command)
        print('所有任务执行完毕，关闭模拟器')
        print('\n')
