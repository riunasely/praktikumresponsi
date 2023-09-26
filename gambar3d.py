with open("foto27.jpg", "rb") as rf:
    with open("foto27_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)
