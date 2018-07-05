# 2018 Ebola outbreak in the Democratic Republic of Congo

## Motivation

The Python app in this repository is an interactive visualisation that attempts to replicate the [results by Cristian Althaus](https://github.com/calthaus/Ebola/tree/master/DRC%20%28GitHub%202018%29) using a stochastic formulation of the *SEIR* model for the parameter estimation.

The model is defined by

<p align="center"><img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/8408c8492f7ee269d4822cb9cbc91ffe.svg?invert_in_darkmode" align=middle width=141.36342pt height=33.812129999999996pt/></p>

<p align="center"><img src="https://rawgit.com/cparrarojas/sde-parameter-estimation/svgs/svgs/1f98df381e7e7f1299dd2d58c4da8f6a.svg?invert_in_darkmode" align=middle width=205.0356pt height=20.53161pt/></p>

where <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/f6f917d439b1b9d386192a989ffddff2.svg?invert_in_darkmode" align=middle width=91.00426499999999pt height=24.65759999999998pt/>, and

<p align="center"><img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/c35eb87ea9daff13fd2b38467d5498d3.svg?invert_in_darkmode" align=middle width=218.07059999999996pt height=59.178735pt/></p>

<p align="center"><img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/0ba078565431af8b5ac5a7739bfc5d3c.svg?invert_in_darkmode" align=middle width=394.71959999999996pt height=59.178735pt/></p>

Here, <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/843e00f5cd3d087e8d4b2b0917f4b354.svg?invert_in_darkmode" align=middle width=119.07043500000002pt height=29.19113999999999pt/> for <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/02287b47e24f18091894408359761db9.svg?invert_in_darkmode" align=middle width=36.900600000000004pt height=20.222069999999988pt/> and <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/01be662b82fd71a9b2704e0e18e0263b.svg?invert_in_darkmode" align=middle width=60.970305pt height=24.65759999999998pt/> otherwise. The parameters to estimate are the base transmission rate <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/8217ed3c32a785f0b5aad4055f432ad8.svg?invert_in_darkmode" align=middle width=10.165650000000005pt height=22.831379999999992pt/> and its rate of decay <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode" align=middle width=9.075495000000004pt height=22.831379999999992pt/>. The remaining parameters are given by <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/ade5357775220387c1c475220f63a5a5.svg?invert_in_darkmode" align=middle width=128.795865pt height=24.65759999999998pt/>, <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/d7589a02e178ad1b683928fbb14a026d.svg?invert_in_darkmode" align=middle width=128.236845pt height=24.65759999999998pt/>, and <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/30d3c465f0037285632349145e08bdc0.svg?invert_in_darkmode" align=middle width=82.19755500000001pt height=22.831379999999992pt/>.

The estimation is done from the [data for cumulative incidence](https://github.com/calthaus/Ebola/blob/master/DRC%20%28GitHub%202018%29/Ebola_outbreak_DRC2018_data.csv) corresponding to <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/ccd736d762f121a3684fae7ad66c5265.svg?invert_in_darkmode" align=middle width=64.840215pt height=24.65759999999998pt/>, where the population size is fixed at <img src="https://rawgit.com/cparrarojas/ebov-2018/svgs/svgs/b5b9788de90f0b9dfb14ed2d64708bb8.svg?invert_in_darkmode" align=middle width=59.908695pt height=26.76201000000001pt/>, using the linear noise approximation as described in [Zimmer and Sahle (2014)](http://ieeexplore.ieee.org/abstract/document/7277317/) and [Zimmer (2015)](https://www.sciencedirect.com/science/article/pii/S0025556415001698). The likelihood function is handled by [`sdeparams`](https://github.com/cparrarojas/sde-parameter-estimation/).

Forecast (shaded region) is shown for the mean plus/minus std of 50 stochastic simulations run for 30 days starting from the latest data-point for any given pair of parameters.
