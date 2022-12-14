
from ipfs_video_gateway.start import is_stable, FOLDER_STATUS_CACHE

def test_is_stable():
    assert is_stable("src") == False, "First time should be unstable"
    assert is_stable("src") == True, "Second time we see nothing changed"
    is_stable("src", forget=True)
    assert "src" not in FOLDER_STATUS_CACHE