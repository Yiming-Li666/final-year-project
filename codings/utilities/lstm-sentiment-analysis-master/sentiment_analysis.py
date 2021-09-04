from encoder import Model, sst_binary, model_train, model_predict, model_load
from matplotlib import pyplot as plt
# 选择语言中文还是英文
languageType = ''
while (languageType != 'c' and languageType != 'e'):
    languageType = input("Please enter a train type(chinese enter lower: c , english enter lower: e): ")

max_length = ''  #一句话最大长度
load_path = ''  #文件加载路径
language = ''  #语言类型
tr_num = 30 #训练集
va_num = 10 #训练集

if languageType == 'c':
    max_length = 100
    # data path
    load_path = 'data/chinese'
    language = 'chinese'
    tr_num = 100
    va_num = 25
elif languageType == 'e':
    max_length = 40
    load_path = 'data/english'
    language = 'english'
    tr_num = 8000
    va_num = 600 


model = Model(max_length)

all_data = sst_binary(load_path)  #分别获取所有的句子和标签
print('=> Succeeds in loading <' + language + '> file and starting to translate words into Embeddedness······')

x, y, wi = model.transform(all_data)  #将每个句子里的词转化成词频索引值
print('=> Succeeds in translating swords into word Embeddedness and starting to train the model process······')

history,acc = model_train(x, y, wi, language, max_length, tr_num, va_num)  #训练模型  (如果已经有训练好的模型，这行代码注释掉)
print('=> accuracy: ', acc*100, '%')
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))

plt.plot(epochs,acc, 'b', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='validation accuracy')
plt.title('Training and validation accuracy')
plt.legend(loc='lower right')
plt.figure()

plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
# model_load(language) #如果模型训练好了，调用此方法直接加载模型，不需要再训练

# model_load(language) #如果模型训练好了，调用此方法直接加载模型，不需要再训练

while True:
    sentence = input("Please enter a single sentence to predict:")
    result = model_predict(sentence, max_length)
    print(result)
    # if result == 0:
    #    print('小儿感冒')
    # elif result == 1:
    #    print("贫血")
    # elif result == 2:
    #    print("骨折")
    # elif result == 3:
    #    print("消化不良")
    # else:
    #    print("失眠")
