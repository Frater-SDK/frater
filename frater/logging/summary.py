def get_default_summary(data, eol=' '):
    return str(data)


def get_summary(data, summarizer=None, multiline=True):
    if summarizer is None:
        summarizer = get_default_summary
    eol = '\n' if multiline else ' '
    return summarizer(data, eol)
