from tb_data import TBData

if __name__ == '__main__':

    '''
    1. Run the following command on BOQ:
        tensorboard --logdir ~/logdir --bind_all
    2. Connect to the VPN locally
    3. Run the script:
        python example.py
    '''

    EXAMPLE = {
        "hostname": "http://boq.cc.gt.atl.ga.us",
        "port": 6006,
        "var_name": "total_episodes",
        "run": "minigrid_expl",
        "format": "json"
    }

    tbdata = TBData(**EXAMPLE)
    tbdata.plot(False)

    EXAMPLE["run"] = "minigrid"
    EXAMPLE["format"] = "csv"

    tbdata2 = TBData(**EXAMPLE)
    tbdata2.plot(True)

    EXAMPLE_3 = {
        **EXAMPLE,
        "var_name": "dataset_size",
        "run": "lexa_temporal_walker",
    }

    tbdata3 = TBData(**EXAMPLE_3)
    tbdata3.plot(True)