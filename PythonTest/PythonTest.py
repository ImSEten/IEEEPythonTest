#!F:\PyCharm-projects
# coding : utf-8
# author : 葛壮壮

import tensorflow as tf
#from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.misc
def model_test(filename):
    output='./TestImage/'
    if not os.path.exists(output):
        os.makedirs(output)
    #input='TFcodeX_10.tfrecord'
    input=filename

    image_count = 0
    for record in tf.python_io.tf_record_iterator(input):
        image_count += 1
    print("image_count is %d" % image_count)
    
    data_files = tf.gfile.Glob(input)
    print(data_files)
    # 文件名列表生成器

    filename_queue = tf.train.string_input_producer(data_files,shuffle=True)
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)   #返回文件名和文件
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'data': tf.FixedLenFeature([256,256], tf.float32),
                                           'label': tf.FixedLenFeature([1], tf.int64),
                                           'id': tf.FixedLenFeature([], tf.int64),
                                       })  #取出包含image和label的feature对象n
    #tf.decode_raw可以将字符串解析成图像对应的像素数组

    image = tf.cast(features['data'],tf.float32)
    #image = tf.reshape(image,[256,256])
    #image = tf.add(image,1)
    id = tf.cast(features['id'],tf.int64)
    label = tf.cast(features['label'], tf.int64)
    #print(label)
    #image = tf.reshape(image, [256,256])
    with tf.Session() as sess: #开始一个会话
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        #启动多线程
        coord=tf.train.Coordinator()
        threads= tf.train.start_queue_runners(coord=coord)

        for batch_index in range(image_count):
            batch_images,batch_labels = sess.run([image, label])
            global str
            tmp_images = (batch_images+1)*128
            #print(tmp_images)
            im = Image.fromarray(tmp_images)
            im = im.convert('L')
            #plt.imshow(im)
            #plt.show()
            #im.save(output+str(batch_index)+'_''Label_'+str(batch_labels)+'.jpg')
            im.save(output + str(batch_index) + '_''Label_' + str(batch_labels) + '.jpg')
            #im.save(output + str(batch_index) + '_''Label_' + str(batch_labels) + '.jpg')

        coord.request_stop()
        coord.join(threads)
        sess.close()

    lines = tf.gfile.GFile('./output_labels.txt').readlines()
    uid_to_human = {}
    #一行一行读取数据
    for uid,line in enumerate(lines) :
        #去掉换行符
        line=line.strip('\n')
        uid_to_human[uid] = line

    def id_to_string(node_id):
        if node_id not in uid_to_human:
            return ''
        return uid_to_human[node_id]

    #创建一个图来存放google训练好的模型
    with tf.gfile.FastGFile('./output_graph.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        #遍历目录
        for root,dirs,files in os.walk('./TestImage/'):
            acc_count = 0
            level = []
            for file in files:
                #载入图片
                image_data = tf.gfile.FastGFile(os.path.join(root,file), 'rb').read()

                predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})#图片格式是jpg格式

                predictions = np.squeeze(predictions)#把结果转为1维数据
                #print(predictions)
                #打印图片路径及名称
                str = os.path.join(root,file)
                #print(str)
                for i in range(len(str)):
                    if str[i] == '[':
                        level_image = int(str[i+1])
                        #print('%d' % level)
                        level.append(level_image)
                        break
                    else:
                        i += 1
                #排序
                top_k = predictions.argsort()[::-1] + 1
                #print(top_k[0])

                if level_image == top_k[0]:
                    acc_count += 1

            #print("acc_count is %d" % acc_count)
            #print("file_count is %d" % image_count)
            Accuracy = acc_count / image_count
            print("Accuracy is %.2f%%" % (Accuracy * 100))
        print(level)
    return level

def main():
    level = model_test('TFcodeX_5.tfrecord')

if __name__ == '__main__':
    main()
# def model_test(filename):



