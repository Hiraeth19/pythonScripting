import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-a', '--len',required = True, help = "first operand")
ap.add_argument('-b','--charater',required = False, help = "second operand")
args = vars(ap.parse_args())
print("{}".format(int(args['len']) * args['charater']))


