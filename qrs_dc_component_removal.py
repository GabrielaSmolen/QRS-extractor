
class QRS:

    def __init__(self, qrs):

        self.qrs = qrs


if __name__ == '__main__':
    qrs = [-0.18,-0.155,-0.135,-0.155,-0.19,-0.205,-0.235,-0.225,-0.245,-0.25,-0.26,-0.275,-0.275,-0.275,-0.265,-0.255,-0.265,-0.275,-0.29,-0.29,-0.29,-0.29,-0.285,-0.295,-0.305,-0.285,-0.275,-0.275,-0.28,-0.285,-0.305,-0.29,-0.3,-0.28,-0.29,-0.3,-0.315,-0.32,-0.335,-0.36,-0.385,-0.385,-0.405,-0.455,-0.485,-0.485,-0.425,-0.33,-0.22,-0.07,0.12,0.375,0.62,0.78,0.84,0.765,0.52,0.17,-0.165,-0.365,-0.435,-0.425,-0.37,-0.33,-0.325,-0.335,-0.345,-0.33,-0.325,-0.315,-0.31,-0.32,-0.335,-0.34,-0.325,-0.345,-0.335,-0.33,-0.335,-0.33,-0.325,-0.33,-0.33,-0.345,-0.355,-0.335,-0.325,-0.305,-0.32,-0.32,-0.33,-0.34,-0.335,-0.34,-0.345,-0.355,-0.355,-0.34,-0.33,-0.33,-0.33,-0.34,-0.35,-0.325,-0.325,-0.33,-0.33,-0.335]
    # qrs = [-0.315,-0.315,-0.295,-0.295,-0.3,-0.305,-0.31,-0.32,-0.305,-0.305,-0.3,-0.31,-0.32,-0.325,-0.315,-0.315,-0.315,-0.325,-0.34,-0.35,-0.33,-0.33,-0.33,-0.34,-0.335,-0.345,-0.345,-0.335,-0.33,-0.335,-0.36,-0.37,-0.365,-0.355,-0.38,-0.385,-0.415,-0.44,-0.45,-0.475,-0.505,-0.51,-0.55,-0.625,-0.795,-1.055,-1.35,-1.685,-1.99,-2.215,-2.39,-2.525,-2.62,-2.695,-2.715,-2.69,-2.625,-2.535,-2.42,-2.26,-2.05,-1.805,-1.58,-1.355,-1.15,-0.935,-0.745,-0.58,-0.435,-0.33,-0.27,-0.245,-0.23,-0.205,-0.155,-0.11,-0.065,-0.06,-0.045,-0.035,-0.005,0.02,0.04,0.05,0.065,0.085,0.12,0.14,0.145,0.145,0.13,0.13,0.145,0.165,0.175,0.19,0.2,0.215,0.23,0.25,0.265,0.29,0.29,0.275,0.26,0.265,0.255,0.255]

    samples = QRS(qrs)

print(qrs)