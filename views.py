import models

def get_users():
    results = models.User.query.all()
    return [itm.to_dict() for itm in results]