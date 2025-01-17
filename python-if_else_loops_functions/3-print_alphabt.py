#!/usr/bin/python3
print(
    "{}".format("".join(
        chr(x) for x in range(97, 123) if x != 113 and x != 101
    )),
    end=""
)
