import ROOT
import numpy as n

x=n.linspace(0,4*n.pi,101)
y=n.cos(x)

g=ROOT.TGraph(len(x),x,y)
g.SetTitle("cos in x=[%.1f, %.1f]" % (x[0],x[-1]))
g.GetXaxis().SetTitle("x")
g.GetYaxis().SetTitle("cos(x)")
g.Draw("AL")
