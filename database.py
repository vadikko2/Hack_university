
# coding: utf-8

# # Класс для работы с базой, находящихся в конкретной области людей

# In[2]:


import pickle as pkl
import json as js
import os
import numpy as np
from scipy.spatial import distance


#  - при инициализации подать имя файла с буфером (у каждого сектора свой файл с буфером)
#  - при вызове объекта подать json с информацией о пользователе и флаг (True - вход, False - выход)

# In[6]:


class DataBase:
    def __init__(self, buffer_file):
        self.buf = buffer_file
        if not os.path.exists(self.buf):
            self.dump([])
    def __call__(self, person_info, action):
        if action:
            self._input(person_info)
        else:
            self._output(person_info)
    def dump(self, data):
        with open(self.buf, 'w') as f:
            f.write(js.dumps(data, indent = 4))
    def load(self):
        return js.load(open(self.buf))
    def _input(self, person_info):
        inarea = self.load()
        check, index = self.__inarea__(inarea, {'vector':self.__arrayToStr__(person_info['vector'])})
        if not check:
            inarea.append({'vector':self.__arrayToStr__(person_info['vector']), 'gender':[person_info['gender'],], 'age':[person_info['age'],], 'frame':[person_info['frame'],]})
            self.dump(inarea)
            return False, None
        else:
            inarea[index]['gender'].append(person_info['gender'])
            inarea[index]['age'].append(person_info['age'])
            inarea[index]['frame'].append(person_info['frame'])
            self.dump(inarea)
            return True, index

        self.dump(inarea)
    def _output(self, person_info):
        inarea = self.load()
        check = self.__inarea__(inarea, person_info)
        if check[0]:
            inarea.remove(inarea[check[1]])
        self.dump(inarea)

    def __inarea__(self, inarea, target_person):
        vectors = [self.__strToArray__(p['vector']) for p in inarea]
        dists = []
        for v in vectors:
            dists.append(distance.euclidean(v, self.__strToArray__(target_person['vector'])))
        if len(dists) > 0:
            dists = np.asarray(dists)
            if np.min(dists) < 0.55:
                return (True, np.argmin(dists))
            else:
                return (False, None)
        else:
            return (False, None)
        
    def __strToArray__(self, string):
        return np.asarray([float(v) for v in string.split(';')])
    
    def fictionvectors(self):
        fict_vs = []
        for i in range(10):
            fict_vs.append({'vector':self.__arrayToStr__(np.random.random(24))})
        with open(self.buf, 'w') as f:
            f.write(js.dumps(fict_vs))
            
    def __arrayToStr__(self, array):
        array_strs = [str(v) for v in array]
        return ';'.join(array_strs)

    @staticmethod
    def chunk(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out

    def getstatistic(self, num_frames, len_statisticts):
        inarea = self.load()
        male = {
            'C':[0 for i in range(num_frames)],
            'Y':[0 for i in range(num_frames)],
            'A':[0 for i in range(num_frames)],
            'O':[0 for i in range(num_frames)],
            'total':[],
            'percentage': 0,
            'nframe': 0
        }
        female = {
            'C':[0 for i in range(num_frames)],
            'Y':[0 for i in range(num_frames)],
            'A':[0 for i in range(num_frames)],
            'O':[0 for i in range(num_frames)], 
            'total':[],
            'percentage': 0
        }
        for person in inarea:
            age = self.most_common(person['age'])
            gender = 'F' if 'F' in person['gender'] else 'M'
            nframe = int(sum(person['frame'])/len(person['frame']))
            if gender == 'F':
                female[age][nframe]+=1
            else:
                male[age][nframe]+=1

        for key in ['C', 'Y', 'A', 'O']:
            male[key] = self.chunk(male[key], int(num_frames / len_statisticts))
            female[key] = self.chunk(female[key], int(num_frames / len_statisticts))

            for i in range(len(male[key])):
                male[key][i] = sum(male[key][i])

            for i in range(len(female[key])):
                female[key][i] = sum(female[key][i])

        male['total'] = [male['C'][i] + male['Y'][i] + male['A'][i] + male['O'][i] for i in range(len(male['C']))]
        female['total'] = [female['C'][i] + female['Y'][i] + female['A'][i] + female['O'][i] for i in range(len(female['C']))]
        
        maleSum = sum(male['total'])
        femaleSum = sum(female['total'])


        male['percentage'] = maleSum * 100 / (maleSum + femaleSum)
        female['percentage'] = femaleSum * 100 / (maleSum + femaleSum)
        male['nframe'] = int(num_frames / len_statisticts)

        with open('male.json', 'w') as f:
            f.write(js.dumps(male, indent = 4))
        with open('female.json', 'w') as f:
            f.write(js.dumps(female, indent = 4))
        return male, female
    
    def most_common(self, lst):
        return max(set(lst), key=lst.count)

# пример использования класса DataBase

# In[8]:


#db = DataBase("inarea.json")
#заполняем базу фиктивными векторами
#db.fictionvectors()
#ищем в базе случайно сгенерированный вектор
#db({'vector':db.__arrayToStr__(np.random.random(24))}, False)

