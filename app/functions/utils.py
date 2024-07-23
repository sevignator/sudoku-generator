def retry_until_successful(fn):
    try:
        return fn()
    except:
        return retry_until_successful(fn)
