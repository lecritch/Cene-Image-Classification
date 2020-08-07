import matplotlib.pyplot as plt
parent_dir = '../'

def visualize_training_results(results):
    """
    A function to visualise a model's loss and accuracy, comparing
    train and validation sets.
    """
    history = results.history
    plt.figure(figsize = (10, 8))
    plt.plot(history['val_loss'])
    plt.plot(history['loss'])
    plt.legend(['val_loss', 'loss'])
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.savefig(parent_dir + 'figures/model_loss')
    plt.show();
    
    plt.figure(figsize = (10, 8))
    plt.plot(history['val_acc'])
    plt.plot(history['acc'])
    plt.legend(['val_acc', 'acc'])
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.savefig(parent_dir + 'figures/model_accuracy')
    plt.show();