import tempfile
import os
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from organizer.organizer import (
    plan_organization,
    file_filter,
    get_unique_path
)


def test_plan_organization():
    with (
        TemporaryDirectory() as d,
        tempfile.NamedTemporaryFile(dir=d, suffix=".txt") as document,
        tempfile.NamedTemporaryFile(dir=d, suffix=".png") as image,
        tempfile.NamedTemporaryFile(dir=d, suffix=".mp4") as video,
        tempfile.NamedTemporaryFile(dir=d, suffix=".zip") as archive,
        tempfile.NamedTemporaryFile(dir=d, suffix=".cbz") as comic,
        tempfile.NamedTemporaryFile(dir=d, suffix=".mp3") as audio
    ):
        organized_temp_d = plan_organization(Path(d))
        assert organized_temp_d[Path(document.name)] == Path(d + "/documents/" + os.path.basename(document.name))
        assert organized_temp_d[Path(image.name)] == Path(d + "/images/" + os.path.basename(image.name))
        assert organized_temp_d[Path(video.name)] == Path(d + "/videos/" + os.path.basename(video.name))
        assert organized_temp_d[Path(archive.name)] == Path(d + "/archives/" + os.path.basename(archive.name))
        assert organized_temp_d[Path(comic.name)] == Path(d + "/others/" + os.path.basename(comic.name))
        assert organized_temp_d[Path(audio.name)] == Path(d + "/audio/" + os.path.basename(audio.name))


def test_file_filter():

    assert file_filter(Path("test.png")) == "images"
    assert file_filter(Path("test.mp4")) == "videos"
    assert file_filter(Path("test.txt")) == "documents"
    assert file_filter(Path("test.zip")) == "archives"
    assert file_filter(Path("test.cbz")) == "others"
    assert file_filter(Path("test.mp3")) == "audio"
    return


def test_get_unique_path():
    with (
        TemporaryDirectory() as d,
        tempfile.NamedTemporaryFile(dir=d, suffix=".txt") as document,
        tempfile.NamedTemporaryFile(dir=d, suffix=".png") as image,
        tempfile.NamedTemporaryFile(dir=d, suffix=".jpg") as image2
    ):

        assert get_unique_path(Path(document.name)) == Path(document.name).parent / f"{Path(document.name).stem} (1).txt"
        assert get_unique_path(Path(image.name)) == Path(image.name).parent / f"{Path(image.name).stem} (1).png"
        assert get_unique_path(Path(image2.name)) == Path(image2.name).parent / f"{Path(image2.name).stem} (1).jpg"
