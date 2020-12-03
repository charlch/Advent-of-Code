def parse(data, form):
    lines = []
    for line in data.split("\n"):
        lines.append(parse_line(line, form))
    return lines

def parse_line(line, form):
    
    parts =[]
    for seg, next_seg in zip(form,form[1:]+[None]):
        if isinstance(seg, str):
            line = line[len(seg):]
        else:
            part, line = seg.get(line, next_seg)
            parts.append(part)
    return parts


class Part(object):
    def __init__(self, typ, length=None):
        #print("Part const",typ,length)
        self.length=length
        self.typ=typ
        #print(self)

    def get(self, line, next_delimiter=None):
        #print(self)
        if self.length:
            value = self.typ(line[0:self.length])
            rest = line[self.length:]
        elif next_delimiter:
            index = line.index(next_delimiter)
            value = self.typ(line[0:index])
            rest = line[index:]
        else:
            value = self.typ(line)
            rest = ""           

        return value, rest

class Int(Part):
    def __init__(self, length=None):
        Part.__init__(self, int, length)
    
class Str(Part):
    def __init__(self, length=None):
        Part.__init__(self, str, length)

class Float(Part):
    def __init__(self, length=None):
        Part.__init__(self, float, length)


if __name__ == "__main__":

    assert [2,9,"c","ccccccccc"] == parse_line("2-9 c: ccccccccc", [Int(), "-", Int(), " ", Str(1), ": ", Str()])
    assert [2.5,"c",": ccccccccc"] == parse_line("2.5 c: ccccccccc", [Float(3), " ", Str(1),  Str()])
    assert ["R",992] == parse_line("R992",[Str(1),Int()])
    assert ["TT5","Y6Q"] == parse_line("TT5)Y6Q", [Str(3), ")", Str()])
    assert ["TT5","Y6Q"] == parse_line("TT5)Y6Q", [Str(3), ")", Str(3)])
    assert ["TT5","Y6Q"] == parse_line("TT5)Y6Q", [Str(), ")", Str(3)])
    assert [-16, -1,-12] == parse_line("<x=-16, y=-1, z=-12>", ["<x=",Int(),", y=", Int(), ", z=", Int(), ">"])
