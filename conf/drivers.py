# coding=utf-8
from appium import webdriver

from conf.base_page import BasePage
from conf.devices import Devices
from conf.appium_server import *
from conf.login_status import LoginStatus
from conf.ports import Ports
from conf.log import Log
from conf.report_path import ReportPath
from conf.run_cases import RunCases


class Drivers:
    @staticmethod
    def _run_cases(server_url, run, cases):
        log = Log()
        log.set_logger(run.get_device()['deviceName'], run.get_path() + '\\' + 'client.log')

        log.i('platformName: %s', run.get_device()['platformName'])
        log.i('platformVersion: %s', run.get_device()['platformVersion'])
        log.i('deviceName: %s', run.get_device()['deviceName'])
        log.i('app: %s', run.get_device()['app'])
        # log.i('package: %s', run.get_device()['package'])
        # log.i('appActivity: %s', run.get_device()['appActivity'])
        # log.i('noReset: %s', run.get_device()['noReset'])
        log.i('appium server port: %d\n', run.get_port())

        addr = "http://%s:%s/wd/hub" % (server_url['hostname'], server_url['port'])
        remote = run.get_device()
        # init driver
        driver = webdriver.Remote(addr, remote)

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(driver)

        login_status = LoginStatus()
        login_status.set_status(False)

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        try:
            time.sleep(5)
            print('start cases')
            run.run(cases)
            print('end')
        except AssertionError as e:
            log.e('AssertionError, %s', e)

        # quit driver
        driver.quit()

    def run(self, cases):
        get_devices = Devices()
        # get_devices.start_android_devices()  # 启动模拟器
        # read all devices on this PC
        devices = get_devices.get_devices()

        # read free ports on this PC
        ports = Ports().get_ports(len(devices))

        if not len(devices):
            print('there is no device connected this PC')

        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i], ports[i]))

        # start Appium server
        appium_server = AppiumServer(runs)
        appium_server.start_appium_server()  # 启动appium服务

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(Drivers()._run_cases,
                             args=(appium_server.server_url(run.get_port()), run, cases,))

            # fix bug of Appium, android driver can not init in the same time
            time.sleep(2)

        pool.close()
        pool.join()

        # Devices().stop_android_devices()  # 关闭模拟器
        appium_server.stop_appium_server()  # 关闭appium服务
