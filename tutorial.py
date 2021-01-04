if __name__ == "__main__":
    from Vectors import Vector
    import matplotlib.pyplot as plt


    v1, v2, = Vector(10,0), Vector(0,10)
    v1.plot(plt, c="r")
    v2.plot(plt, c="g")


    v1 += v2
    v1.plot(plt, c="b")

    plt.show()

pass 