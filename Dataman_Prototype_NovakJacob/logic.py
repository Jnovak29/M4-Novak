import store

def complete_activity(learner_id, activity_id):
    store.save_completion(learner_id, activity_id)

def view_progress(learner_id):
    return store.get_completions(learner_id)