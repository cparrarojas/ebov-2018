# 2018 Ebola outbreak in the Democratic Republic of Congo

## Motivation

The Python app in this repository is an interactive visualisation that attempts to replicate the results by ... using a stochastic formulation for the parameter estimation.

The model is defined by

<p align="center"><img src="https://rawgit.com/cparrarojas/sde-parameter-estimation/svgs/svgs/0b5dcb93ea61d33f4ece87c5e14a9177.svg?invert_in_darkmode" align=middle width=161.98281pt height=37.82361pt/></p>

<p align="center"><img src="https://rawgit.com/cparrarojas/sde-parameter-estimation/svgs/svgs/1f98df381e7e7f1299dd2d58c4da8f6a.svg?invert_in_darkmode" align=middle width=205.0356pt height=20.53161pt/></p>

where $\mathbf{x}=(S,E,I)$, and

$$\mathbf{A}(\mathbf{X}) = \left(\begin{array}{c}-\beta(t) S I/N \\ \beta(t) S I/N - \sigma E \\ \sigma E - \gamma I\end{array}\right)$$

$$\mathbf{B}(\mathbf{x}) = \left(\begin{array}{c c} \beta(t) S I/N & -\beta(t) S I/N & 0 \\ -\beta(t) S I/N & \beta(t) S I/N + \sigma E & -\sigma E \\ 0 & -\sigma E & \sigma E + \gamma I\end{array}\right)$$

Here, $\beta(t)=\beta e^{-k(t-\tau)}$ for $t>\tau$ and $\beta(t)=\beta$ otherwise. The parameters to estimate are the base transmission rate $\beta$ and its rate of decay $k$. The remaining parameters are given by $1/\sigma=1/9.31\,\text{days}$, $1/\gamma=1/7.41\,\text{days}$, and $\tau=28\,\text{days}$.

The estimation is done from the [data for cumulative incidence](....) corresponding to $N-S(t)$, where the population size is fixed at $N=10^6$, using the linear noise approximation as described in [Zimmer and Sahle (2014)](http://ieeexplore.ieee.org/abstract/document/7277317/) and [Zimmer (2015)](https://www.sciencedirect.com/science/article/pii/S0025556415001698). The objective function is handled by [`sdeparams`](..........).

## Usage

```bash
$python app.py
```

Upon opening the resulting link, you should see this:
<html xmlns="http://www.w3.org/1999/xhtml">
    <body>
        <div id="content">
            <iframe width="1200px" height="800px" frameborder="0" zoom="0.5" src="https://ebov-2018.herokuapp.com/" />
        </div>
    </body>
</html>

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
