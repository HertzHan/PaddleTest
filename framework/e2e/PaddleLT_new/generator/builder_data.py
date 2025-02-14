#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
data builder
"""

import os
import numpy as np

if os.environ.get("FRAMEWORK") == "paddle":
    import paddle
    import diy
    import layerApicase
    import layercase
elif os.environ.get("FRAMEWORK") == "torch":
    import torch
    import layerTorchcase

import tools.np_tool as tool


class BuildData(object):
    """BuildData"""

    def __init__(self, layerfile):
        """init"""
        self.dataname = layerfile

    def get_single_data(self):
        """get data"""
        dataname = self.dataname + ".create_numpy_inputs()"
        data = []
        for i in eval(dataname):
            if os.environ.get("FRAMEWORK") == "paddle":
                data.append(paddle.to_tensor(i, stop_gradient=False))
            elif os.environ.get("FRAMEWORK") == "torch":
                data.append(torch.tensor(i, requires_grad=True))

        return data

    def get_single_tensor(self):
        """get data"""
        dataname = self.dataname + ".create_tensor_inputs()"
        data = []
        for i in eval(dataname):
            data.append(i)

        return data

    def get_single_numpy(self):
        """get data"""
        dataname = self.dataname + ".create_numpy_inputs()"
        data = []
        for i in eval(dataname):
            data.append(i)

        return data

    # def get_single_inputspec(self):
    #     """get single inputspec"""
    #     spec_list = []
    #     for k, v in self.data.items():
    #         if v["type"] == "Tensor":
    #             spec_tmp = paddle.static.InputSpec(shape=v["shape"], dtype=v["dtype"], name=k)
    #             spec_list.append(spec_tmp)
    #     return spec_list
