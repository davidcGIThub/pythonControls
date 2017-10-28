import matplotlib.pyplot as plt
def showState(c):
    plt.figure(1)
    plt.clf()
    plt.fill([5+c, 5+c, 10+c,10+c, 5+c],[0, 5, 5, 0, 0],'r')
    plt.axis([0, 20, 0, 10])
    plt.axes().set_aspect('equal')
    plt.plot([0,2.25+c/2],[1,1],'g',[2.75+c/2,5+c],[1,1],'g',[2.75+c/2,c/2+2.25,2.25+c/2,2.75+c/2],[.5,.5,1.5,1.5],'g',[2.75+c/2,2.75+c/2],[.75,1.25],'g');
    plt.plot([0,1.5,1.75+c*(.5/4),2.25+c*(1.5/4),2.75+c*(2.5/4),3.25+c*(3.5/4),3.5+c,5+c],[4,4,4.5,3.5,4.5,3.5,4,4]);
    plt.show()
