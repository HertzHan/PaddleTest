# method:cast||method:__add__||method:cast||method:__sub__||method:cast||method:__sub__||api:paddle.nn.functional.loss.cross_entropy||method:__mul__||api:paddle.nn.functional.loss.cross_entropy||method:__mul__||method:__add__||method:__rmul__||method:__mul__||method:sum||method:__truediv__
import paddle
import unittest
import numpy as np


class LayerCase(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
    def forward(
        self,
        var_0,    # (shape: [24, 8], dtype: paddle.float32, stop_gradient: False)
        var_1,    # (shape: [24], dtype: paddle.float32, stop_gradient: True)
        var_2,    # (shape: [24], dtype: paddle.float32, stop_gradient: True)
    ):
        var_3 = var_1.cast('int64')
        var_4 = var_3.__add__(1)
        var_5 = var_4.cast('float32')
        var_6 = var_5.__sub__(var_1)
        var_7 = var_3.cast('float32')
        var_8 = var_1.__sub__(var_7)
        var_9 = paddle.nn.functional.loss.cross_entropy(var_0, var_3, reduction='none')
        var_10 = var_9.__mul__(var_6)
        var_11 = paddle.nn.functional.loss.cross_entropy(var_0, var_4, reduction='none')
        var_12 = var_11.__mul__(var_8)
        var_13 = var_10.__add__(var_12)
        var_14 = var_13.__rmul__(0.25)
        var_15 = var_14.__mul__(var_2)
        var_16 = var_15.sum()
        var_17 = var_16.__truediv__(4.0)
        return var_17


def create_tensor_inputs():
    inputs = (
        paddle.rand(shape=[24, 8], dtype=paddle.float32),
        paddle.rand(shape=[24], dtype=paddle.float32),
        paddle.rand(shape=[24], dtype=paddle.float32),
    )
    return inputs


def create_numpy_inputs():
    inputs = (
        np.random.random(size=[24, 8]).astype('float32'),
        np.random.random(size=[24]).astype('float32'),
        np.random.random(size=[24]).astype('float32'),
    )
    return inputs


class TestLayer(unittest.TestCase):
    def setUp(self):
        self.inputs = create_tensor_inputs()
        self.net = LayerCase()
    def train(self, net, to_static, with_prim=False, with_cinn=False):
        if to_static:
            paddle.set_flags({'FLAGS_prim_all': with_prim})
            if with_cinn:
                build_strategy = paddle.static.BuildStrategy()
                build_strategy.build_cinn_pass = True
                net = paddle.jit.to_static(net, build_strategy=build_strategy, full_graph=True)
            else:
                net = paddle.jit.to_static(net, full_graph=True)
        paddle.seed(123)
        outs = net(*self.inputs)
        return outs
    def test_ast_prim_cinn(self):
        st_out = self.train(self.net, to_static=True)
        cinn_out = self.train(self.net, to_static=True, with_prim=True, with_cinn=True)
        for st, cinn in zip(paddle.utils.flatten(st_out), paddle.utils.flatten(cinn_out)):
            np.testing.assert_allclose(st.numpy(), cinn.numpy(), atol=1e-8)


if __name__ == '__main__':
    unittest.main()