import numpy as np


def generate():
    
    max_customers = 100

                       #0 1 2 3 4 5 6 7 8 9  10  11  12  13    14  15 16  17   18  19  20  21 22   23
    weekEnd = np.array([0,0,0,0,0,0,0,0,0,0,0.1,0.4,0.6, 0.8, 0.9, 0.9, 0.8, 0.9, 1,1,0.7,0.4, 0.1, 0])
    friDay = np.array([0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.2, 0.3, 0.5, 0.6, 0.35, 0.3, 1,1,0.7,0.6, 0.5, 0])
    weekDay = np.array([0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.2, 0.3, 0.5, 0.6, 0.35, 0.3, 0.6,0.6,0.6,0.6, 0.4, 0])

    data_set = []
    for week in range(0,12):
        for days in range(0,4):

            for day in range(0,4):
                temp = weekDay * max_customers + np.array([np.random.uniform(-10,10) if i != 0 else 0 for i in weekDay])
                data_set += [[e, day] for e in temp]

            temp = friDay * max_customers + np.array([np.random.uniform(-10,10) if i != 0 else 0 for i in friDay])        
            data_set += [[e, 4] for e in temp]


            for day in range(5,7):
                temp = weekEnd * max_customers + np.array([np.random.uniform(-10,10) if i != 0 else 0 for i in weekEnd])
                data_set += [[e, day] for e in temp]


    coeff = max([d[0] for d in data_set])
    data_set = [[d[0] / coeff, d[1] / 7] for d in data_set]


    weekTest = []
    for day in range(0,4):
        temp = weekDay * max_customers + np.array([np.random.uniform(-15,15) if i != 0 else 0 for i in weekDay])
        weekTest += [[e, day] for e in temp]

    temp = friDay * max_customers + np.array([np.random.uniform(-15,15) if i != 0 else 0 for i in friDay])        
    weekTest += [[e, 4] for e in temp]


    for day in range(5,7):
        temp = weekEnd * max_customers + np.array([np.random.uniform(-15,15) if i != 0 else 0 for i in weekEnd])
        weekTest += [[e, day] for e in temp]

    coeff = max([d[0] for d in weekTest])
    weekTest = [[d[0] / coeff, d[1] / 7] for d in weekTest]
    
    return data_set, weekTest