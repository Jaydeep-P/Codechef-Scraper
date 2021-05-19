import worker as work
import os
import pandas as pd

contest_link = str(input("Enter link of the contest: "))
contest_name = contest_link.split(sep='/')[-1]
contest_name = contest_name.split(sep='?')[0]
cwd = os.getcwd()
new_path = os.path.join(cwd, contest_name)

pathtosubscsv = os.path.join(new_path, contest_name + '-subs.csv')
pathtoacccsv = os.path.join(new_path, contest_name + '-acc.csv')

# noinspection PyBroadException
try:
    os.mkdir(new_path)
    listofproblems = list(['time'] + work.returnNames(contest_link))
    temp = pd.DataFrame(columns=listofproblems)
    temp.to_csv(os.path.join(new_path, contest_name + '-subs.csv'))
    temp.to_csv(os.path.join(new_path, contest_name + '-acc.csv'))
    pathtosubscsv = os.path.join(new_path, contest_name + '-subs.csv')
    pathtoacccsv = os.path.join(new_path, contest_name + '-acc.csv')
    print("New Directory", new_path, "made.")
except:
    print("Directory present.")

print("Adding lines to the csvs every five minutes, close this window to exit.")

work.workerfunction(contest_link, pathtosubscsv, pathtoacccsv)
