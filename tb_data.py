import csv
import json
import sys

import matplotlib.pyplot as plt
import numpy as np
import requests

from utils import var_to_title


class TBData:

    def __init__(self, hostname, port, var_name, run, format="json") -> None:
        self._hostname = hostname
        self._port = port
        self._var_name = var_name
        self._run = run
        self._format = format
        self._url = self.create_url()
        self._data = None

    def create_url(self):
        return f"{self._hostname}:{self._port}/data/plugin/scalars/scalars?tag=scalars/{self._var_name}&run={self._run}&format={self._format}"

    def get_data(self):
        if self._data is None:
            try:
                r = requests.get(self._url, allow_redirects=True)
            except:
                print(f"Make sure tensorboard is running on the {self._hostname}:{self._port}, you are connected to the VPN, and the rest of the parameters are correct.")
                print("To run tensorboard use the following command:")
                print("\ttensorboard --logdir {LOGDIR} --bind_all")
                sys.exit(1)
            data_bytes = r.content
            if self._format == "json":
                self._data = np.array(json.loads(data_bytes))
            elif self._format == "csv":
                data_str = data_bytes.decode(r.encoding)
                self._data = list(csv.reader(data_str.split("\r\n")))[1:-1]
                self._data = np.array([[float(el) for el in d] for d in self._data])
            else:
                self._data = str(data_str, "utf-8")
        return self._data
        
    def plot(self, show=True):
        self.get_data()
        steps = self._data[:, 1]
        values = self._data[:, 2]

        plt.xlabel("steps")
        plt.ylabel(self._var_name)
        title_var_name = var_to_title(self._var_name)
        plt.title(f"{title_var_name} vs Steps")

        plt.plot(steps, values, label=f"{var_to_title(self._run)} {title_var_name}")
        plt.legend()
        if show:
            plt.show()

    def get_hostname(self):
        return self._hostname

    def set_hostname(self, hostname):
        self._hostname = hostname
        self._url = self.create_url()

    def get_port(self):
        return self._port

    def set_port(self, port):
        self._port = port
        self._url = self.create_url()

    def get_var_name(self):
        return self._var_name

    def set_var_name(self, var_name):
        self._var_name = var_name
        self._url = self.create_url()

    def get_run(self):
        return self._run

    def set_run(self, run):
        self._run = run
        self._url = self.create_url()

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format
        self._url = self.create_url()

    def get_url(self):
        return self._url
