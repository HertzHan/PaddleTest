import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: masked_select_base
    api简介: 返回一个1-D 的Tensor, Tensor的值是根据 mask 对输入 x 进行选择的
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, mask, ):
        """
        forward
        """
        out = paddle.masked_select(x, mask,  )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([2, 3, 4, 4]).astype('float32'), dtype='float32', stop_gradient=False), paddle.to_tensor(np.random.randint(0, 2, [2, 3, 4, 4]).astype('bool'), dtype='bool', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([2, 3, 4, 4]).astype('float32'), np.random.randint(0, 2, [2, 3, 4, 4]).astype('bool'), )
    return inputs

