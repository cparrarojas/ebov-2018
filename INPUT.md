# 2018 Ebola outbreak in the Democratic Republic of Congo

## Motivation

The Python app in this repository is an interactive visualisation that attempts to replicate the [results by Cristian Althaus](https://github.com/calthaus/Ebola/tree/master/DRC%20%28GitHub%202018%29) using a stochastic formulation of the *SEIR* model for the parameter estimation.

The model is defined by

$$\frac{\rm{d}\mathbf{x}}{\rm{d}t} = \mathbf{A}(\mathbf{x}) + \boldsymbol{\eta}(t)$$

<p align="center"><img src="https://rawgit.com/cparrarojas/sde-parameter-estimation/svgs/svgs/1f98df381e7e7f1299dd2d58c4da8f6a.svg?invert_in_darkmode" align=middle width=205.0356pt height=20.53161pt/></p>

where $\mathbf{x}=(S,E,I)$, and

$$\mathbf{A}(\mathbf{x}) = \left(\begin{array}{c}-\beta(t) S I/N \\ \beta(t) S I/N - \sigma E \\ \sigma E - \gamma I\end{array}\right)$$

$$\mathbf{B}(\mathbf{x}) = \left(\begin{array}{c c c} \beta(t) S I/N & -\beta(t) S I/N & 0 \\ -\beta(t) S I/N & \beta(t) S I/N + \sigma E & -\sigma E \\ 0 & -\sigma E & \sigma E + \gamma I\end{array}\right)$$

Here, $\beta(t)=\beta e^{-k(t-\tau)}$ for $t>\tau$ and $\beta(t)=\beta$ otherwise. The parameters to estimate are the base transmission rate $\beta$ and its rate of decay $k$. The remaining parameters are given by $1/\sigma=1/9.31\,\text{days}$, $1/\gamma=1/7.41\,\text{days}$, and $\tau=28\,\text{days}$.

The estimation is done from the [data for cumulative incidence](https://github.com/calthaus/Ebola/blob/master/DRC%20%28GitHub%202018%29/Ebola_outbreak_DRC2018_data.csv) corresponding to $N-S(t)$, where the population size is fixed at $N=10^6$, using the linear noise approximation as described in [Zimmer and Sahle (2014)](http://ieeexplore.ieee.org/abstract/document/7277317/) and [Zimmer (2015)](https://www.sciencedirect.com/science/article/pii/S0025556415001698). The likelihood function is handled by [`sdeparams`](https://github.com/cparrarojas/sde-parameter-estimation/).

Forecast (shaded region) is shown for the mean plus/minus std of 50 stochastic simulations run for 30 days starting from the latest data-point for any given pair of parameters.

## Usage

```bash
$python app.py
```

Upon opening the resulting link, you should see something like this:
<p align="center"><img src="https://rawgit.com/cparrarojas/ebov-2018/master/animation.gif" align=middle width=800px></p>

## Requirements (app only)

- Python 3.x
- `numpy`
- `pandas`
- `matplotlib`
- `plotly`
- `dash`
- `dash-renderer`
- `dash-core-components`
- `dash-html-components`
