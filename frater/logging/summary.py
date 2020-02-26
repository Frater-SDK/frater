def get_default_summary(data, eol=' '):
    return str(data) + eol


def get_summary(data, summarizer=None, multiline=True):
    if summarizer is None:
        summarizer = get_default_summary
    eol = '\n' if multiline else ' '
    return summarizer(data, eol)


def summarize(data, multiline=True):
    return data.summary(multiline) if hasattr(data, 'summary') else get_summary(data, multiline=multiline)
