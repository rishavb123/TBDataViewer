from tb_data import TBData

if __name__ == '__main__':

    EXAMPLE = {
        "hostname": "http://boq.cc.gt.atl.ga.us",
        "port": 6006,
        "var_name": "total_episodes",
        "run": "minigrid",
        "format": "json"
    }

    tbdata = TBData(**EXAMPLE)
    tbdata.plot()