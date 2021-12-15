############################################
# Script with functions to valuate models
############################################

from sklearn import metrics
from matplotlib import pyplot as plt


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
    
def models_summary(models = None):
    '''
    Makes model summary with Recall, Precission and AUC scores
    :param models:
    :return:
    '''
    scores = pd.DataFrame(data = models.keys(), columns = ['Models'], index = [0, 1, 2, 3, 4])

    pres = list()
    rec = list()
    roc = list()

    for key in models:
        Y_pred = models[key].predict(X_test)
        # Precision
        pres.append(metrics.precision_score(Y_test, Y_pred, zero_division = 0.0, labels=[0], average='weighted'))
        # Recall
        rec.append(metrics.recall_score(Y_test, Y_pred, zero_division = 0.0, labels=[0], average='weighted'))
        # RocAUC
        roc.append(metrics.roc_auc_score(Y_test, models[key].predict_proba(X_test)[:,1]))

    scores['Precision'] = pres
    scores['Recall'] = rec
    scores['Roc_Auc'] = roc
    
    return scores
    