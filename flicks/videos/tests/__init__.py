from contextlib import contextmanager

from flicks.videos.models import Video


@contextmanager
def build_video(user, **kwargs):
    """Create a new video object, with default acceptable values. The video
    is deleted once the block is exited."""
    args = {'title': 'Test',
            'description': 'Test description',
            'user': user,
            'category': 'test',
            'region': 'test',
            'upload_url': 'http://test.com',
            'shortlink': 'test_shortlink'}
    args.update(kwargs)

    video = Video.objects.create(**args)
    yield video
    video.delete()
