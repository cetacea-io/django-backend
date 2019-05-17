from requests import request, HTTPError

from django.core.files.base import ContentFile

def get_profile_picture(backend, user, response, is_new=False, *args, **kwargs):
    avatar_url = None
    if backend.name == 'facebook':
        avatar_url = \
            'https://graph.facebook.com/{}/picture?type=large'\
            .format(response['id'])

    if avatar_url and is_new:
        try:
            response = request('GET', avatar_url)
            response.raise_for_status()
        except HTTPError:
            pass

        profile = user.profile
        profile.profile_picture.save('{0}_social.jpg'.format(user.id),
                                   ContentFile(response.content))
        profile.save()

def get_email(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        print(response.get('email'))
    