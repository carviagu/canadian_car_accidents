############################################
# Script with functions to valuate models
############################################

from sklearn import metrics
from matplotlib import pyplot as plt


def accuracy(test=None, pred=None):
    if test is None or pred is None:
        print('ERROR: Real and Predicted values must be provided')
        return -1

    return metrics.accuracy_score(test, pred)


def confusion_matrix_estimator(titles_options = None, model = None,
                               test = None, pred = None, labels = None):
    for title, normalize in titles_options:
        disp = metrics.ConfusionMatrixDisplay.from_estimator(
            model,
            test,
            pred,
            display_labels=labels,
            cmap=plt.cm.Blues,
            normalize=normalize
        )
        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

    plt.show()


def confusion_matrix(titles_options = None, test = None, pred = None, labels = None):
    for title, normalize in titles_options:
        disp = metrics.ConfusionMatrixDisplay.from_predictions(
            test,
            pred,
            display_labels=labels,
            cmap=plt.cm.Blues,
            normalize=normalize
        )
        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

    plt.show()


def roc_curve(test = None, pred = None, label = "Model"):

    yhat = pred
    # calculate roc curves
    fpr, tpr, thresholds = metrics.roc_curve(test, yhat)
    # plot the roc curve for the model
    plt.plot([0,1], [0,1], linestyle='--', label='No Skill')
    plt.plot(fpr, tpr, marker='.', label=label)
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    # show the plot
    plt.show()