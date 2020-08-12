import matplotlib.pyplot as plt
PARENT_DIR = '../'

# plot params:
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['figure.figsize'] = [10, 8]

def loss_acc_vis(results, title, save_as = 'figures/model'):
    """
    results:  results of fitted model
    title:  string of title you want for the plot.  Just needs to be 
            which model it is for as each plot will end with 'Loss' or 'Accuracy' 
            accordingly.  e.g. 'Model 2 Loss', then title = 'Model 2'
    save_as:  string of file path to where figure should be saved to.  Defaults to figures 
            folder.  Ideally put the name of the model. 
    """
    history = results.history
    plt.figure(figsize = (10, 8))
    plt.plot(history['val_loss'])
    plt.plot(history['loss'])
    plt.legend(['val_loss', 'loss'])
    plt.title(f'{title} Loss', fontsize = 25)
    plt.xlabel('Epochs', fontsize = 22)
    plt.ylabel('Loss', fontsize = 22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.savefig(PARENT_DIR + f'{save_as}_loss')
    plt.show();

    plt.figure(figsize = (10, 8))
    plt.plot(history['val_accuracy'])
    plt.plot(history['accuracy'])
    plt.legend(['val_acc', 'acc'])
    plt.title(f'{title} Accuracy', fontsize = 25)
    plt.xlabel('Epochs', fontsize = 22)
    plt.ylabel('Accuracy', fontsize = 22)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.savefig(PARENT_DIR + f'{save_as}_accuracy')
    plt.show();