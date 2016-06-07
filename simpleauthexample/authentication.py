from django.contrib.auth.models import User as DjangoUser



class ForceAuthBackend(object):
    """
    Authentication backend for debugging
    """

    def authenticate(self, user_id=None):
        return DjangoUser.objects.get(id=user_id)

    def get_user(self, user_id):
        return DjangoUser.objects.get(pk=user_id)
