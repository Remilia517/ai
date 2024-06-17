import numpy as np
from value import Value

class CrossEntropyLoss:
    def __call__(self, logits, labels):
        exp_scores = [Value(np.exp(logit.data)) for logit in logits]
        sum_exp_scores = Value(sum(exp_scores).data)
        probs = [exp_score / sum_exp_scores for exp_score in exp_scores]
        log_probs = [Value(np.log(prob.data)) for prob in probs]
        loss = sum([-label * log_prob for label, log_prob in zip(labels, log_probs)])
        return loss
