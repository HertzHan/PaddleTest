import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: bernoulli_base
    api简介: 该OP以输入 x 为概率，生成一个伯努利分布（0-1分布）的Tensor
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, ):
        """
        forward
        """
        out = paddle.bernoulli(x,  )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(0 + (1 - 0) * np.random.random([2, 3, 4, 4]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (0 + (1 - 0) * np.random.random([2, 3, 4, 4]).astype('float32'), )
    return inputs

