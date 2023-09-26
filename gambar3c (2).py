with open("test.txt", "w") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)
