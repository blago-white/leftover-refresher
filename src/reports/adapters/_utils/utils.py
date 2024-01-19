import io


def get_io_from_bytes(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
