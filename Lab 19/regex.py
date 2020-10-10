#Serhii Maltsev (sm5zj)
import re

nospace = re.compile(r"\S+")
quotation = re.compile(r"\"[^ ][^\"]*?[^ ]\"")
twonum = re.compile(r"(-?\d+\.\d+|-?\d+)(, |,| )(-?\d+\.\d+|-?\d+)")


