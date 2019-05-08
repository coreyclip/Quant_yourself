import xlwings as xw
import pandas as pd
import seaborn as sns
import numpy as np


def hello_xlwings():
    wb = xw.Book.caller()
    # sheets can be called via an integer value 
    wb.sheets[0].range("A1").value = "Hello xlwings!"

def main(file):
    wb = xw.Book.caller()
    df = pd.read_csv(file)
    df = df.replace(np.int(0), np.nan)

    front_page = wb.sheets[0]
    front_page.range('A1:Z500').clear()

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

    # and they can be selected by name
    graphs_page = wb.sheets['Graphs']
    graphs_page.range('A1:Z300').clear()

    sns.set_style("darkgrid")
    steps = df['Steps (count)'].dropna()
    steps_fig = sns.distplot(steps).get_figure()

    graphs_page.pictures.add(steps_fig, name='step count distribution')






@xw.func
def hello(name):
    return "hello {0}".format(name)
