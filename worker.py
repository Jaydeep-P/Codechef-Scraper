from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import pandas as pd
from sys import stdout


#inp = link to contest
Timeout = 300



def workerfunction(inp, pathtosubscsv, pathtoacccsv):
    url = inp
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])


    while True:

        driver = webdriver.Chrome('chromedriver.exe', options=options)
        driver.get(url)
        time.sleep(3) #making sure to load
        
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%d %H:%M:%S")

        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')

        table = soup.find_all('td', class_ = 'num')

        driver.quit()


        def submissionsextractor(string):
            open = 0
            ans = ""
            for ch in string:
                if ch =='<':
                    open+=1
                if open == 0:
                    ans = ans + ch
                if ch =='>':
                    open-=1

            return int(ans)

        def accextractor(string):
            open = 0
            ans = ""
            for ch in string:
                if ch =='<':
                    open+=1
                if open == 0:
                    ans = ans + ch
                if ch =='>':
                    open-=1

            return float(ans)

        def nameextractor(string):
            ind = string.find("status/")
            ans = ""
            if ind==-1:
                print("wtf")
                return "wtf?"
            else:
                ind+=7
                while string[ind] != '"':
                    ans = ans+string[ind]
                    ind+=1
                return ans



        subsoracc =1
        subs_df = pd.read_csv(filepath_or_buffer=pathtosubscsv,index_col=0)
        subs_dic = {}
        subs_dic['time'] = current_time
        acc_df = pd.read_csv(filepath_or_buffer=pathtoacccsv,index_col=0)
        acc_dic = {}
        acc_dic['time'] = current_time

        for row in table:
            if subsoracc ==1:
                currsubs = submissionsextractor(str(row))
                subsoracc =0
            else:
                currprob = nameextractor(str(row))
                curracc = accextractor(str(row))
                subsoracc = 1
                subs_dic[currprob] = currsubs
                acc_dic[currprob] = curracc

        new_subs_df = pd.DataFrame.from_records([subs_dic])
        new_acc_df = pd.DataFrame.from_records([acc_dic])

        subs_df = subs_df.append(new_subs_df,ignore_index=True)
        subs_df.to_csv(path_or_buf=pathtosubscsv)
        acc_df = acc_df.append(new_acc_df,ignore_index=True)
        acc_df.to_csv(path_or_buf=pathtoacccsv)

        updatestr = "Last update made on "+ current_time 
        stdout.write("\r%s" %updatestr)
        stdout.flush()
        time.sleep(Timeout)
        
        
    

def returnNames(inp):

    url = inp
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(url)

    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('td', class_='num')

    driver.quit()


    def nameextractor(string):
        ind = string.find("status/")
        ans = ""
        if ind == -1:
            print("wtf")
            return "wtf?"
        else:
            ind += 7
            while string[ind] != '"':
                ans = ans + string[ind]
                ind += 1
            return ans


    subsoracc = 1

    anslist =[]

    for row in table:
        if subsoracc == 1:
            subsoracc = 0
        else:
            currprob = nameextractor(str(row))
            subsoracc = 1
            anslist.append(currprob)
    return anslist