import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: add_1
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
    inputs = (paddle.to_tensor(np.random.randint(-10, 10, [2, 3, 4, 4]).astype('int32'), dtype='int32', stop_gradient=False), paddle.to_tensor(np.random.randint(-10, 10, [2, 3, 4, 4]).astype('int32'), dtype='int32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (np.random.randint(-10, 10, [2, 3, 4, 4]).astype('int32'), np.random.randint(-10, 10, [2, 3, 4, 4]).astype('int32'), )
    return inputs

