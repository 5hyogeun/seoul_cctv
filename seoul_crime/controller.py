from seoul_crime.cctv_pop import CCTVModel

class Controller:
    def __init__(self):
        self._cctv = CCTVModel()

    def excute(self):
        cctv = self._cctv
        cctv.hook_process()
