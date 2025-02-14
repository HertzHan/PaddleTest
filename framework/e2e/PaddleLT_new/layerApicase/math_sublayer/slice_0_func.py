import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: slice_0
    api简介: 沿多个轴生成 input 的切片
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, input, ):
        """
        forward
        """
        out = paddle.slice(input,  axes=[0], starts=[1], ends=[3], )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([6]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([6]).astype('float32'), )
    return inputs

