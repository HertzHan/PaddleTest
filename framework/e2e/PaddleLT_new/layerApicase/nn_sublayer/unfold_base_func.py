import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: unfold_base
    api简介: 通被称作为im2col过程. 对于每一个输入形状为[N, C, H, W]的 x ，都将计算出一个形状为[N, Cout, Lout]的输出
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, ):
        """
        forward
        """
        out = paddle.nn.functional.unfold(x,  kernel_sizes=[3, 3], strides=1, paddings=0, dilations=1, )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([5, 3, 8, 8]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([5, 3, 8, 8]).astype('float32'), )
    return inputs

