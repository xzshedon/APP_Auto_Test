# encoding: utf-8

''' 对APIUM进行简单的封装 '''


class DriverBase():

    def __init__(self, driver):
        self.driver = driver

    def find_elem(self, attr, tag):
        '''
        封装appium控件查找方法，简化脚本
        :param attr: 控件属性
        :param tag: 查找内容（id,xpath,css,name...）
        :return: element
        '''
        if attr == 'id':
            ele = self.driver.find_element_by_id(tag)
        elif attr == 'xpath':
            ele = self.driver.find_element_by_xpath(tag)
        elif attr == 'css':
            ele = self.driver.find_element_by_css_selector(tag)
        elif attr == 'class':
            ele = self.driver.find_element_by_class_name(tag)
        elif attr == 'name':
            ele = self.driver.find_element_by_name(tag)
        elif attr == 'acces_id':
            ele = self.driver.find_element_by_accessibility_id(tag)
        elif attr == 'link_text':
            ele = self.driver.find_element_by_link_text(tag)
        elif attr == 'partial_link_text':
            ele = self.driver.find_element_by_partial_link_text(tag)
        elif attr == 'tag_name':
            ele = self.driver.find_element_by_tag_name(tag)
        elif attr == 'uiautomator':
            ele = self.driver.find_element_by_android_uiautomator('new Uiselector().%s' % tag)
        else:
            raise NameError('No element,please send exist tag,xpath,text,id,css,id...')
        return ele

    def find_elements(self, attr, tag):
        try:
            if attr == 'id':
                ele = self.driver.find_elements_by_id(tag)
            elif attr == 'xpath':
                ele = self.driver.find_elements_by_xpath(tag)
            elif attr == 'css':
                ele = self.driver.find_elements_by_css_selector(tag)
            elif attr == 'class':
                ele = self.driver.find_elements_by_class_name(tag)
            elif attr == 'name':
                ele = self.driver.find_elements_by_name(tag)
            elif attr == 'acces_id':
                ele = self.driver.find_elements_by_accessibility_id(tag)
            elif attr == 'link_text':
                ele = self.driver.find_elements_by_link_text(tag)
            elif attr == 'partial_link_text':
                ele = self.driver.find_elements_by_partial_link_text(tag)
            elif attr == 'tag_name':
                ele = self.driver.find_elements_by_tag_name(tag)
            elif attr == 'uiautomator':
                ele = self.driver.find_elements_by_android_uiautomator('new Uiselector().%s' % tag)
            else:
                raise NameError('No element,please send exist tag,xpath,text,id,css,id...')
            return ele
        except Exception as e:
            return e

    def install_app(self, path):
        self.driver.install_app(path)

    def remove_app(self, package_name):
        self.driver.remove_app(package_name)

    def remove_ios_app(self, bundleId):
        self.driver.remove_app(bundleId)

    def close(self):
        self.driver.close_app()

    def reset(self):
        self.driver.reset()

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def send_keyevent(self,event):
        self.driver.keyevent(event)

    def press_keycode(self, keycode):
        self.driver.press_keycode(keycode=keycode)

    def long_press_keycode(self, keycode):
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        return self.driver.current_activity()

    def wait_activity(self, activity, times, interval=1):
        self.driver.wait_activity(activity, time=times, interval=1)

    def run_back(self, second):
        self.driver.background_app(second=second)

    def is_app_installed(self, package_name):
        self.driver.is_app_installed(package_name)

    def launch_app(self):
        self.driver.launch_app()

    def start_activity(self, package, activity):
        self.driver.start_activity(package, activity)

    def ios_lock(self, locktime):
        self.driver.lock(locktime)

    def shake(self):
        self.driver.shake()

    def open_notifications(self):
        self.driver.open_notifications()

    def network_state(self):
        return self.driver.network_connection

    def set_network_type(self, type):
        from appium.webdriver.connectiontype import ConnectionType
        if type=='wifi' or type=='WIFI' or type=='w' or type=='WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif type=='data' or type=='DATA' or type=='d' or type=='DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif type=='all' or type=='ALL' or type=='a' or type=='ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif type=='no' or type=='NO' or type=='n' or type=='NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif type=='air' or type=='fly' or type=='at' or type=='AIRPLANE_MODE':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        else:
            raise NameError('please set wifi,data,all,no,fly')

    def avail_input(self):
        return self.driver.available_ime_engines

    def is_input_active(self):
        return self.driver.is_ime_active

    def active_input(self, engine):
        self.driver.activate_ime_engine(engine)

    def close_input(self):
        self.driver.deactivate_ime_engine()

    def input_name(self):
        return self.driver.activate_ime_engine

    def open_gps(self):
        self.driver.toggle_location_services()

    def set_location(self,latitude,longitude,altitude):
        self.driver.set_location(latitude,longitude,altitude)

    def get_size(self):
        return self.driver.se.size

    def text(self):
        return self.driver.text

    def is_displayed(self):
        return self.driver.se.is_displayed()

    def screenshot(self, filename):
        self.driver.get_screenshot_as_base64(filename)

    def is_screenshot(self):
        return self.driver.get_screenshot_as_file()

    def close(self):
        self.driver.close()

    def kill(self):
        self.driver.quit()

    def get_window_size(self):
        return self.driver.get_window_size()

    def zoom_in(self,element):  # 放大
        self.driver.zoom(element)

    def zoom_out(self,element):  # 缩小
        self.driver.pinch(element)

    def flick(self, start_x, start_y, end_x, end_y):  # 快速滑动
        self.driver.flick(start_x, start_y, end_x, end_y)

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def tap(self, x, y, duration=200):
        self.driver.tap([(x, y), duration])

    def scroll(self, x, y):  # 滚动元素
        self.driver.scroll(x, y)

    def drag_and_drop(self, e1, e2):
        self.driver.drag_and_drop(e1, e2)

    def context(self):
        self.driver.contexts()

    def push(self, file, path):
        self.driver.push_file(file, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def wait(self, second):
        self.driver.wait_activity(second)

    def send_key(self, text):
        self.driver.send_keys(text)





