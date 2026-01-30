from pathlib import Path
from organizer.organizer import (
    plan_organization,
    file_filter
)


def test_plan_organization():
    """
    assert plan_organization(path("test_image")) contains tests_image/images
    """


def test_file_filter():

    assert file_filter(Path("test.png")) == "images"
    assert file_filter(Path("test.mp4")) == "videos"
    assert file_filter(Path("test.txt")) == "documents"
    assert file_filter(Path("test.zip")) == "archives"
    assert file_filter(Path("test.cbz")) == "others"
    return

