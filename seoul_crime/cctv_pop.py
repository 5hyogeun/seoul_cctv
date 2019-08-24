import numpy as np
import pandas as pd
from seoul_crime.data_reader import DataReader

class CCTVModel:
    def __init__(self):
        self.dr = DataReader()

    def hook_process(self):
        print('--------------------1. CCTV 파일 DF 생성--------------------')    # DF: Data Frame => 메트릭스 구조
        self.get_cctv()

    def get_cctv(self):
        self.dr.context = './data/'
        self.dr.fname = 'cctv_in_seoul.csv'
        cctv = self.dr.csv_to_dframe()
        self.dr.fname = 'pop_in_seoul.xls'
        pop = self.dr.xls_to_dframe(2, 'B, D, G, J, N')

        print(cctv.columns)
        #print(cctv)