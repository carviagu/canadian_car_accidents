############################################
# Script with functions to valuate models
############################################

from sklearn import metrics
from matplotlib import pyplot as plt
import scikitplot as skplt


def accuracy(test=None, pred=None):
    '''
    Returns model accuracy
    :param test: real values
    :param pred: predicted values
    :return:
    '''
    if test is None or pred is None:
        print('ERROR: Real and Predicted values must be provided')
        return -1

    return metrics.accuracy_score(test, pred)


def confusion_matrix_estimator(titles_options = None, model = None,
                               test = None, pred = None, labels = None):
    '''
    Returns confusion matrix using only the labels
    :param titles_options:
    :param model:
    :param test:
    :param pred:
    :param labels:
    :return:
    '''
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
    '''
    Prints confusion matrix making the predictions
    :param titles_options:
    :param test:
    :param pred:
    :param labels:
    :return:
    '''
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
    '''
    Prints the model roc_curve
    :param test:
    :param pred:
    :param label:
    :return:
    '''
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


def model_curves_summary(test = None, pred = None, label = 'Model'):
    '''
    Prints a plot report with four different plots: ROC curve, PR curve,
    Gain curve, Lift curve
    :param test: Real values
    :param pred: Predicted values
    :param label: Model name
    '''
    fig, axes = plt.subplots(2, 2, figsize=(15, 10), sharey=False)
    fig.suptitle('Curvas del modelo ' + label)

    # ROC CURVE
    fpr, tpr, thresholds = metrics.roc_curve(test, pred[:,1])
    # plot the roc curve for the model
    axes[0,0].plot([0,1], [0,1], linestyle='--', label='No Skill')
    axes[0,0].plot(fpr, tpr, marker='.', label=label)
    # axis labels
    axes[0,0].set_title('Curva ROC')
    axes[0,0].set(xlabel='False Positive Rate', ylabel='True Positive Rate')
    axes[0,0].legend()
    axes[0,0].grid()

    # Precission-Recall CURVE
    # calculate pr-curve
    precision, recall, thresholds = metrics.precision_recall_curve(test, pred[:,1])
    no_skill = len(test[test==1]) / len(test)
    axes[0,1].plot([0,1], [no_skill,no_skill], linestyle='--', label='No Skill')
    axes[0,1].plot(recall, precision, marker='.', label=label)
    # axis labels
    axes[0,1].set_title('Curva Precission-Recall')
    axes[0,1].set(xlabel='Precission', ylabel='Recall')
    axes[0,1].legend()
    axes[0,1].grid()

    # GAIN CURVE
    skplt.metrics.plot_cumulative_gain(test, pred, ax = axes[1,0])

    # LIFT CURVE
    skplt.metrics.plot_lift_curve(test, pred, ax = axes[1,1])
