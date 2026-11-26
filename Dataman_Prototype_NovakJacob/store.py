completions = {}

def save_completion(learner_id, activity_id):
    completions.setdefault(learner_id, []).append(activity_id)

def get_completions(learner_id):
    return completions.get(learner_id, [])