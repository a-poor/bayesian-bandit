# bayesian-bandit

_created by Austin Poor_

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/a-poor/bayesian-bandit/master?filepath=bayes-bandit.ipynb&urlpath=lab)
[![NBViewer](https://img.shields.io/badge/render-nbviewer-orange)](https://nbviewer.jupyter.org/github/a-poor/bayesian-bandit/blob/master/bayes-bandit.ipynb#)

Using [`pystan`](https://mc-stan.org/) to approach a simplified version of the [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit), where the goal is to use bayesian modeling to predict the probability of success for an unknown process.

The notebook [bayes-bandit.ipynb](./bayes-bandit.ipynb) has the analysis code and the file [bandit.py](./bandit.py) has a 1-armed-bandit class used by the notebook.


## Run the Code

### Binder

To run the notebook using Binder, click the badge above or use [this link](https://mybinder.org/v2/gh/a-poor/bayesian-bandit/master?filepath=bayes-bandit.ipynb&urlpath=lab). 

### Docker

There's an included [docker-compose file](./docker-compose.yml), for running the notebook in a container, which can be run with the command:

```bash
$ docker-compose up
```

