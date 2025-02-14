import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: add_0
    api简介: 逐元素相加算子
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, y, ):
        """
        forward
        """
        out = paddle.add(x, y,  )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-10 + (10 - -10) * np.random.random([2, 3, 4, 4]).astype('float64'), dtype='float64', stop_gradient=False), paddle.to_tensor(-10 + (10 - -10) * np.random.random([2, 3, 4, 4]).astype('float64'), dtype='float64', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-10 + (10 - -10) * np.random.random([2, 3, 4, 4]).astype('float64'), -10 + (10 - -10) * np.random.random([2, 3, 4, 4]).astype('float64'), )
    return inputs

