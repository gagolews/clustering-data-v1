Generator: <https://github.com/gagolews/clustering-data-v1/blob/master/.devel/generate_gKmg.py>

Author: Marek Gagolewski (http://www.gagolewski.com)
Copyleft 2020
Licensed under the Creative Commons Attribution 4.0 International License

Each dataset consists of 2,048 observations from
two equisized Gaussian clusters in $d=1, 2, \dots, 128$ dimensions
(the components are sampled independently from a normal distribution).

They can be considered a modified version of Gaussian `G2`-sets from
<https://cs.joensuu.fi/sipu/datasets/>, but with variances
dependent on datasets' dimensionalities, i.e., $s\sqrt{d/2}$
for different *s*. This makes these new problems more difficult than
their original counterparts.
The 1-dimensional datasets as well as those of very low and very
high variances should probably be discarded.

It is well-known that such a data distribution
(multivariate normal with independent components)
is subject to the so-called curse of dimensionality,
leading to some weird behaviour for high *d*.

We suggest that these datasets should be studied separately
from other batteries, because they are too plentiful.
Also, *parametric* algorithms that *specialise* in detecting
Gaussian blobs (*k*-means, expectation-maximisation (EM)
for Gaussian mixtures) will naturally perform better thereon than
the non-parametric approaches.
