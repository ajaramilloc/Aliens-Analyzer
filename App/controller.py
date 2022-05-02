import config as cf
import model
import csv
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
csv.field_size_limit(2147483647)

# -----------------------------------------------------
# NEW CONTROLLER
# -----------------------------------------------------

def newController():
    analyzer = model.newAnalyzer()
    return analyzer

# -----------------------------------------------------
# LOADING DATA FUNCTIONS
# -----------------------------------------------------

def loadData(analyzer):
    ovnis_file = cf.data_dir + 'ovnis_limpio.csv'
    input_file = csv.DictReader(open(ovnis_file, encoding='utf-8'))
    for ovni in input_file:
        model.addOvni(analyzer, ovni)

# -----------------------------------------------------
# REQUIREMENTS FUNCTIONS
# -----------------------------------------------------

def requirement2(analyzer, date):
    return model.requirement2(analyzer, date)

def requirement3(analyzer, city):
    return model.requirement3(analyzer, city)

def requirement4(analyzer, duration):
    return model.requirement4(analyzer, duration)

def requirement5(analyzer, initial_date, final_date):
    return model.requirement5(analyzer, initial_date, final_date)