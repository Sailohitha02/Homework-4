# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "the rules are not mutually exclusive because some instances can satisfy multiple rules. For example, if a person has Home Owner = Yes, Marital Status = Single, Annual Income = Low, and Currently Employed = Yes, both rules 1 and 2 are satisfied, leading to a conflict (DB = Yes and DB = Yes)"
    answers["(b) explain"] = "the rule set is not exhaustive because there are instances of attribute values that do not satisfy any of the rules. For example, if a person has Home Owner = No, Marital Status = Divorced, Annual Income = Medium, and Currently Employed = No, none of the rules apply to this instance"
    answers["(c) explain"] = "ordering is needed for this set of rules because some instances can trigger multiple rules, leading to conflicts. For example, if a person has Home Owner = Yes, Marital Status = Single, Annual Income = Low, and Currently Employed = No, both rules 1 and 2 are satisfied (DB = Yes and DB = Yes). Without an order, there would be a conflict in deciding the class for this instance"
    answers["(d) explain"] = " a default class is needed for this rule set because it is not exhaustive. For instances that do not satisfy any of the rules, a default class should be specified to handle such cases. In the example mentioned earlier (Home Owner = No, Marital Status = Divorced, Annual Income = Medium, and Currently Employed = No), a default class would be required to determine the class label (DB = Yes or DB = No) for this instance."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Yes, the rules are mutually exclusive, as the conditions in each rule do not overlap with any other rule."
    answers["(b) example"] = "No, the rules are not exhaustive. There exist instances in the data set that do not satisfy the conditions of any of the given rules. For example, consider an amphibian like a frog. None of the rules cover the case where Gives Birth = No, Aerial Creature = No, Aquatic Creature = Semi"
    answers["(c) example"] = "no, ordering is not needed, as the rules assign different non-overlapping classes and at most one rule will be triggered for any instance."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The backpropagation algorithm for training Artificial Neural Networks (ANNs) involves two phases: forward and backward propagation. In the forward phase, inputs are passed through the network, and neuron outputs are computed layer by layer using weights from the previous iteration. In the backward phase, gradients of weights at each layer are computed recursively, starting from the output layer and moving backward through the network. The gradients of weights at layer k+1 are determined using the gradients of weights at layer k. This approach efficiently adjusts weights to minimize prediction errors, utilizing the chain rule of calculus to propagate error signals backward through the network."
    answers["(b) explain"] = "When applying an Artificial Neural Network (ANN) model, activations in the k+1th layer are computed from the kth layer through forward propagation. The perceptron model, a simple neural network, adjusts weights to fit input-output relationships during training. Learning in a perceptron involves updating weights until predictions align with true outputs of training examples"
    answers["(c) explain"] = "The vanishing gradient problem refers to a situation where gradients during backpropagation become extremely small, leading to slow or ineffective learning. It does not directly relate to the discrepancy between training and test errors"
    answers["(d) explain"] = "Even if an ANN model perfectly classifies all training instances during a back-propagation iteration, the gradients of the loss with respect to weights at all layers will not necessarily be 0. This is because the gradients are computed based on the difference between the predicted and actual outputs, which may not be exactly zero due to noise or other factors."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.4
    answers["(c) P(X_1=1 | -)"] = 0.25
    answers["(c) P(X_2=1 | +)"] = 0.25
    answers["(c) P(X_2=1 | -)"] = 0.16
    answers["(c) P(X_3=1 | +)"] = 0.2
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '+'
    answers["(d) Row 3"] = '+'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The data points are clearly separated into two distinct categories, indicating that using a single nearest neighbor (k=1) is sufficient to classify the nearby data point based on its proximity to the target class"
    answers["(b) explain"] = "There exists some overlap between the two categories of data points, suggesting that using a large value of k, such as k=50, is unnecessary. This is because including too many neighboring points may introduce errors and significantly increase computational costs without providing substantial benefits in classification accuracy."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "To calculate P(A=1|+), I counted the number of instances where feature ( A ) is equal to 1 among instances labeled as positive (+), and then divided this count by the total number of instances labeled as positive (+). This gave me the proportion of instances where ( A = 1 ) within the positive class."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857  # WRONG
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Given the probabilities computed using the naive Bayes approach:P(R|+) = 0.192 and P(R|-) = 0.032. Since P(R|+) > P(R|-), the record is assigned to the (+) class."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no' 

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Since the product of P(A=1|+) and P(B=1|+) is not equal to P(A=1, B=1|+), A and B are not conditionally independent given the class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
