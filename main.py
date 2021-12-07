from RPA.Browser.Selenium import Selenium
import re
from RPA.Excel.Application import Application
from RPA.Excel import Files
import os
import RPA.Excel
from RPA.FileSystem import FileSystem


webbrowser = Selenium()


def open_the_website(url):
    webbrowser.open_chrome_browser(url)


def click_buton():
    webbrowser.press_keys('xpath://*[@id="node-23"]/div/div/div/div/div/div/div/a','DIVE IN')
    list_agency = webbrowser.get_text('xpath://*[@id="agency-tiles-widget"]')
    tuple_agency = re.findall("(\w{1,}.\w{1,}.\w{1,}|\w{1,}.\w{1,}.\w{1,}.\w{1,}.\w{1,}.\w{1,}|\w.\w..\w{1,}.\w{1,}.\w{1,}.\w{1,})\s+(\w{1,}.\w{1,}.\w{1,}):\s+(.\d{1,}.\d\w|.\d{1,}\w)\s+(\w{1,4})",list_agency)
    return tuple_agency


def create_workbook():
    create_workbook(path=None, fmt='xlsx')




def read_excel_worksheet(path, worksheet):
    create_workbook(path='C:/Users/User/PycharmProjects/itdashboard/agencies', fmt='xlsx')

    lib = Files()

    lib.open_workbook(path)
    try:
        return lib.read_worksheet(worksheet)
    finally:
        lib.close_workbook()

def amounts():

    # create_workbook(path='itdashboard/', fmt='agencies.xlsx')

    app = Application()

    app.open_application()


    app.open_workbook('agencies.xlsx')
    # app.set_active_worksheet(sheetname='agencies')
    # app.write_to_cells(row=1, column=1, value='new data')
    app.save_excel()
    app.quit_application()

    # i_t = [i for i in click_buton()]
    # print(i_t)
    # t_c =[]
    for i in click_buton():
        print(i)



def read_excel_worksheet(path, worksheet):
    lib = Files()
    lib.open_workbook(path)
    try:
        return lib.read_worksheet(worksheet)
    finally:
        lib.close_workbook()




def search_for(term):
    pass



def store_screenshot(filename):
    pass
    # browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    open_the_website(url="https://itdashboard.gov/")
    click_buton()
    amounts()


    # try:
    #     open_the_website(url="https://itdashboard.gov/")
    #     click_buton()
    #
    #     print('ok')

        # store_screenshot("output/screenshot.png")
    # finally:
    #     # webbrowser.close_browser()
    #     print('close')





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

