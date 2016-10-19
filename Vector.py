import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def add(self, v):
        if v.dimension != self.dimension:
            return None
        i = 0
        a = list(self.coordinates)
        new_coordinaes = []
        for x in v.coordinates:
            print (x)
            new_coordinaes.append(a[i] + x)
            i=i+1
        return Vector(new_coordinaes)

    def sub(self, v):
        if v.dimension != self.dimension:
            return None
        i = 0
        a = list(self.coordinates)
        new_coordinaes = []
        for x in v.coordinates:
            new_coordinaes.append(a[i] - x)
            i=i+1
        return Vector(new_coordinaes)

    def scalar_multiply(self, s):
        new_coordinaes = []
        for x in self.coordinates:
            new_coordinaes.append(x * s)
        return Vector(new_coordinaes)

    def magnitude(self):
        sq = [f*f for f in self.coordinates]
        return math.sqrt(sum(sq))
    
    def direction(self):
        return self.scalar_multiply(1/self.magnitude())
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


def main():
    v1 = Vector([8.218,-9.341])
    v2 = Vector([-1.129,2.111])
    print (v1.add(v2))
    v1 = Vector([7.119,8.215])
    v2 = Vector([-8.223,0.878])
    print (v1.sub(v2))
    v1 = Vector([1.671,-1.012,-0.318])
    print (v1.scalar_multiply(7.41))

    v1 = Vector([8.218,-9.341])
    print (v1.magnitude())
    print (v1.direction())

    print('second')
    v1 = Vector([-0.221,7.437])
    print (v1.magnitude())
    print (v1.direction())

    v1 = Vector([8.813,-1.331,-6.247])
    print (v1.magnitude())
    print (v1.direction())

    v1 = Vector([5.581,-2.136])
    print (v1.magnitude())
    print (v1.direction())

    v1 = Vector([1.996,3.108,-4.554])
    print (v1.magnitude())
    print (v1.direction())
    
    print ('completed')
		
if __name__ == "__main__":
    main()
