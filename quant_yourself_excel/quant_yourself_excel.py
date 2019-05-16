import xlwings as xw
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime as dt


def hello_xlwings():
    wb = xw.Book.caller()
    # sheets can be called via an integer value 
    wb.sheets[0].range("A1").value = "Hello xlwings!"

def main(file):
    # if you have issues
    wb = xw.Book('quant_yourself_excel.xlsm')
    # necssary for date filtering
    df = pd.read_csv(file, parse_dates=['Start'])
    df = df.replace(np.int(0), np.nan)
    front_page = wb.sheets[0]
  
    # try:
    # make sure python reads the excel page values as int for datetime
    upper_date = dt(day=int(front_page.range('E4').value),
                    month=int(front_page.range('F4').value), 
                    year=int(front_page.range('G4').value))
    # except:
    #     upper_date = False
    try:
        lower_date = dt(day=int(front_page.range('E5').value),
                        month=int(front_page.range('F5').value),
                        year=int(front_page.range('G5').value))
    except:
        lower_date = False

    if upper_date:
        front_page.range('C7').value = f"upper bound date: {upper_date.strftime('%m/%d/%Y')}"
        df = df[df['Start'] <= upper_date]
    if lower_date:
        front_page.range('C8').value = f"upper bound date: {lower_date.strftime('%m/%d/%Y')}"
        df = df[df['Start'] >= lower_date]
    
    front_page.range('A8').value = "Statistics"
    front_page.range('A10').value = df.describe().T

    front_page.range('A22').value = 'Correlation Table'
    front_page.range('A23').value = df.corr()
    for col in ['C', 'D', 'E', 'F', 'G', 'H']:
        for i in range(24,31):
            try:
                if float(front_page.range(f"{col}{i}").value) > 0:
                    front_page.range(f"{col}{i}").color = (66, 244, 80)
                else:
                    front_page.range(f"{col}{i}").color = (255, 153, 153)
            except:
                pass

    # auto fit columns
    front_page.autofit('c')
    # and they can be selected by name
    graphs_page = wb.sheets['Graphs']
    graphs_page.range('A1:Z300').clear()

    sns.set_style("darkgrid")
    steps = df['Steps (count)'].dropna()
    steps_fig = sns.distplot(steps).get_figure()
    # since version 0.5
    xw.Plot(steps_fig).show('step counts', sheet='graphs_page')
    # steps_fig.savefig('step count distribution')
    # try:
    #     graphs_page.pictures.add(steps_fig, name='step count distribution')
    # except:
    #     # if the graph already exists use this syntax
    #     graphs_page.pictures.add(steps_fig, update='step count distribution')






@xw.func
def hello(name):
    return "hello {0}".format(name)
