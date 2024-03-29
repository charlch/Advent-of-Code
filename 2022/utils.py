import re
import math
import hashlib
import operator
from functools import total_ordering


LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
UPPER_LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz'.upper()]
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)


def parse_line(regex, line):
    ret = []
    for match in re.match(regex, line).groups():
        try:
            ret.append(int(match))
        except ValueError:
            ret.append(match)

    return ret


def parse_nums(line, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]


def new_table(val, width, height):
    return [[val for _ in range(width)] for _ in range(height)]


def transposed(matrix):
    """Returns the transpose of the given matrix."""
    return [list(r) for r in zip(*matrix)]


def rotated(matrix):
    """Returns the given matrix rotated 90 degrees clockwise."""
    return [list(r) for r in zip(*matrix[::-1])]


def mul(lst):
    """Like sum(), but for multiplication."""
    return reduce(operator.mul, lst, 1)  # NOQA


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def all_unique(lst):
    return len(lst) == len(set(lst))


def factors(n):
    """Returns the factors of n."""
    return sorted(
        x for tup in (
            [i, n // i] for i in range(1, int(n ** 0.5) + 1)
            if n % i == 0)
        for x in tup)


def memoize(f):
    """Simple dictionary-based memoization decorator"""
    cache = {}

    def _mem_fn(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    _mem_fn.cache = cache
    return _mem_fn


def _eratosthenes(n):
    """http://stackoverflow.com/a/3941967/239076"""
    # Initialize list of primes
    _primes = [True] * n

    # Set 0 and 1 to non-prime
    _primes[0] = _primes[1] = False

    for i, is_prime in enumerate(_primes):
        if is_prime:
            yield i

            # Mark factors as non-prime
            for j in xrange(i * i, n, i):  # NOQA
                _primes[j] = False


def primes(n):
    """Return a list of primes from [2, n)"""
    return list(_eratosthenes(n))


def md5(msg):
    m = hashlib.md5()
    m.update(msg)
    return m.hexdigest()


def sha256(msg):
    s = hashlib.sha256()
    s.update(msg)
    return s.hexdigest()


def knot_hash(msg):
    lengths = [ord(x) for x in msg] + [17, 31, 73, 47, 23]
    sparse = range(0, 256)
    pos = 0
    skip = 0

    for _ in range(64):
        for l in lengths:
            for i in range(l // 2):
                x = (pos + i) % len(sparse)
                y = (pos + l - i - 1) % len(sparse)
                sparse[x], sparse[y] = sparse[y], sparse[x]

            pos = pos + l + skip % len(sparse)
            skip += 1

    hash_val = 0

    for i in range(16):
        res = 0
        for j in range(0, 16):
            res ^= sparse[(i * 16) + j]

        hash_val += res << ((16 - i - 1) * 8)

    return '%032x' % hash_val


HEX_DIRS = {
    'N': (1, -1, 0),
    'NE': (1, 0, -1),
    'SE': (0, 1, -1),
    'S': (-1, 1, 0),
    'SW': (-1, 0, 1),
    'NW': (0, -1, 1),
}


def hex_distance(x, y, z):
    """Returns a given hex point's distance from the origin."""
    return (abs(x) + abs(y) + abs(z)) // 2


@total_ordering
class Point:
    """Simple 2-dimensional point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle(self, to=None):
        if to is None:
            return math.atan2(self.y, self.x)
        return math.atan2(self.y - to.y, self.x - to.x)

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def neighbours_4(self):
        return [self + p for p in DIRS_4]

    def neighbours_8(self):
        return [self + p for p in DIRS_8]

    def turn_left(self, a):
        if a ==90:
            return Point(-self.y, self.x)
        if a == 180:
            return -self
        if a== 270:
            return Point(self.y, -self.x)

    def turn_right(self, a):
        if a ==90:
            return Point(self.y, -self.x)
        if a == 180:
            return -self
        if a== 270:
            return Point(-self.y, self.x)

    def unit(self):
        return Point(int(self.x / self.length), int(self.y/self.length))


DIRS_4 = DIRS = [
    Point(0, 1),   # north
    Point(1, 0),   # east
    Point(0, -1),  # south
    Point(-1, 0),  # west
]

DIRS_8 = [
    Point(0, 1),    # N
    Point(1, 1),    # NE
    Point(1, 0),    # E
    Point(1, -1),   # SE
    Point(0, -1),   # S
    Point(-1, -1),  # SW
    Point(-1, 0),   # W
    Point(-1, 1),   # NW
]

class Point3D():
    def __init__(self, x, y, z):
        self.x =x
        self.y=y
        self.z=z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n, self.z * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n, self.z/n)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z==other.z

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Point3D({}, {}, {})".format(self.x, self.y, self.z)

    def __hash__(self):
        return hash(tuple((self.x, self.y, self.z)))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z -other.z)

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z. ** 2)

    def neighbours_6(self):
        return [self + p for p in DIRS3D]


DIRS3D = [Point3D(1,0,0),
Point3D(-1,0,0),
Point3D(0,1,0),
Point3D(0,-1,0),
Point3D(0,0,-1),Point3D(0,0,-1)]

class Board(dict):
    def __init__(self, data=""):
        dict.__init__({})
        w=h=0
        for y,lin in enumerate(data.split("\n")):
            h=y+1
            for x,char in enumerate(lin):
                w=x+1
                self[Point(x,y)] = char
        self.width=w
        self.height=h

    def recalc_range(self):
        w=h=0
        for p in self:
            w= max(w, p.x)
            h= max(h, p.y)
        self.width=w
        self.height=h
            
    def __repr__(self, x_range=None, y_range=None):
        x_range = x_range or range(-5,self.width+6)
        y_range = y_range or range(-5,self.height+6)
        
        rep = "┌" + ("".join(str(i%10) for i in x_range)) + "x\n"
        for y in y_range:
            rep+=str(y%10)+"".join(self.get(Point(x,y),"?") for x in x_range)+"│\n"
        rep += "y" + ("─"*len(x_range)) + "┘\n"
        return rep

    def find_elements(self, elements):
        return {p: char for p, char in self.items() if char in elements}

    def copy(self, empty=False):
        new_board = Board()
        new_board.width = self.width
        new_board.height = self.height
        if not empty:
            for k, v in self.items():
                new_board[k]=v
        return new_board
        
    def transform(self, fn):
        new_board = self.copy(empty = True)
        any_change = False
        for p, char in self.items():
            new_char = fn(p, char, self)
            if char != new_char:
                any_change = True
            new_board[p] = new_char
        return new_board, any_change

    
    
