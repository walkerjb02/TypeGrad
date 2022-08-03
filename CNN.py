from keras import layers, models
from keras.optimizers import SGD
from emnist import extract_training_samples, extract_test_samples

def load_data():
    xtrain, ylabel = extract_training_samples('letters')
    xtest, ytest = extract_test_samples('letters')
    xtrain = xtrain / 255
    xtest = xtest / 255
    return (xtrain, ylabel, xtest, ytest)

def CNN(train_images, train_labels, test_images, test_labels):
    model = models.Sequential()
    model.add(layers.Conv2D(28, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(56, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(56, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(56, activation='softmax'))
    model.add(layers.Dense(26))
    opt = SGD(learning_rate=0.0001, decay=1e-4, momentum=0.6)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10,
                        validation_data=(test_images, test_labels))
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f"Test Loss = {test_loss}\nTest Accuracy = {test_acc}")

data = load_data()
CNN(train_images=data[0], train_labels=data[1], test_images=data[2], test_labels=data[3])
