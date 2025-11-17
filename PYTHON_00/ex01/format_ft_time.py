import datetime

now = datetime.datetime.now()
epoch = datetime.datetime(1970, 1, 1, 0, 0, 0)
seconds = (now - epoch).total_seconds()

print(
    f"Seconds since January 1st, 1970: {seconds} of {seconds:e} in scientific notation"
)

print(now.strftime("%b %d %Y"))
