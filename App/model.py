from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
import time

def newAnalyzer():
    analyzer = {
        'ovnis_country': None,
        'ovnis_date': None,
        'ovnis_city': None,
        'ovnis_duration': None
    }

    analyzer['ovnis_country'] = mp.newMap(101, maptype='PROBING', loadfactor=0.5)
    analyzer['ovnis_date'] = om.newMap(omaptype='RBT', comparefunction = cmpDates)
    analyzer['ovnis_city'] = mp.newMap(101, maptype='PROBING', loadfactor=0.5)
    analyzer['ovnis_duration'] = om.newMap(omaptype='RBT', comparefunction = cmpTreeElements)

    return analyzer

def addOvni(analyzer, ovni):
    ovni['duration (seconds)'] = float(ovni['duration (seconds)'])
    ovni['datetime'] = ovni['datetime'].split(' ', 1)[0]
    addOvniMap(analyzer['ovnis_country'], ovni, 'country')
    addOvniTree(analyzer['ovnis_date'], ovni, 'datetime')
    addOvniMap(analyzer['ovnis_city'], ovni, 'city')
    addOvniTree(analyzer['ovnis_duration'], ovni, 'duration (seconds)')

# -----------------------------------------------------
# CMP FUNCTIONS    
# -----------------------------------------------------

def cmpTreeElements(element1, element2):
    if element1 == element2:
        return 0
    elif element1 > element2:
        return 1
    else:
        return -1

def cmpDates(date1, date2):
    sight1 = time.strptime(str(date1), "%Y-%m-%d")
    sight2 = time.strptime(str(date2), "%Y-%m-%d")

    if (sight1 == sight2):
        return 0
    elif (sight1 > sight2):
        return 1
    else:
        return -1
    
# -----------------------------------------------------
# ADD DATA FUNCTIONS (MAPS)     
# -----------------------------------------------------

def addOvniMap(map, ovni, property_name):
    property = ovni[f'{property_name}']
    exist_property = mp.contains(map, property)
    if exist_property:
        entry = mp.get(map, property)
        property_ovnis = me.getValue(entry)
    else:
        property_ovnis = newProperty(property)
        mp.put(map, property, property_ovnis)
    lt.addLast(property_ovnis['ovnis'], ovni)

# -----------------------------------------------------
# ADD DATA FUNCTION (TREES)
# -----------------------------------------------------

def addOvniTree(tree, ovni, property_name):
    property = ovni[f'{property_name}']
    exist_property = om.contains(tree, property)
    if exist_property:
        entry = om.get(tree, property)
        property_ovnis = me.getValue(entry)
    else:
        property_ovnis = newProperty(property)
        om.put(tree, property, property_ovnis)
    lt.addLast(property_ovnis['ovnis'], ovni)

# -----------------------------------------------------
# CREATE DATA FUNCTIONS
# -----------------------------------------------------

def newProperty(property):
    entry = {f'{property}': '', 'ovnis': None}
    entry[f'{property}'] = property
    entry['ovnis'] = lt.newList('ARRAY_LIST')
    return entry

# -----------------------------------------------------
# REQUIREMENTS FUNCTIONS
# -----------------------------------------------------

def requirement2(analyzer, date):
    ovnis_date = getOvnisTree(analyzer['ovnis_date'], date)
    return ovnis_date

def requirement3(analyzer, city):
    ovnis_city = getOvnisMap(analyzer['ovnis_city'], city)
    return ovnis_city

def requirement4(analyzer, duration):
    max_duration = om.maxKey(analyzer['ovnis_duration'])
    interval = getIntervalOvnis(analyzer['ovnis_duration'], duration, max_duration)
    return interval

def requirement5(analyzer, initial_date, final_date):
    ovnis_period_time = getIntervalOvnis(analyzer['ovnis_date'], initial_date, final_date)
    return ovnis_period_time

# -----------------------------------------------------
# GET DATA FUNCTIONS
# -----------------------------------------------------

def getOvnisMap(map, property):
    if mp.contains(map, property):
        property_ovnis = mp.get(map, property)
        if property_ovnis:
            return me.getValue(property_ovnis)['ovnis']
    else:
        return None

def getOvnisTree(tree, property):
    if om.contains(tree, property):
        property_ovnis = om.get(tree, property)
        if property_ovnis:
            return me.getValue(property_ovnis)['ovnis']
    else:
        return None

def getIntervalOvnis(tree, initial_interval, final_interval):
    try:
        interval_ovnis = om.values(tree, initial_interval, final_interval)
        return interval_ovnis
    except Exception:
        return None