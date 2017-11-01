import numpy as np
import chainer
import chainer.links as L
import chainer.functions as F
from chainer import Chain, optimizers, Variable, serializers, cuda

xp = cuda.cupy

x_train = xp.load('face_data.npy').astype(xp.float32)
x_test = xp.load('face_test_data.npy').astype(xp.float32) #テスト用のデータを用意
t_train = xp.load('face_label.npy').astype(xp.int32)
t_test = xp.load('face_test_label.npy').astype(xp.int32) #テスト用データに対するラベリングを用意

Ntrain = x_train.shape[0]
Ntest = x_test.shape[0]

#今回は分類するクラスを7としていますが、各自用意したクラス数で
class CNN(Chain):
    def __init__(self):
        super(CNN,self).__init__(
            conv1 = L.Convolution2D(3,32,4),
            conv2 = L.Convolution2D(32,64,4),
            l1 = L.Linear(2304,1000),
            l2 = L.Linear(1000,1000),
            l3 = L.Linear(1000,7)
        )
    def forward(self,x):
        h = F.max_pooling_2d(F.relu(self.conv1(x)),2)
        h = F.max_pooling_2d(F.relu(self.conv2(h)),2)
        h = F.dropout(F.relu(self.l1(h)),ratio=0.2)
        h = F.relu(self.l2(h))
        h = self.l3(h)
        return h

model = CNN()

cuda.get_device(0).use()
model.to_gpu()

optimizer = optimizers.Adam()
optimizer.setup(model)

epochs = 300

for epoch in range(epochs):
    train_accuracy = 0
    
    x = Variable(x_train)[0:Ntrain]
    t = Variable(t_train)[0:Ntrain]
    y = model.forward(x)
    model.zerograds()
    loss = F.softmax_cross_entropy(y,t)
    acc = F.accuracy(y,t)
    loss.backward()
    optimizer.update()

    train_accuracy = acc.data
    print("epoch : {} accuracy : {}".format(epoch,train_accuracy))

serializers.save_npz('HairColor_Recognition.model',model)

#テストデータに対してaccuracyを計算
count = 0
with chainer.using_config('train',False):
    for i in range(0,Ntest):
        x = Variable(xp.array([x_test[i]],dtype=xp.float32))
        t = t_test[i]
        y = model.forward(x)
        y = np.argmax(y.data[0])
        if t == y:
            count += 1

print("test accuracy : {}".format(count/Ntest))