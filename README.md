# [A Framework for Benchmarking Clustering Algorithms](https://clustering-benchmarks.gagolewski.com)
## Benchmark Suite Version 1 (with updates)

The aim of this project is to **aggregate, polish, and standardise the
existing clustering benchmark batteries** referred to across the machine
learning and data mining literature, and to introduce **new datasets**
of different dimensionalities, sizes, and cluster types.

This repository is part of the
[**Framework for Benchmarking Clustering Algorithms**](https://clustering-benchmarks.gagolewski.com).
It hosts the datasets from version 1 of the benchmark suite.

Refer to <https://clustering-benchmarks.gagolewski.com>
for a detailed description, file format specification,
example Python/R/MATLAB code, datasets explorer,
and literature references.



**Editor/Maintainer**:
[Marek Gagolewski](https://www.gagolewski.com).


**How to Cite**: Please cite the following paper which describes
the overall benchmarking methodology:

> Gagolewski M., A framework for benchmarking clustering algorithms,
*SoftwareX* **20**, 2022, 101270, <https://clustering-benchmarks.gagolewski.com>,
DOI: [10.1016/j.softx.2022.101270](https://doi.org/10.1016/j.softx.2022.101270).

Additionally, mention the exact version of this benchmark suite
(see *Changelog* below for version information):

> Gagolewski M. et al. (Eds.), *A benchmark suite for clustering algorithms:
Version 1.1.0*, 2022,
<https://github.com/gagolews/clustering-data-v1/releases/tag/v1.1.0>,
DOI: [10.5281/zenodo.7088171](https://doi.org/10.5281/zenodo.7088171).


The datasets are provided **solely for research purposes**,
unless stated otherwise. Please cite the literature references mentioned
in the corresponding dataset description files in any publications
that make use of these.




## Changelog

The datasets and the reference labels included in this suite
are versioned. This ensures reproducibility.

See <https://github.com/gagolews/clustering-data-v1/releases/> for
downloadable snapshots.


###  1.1.0 (2022-09-17)

-   Each battery is now equipped with a README.txt file.

-   New label vectors:
    wut/x2.labels1,
    wut/x3.labels1.

-   Prettified (slightly) label vectors:
    graves/fuzzyx.labels[1-4],
    graves/parabolic.labels1.

-   Deleted now redundant label vectors:
    graves/fuzzyx.labels5.

-   The historical snapshot of this release is available at
    DOI: [10.5281/zenodo.7088171](https://doi.org/10.5281/zenodo.7088171).


###  1.0.1 (2022-09-10)

-   Updated dataset description files, e.g., fixed broken links.

-   The code and the data repositories were separated; see
    <https://github.com/gagolews/clustering-benchmarks> and
    <https://github.com/gagolews/clustering-data-v1>.

-   The project's homepage has been created. It is available at
    <https://clustering-benchmarks.gagolewski.com>.

-   The historical snapshot of this release is available at
    DOI: [10.5281/zenodo.7066690](https://doi.org/10.5281/zenodo.7066690).


###  1.0.0 (2020-05-08)

-   Datasets in the 1st (v1.0.0) version of the benchmark
    battery are now frozen.

-   The historical snapshot of this release is available at
    DOI: [10.5281/zenodo.3815066](https://doi.org/10.5281/zenodo.3815066).


###  0.0.0 (2015-12-29)

-   Version 0 of the benchmark suite consists of the datasets
    studied in: Gagolewski M., Bartoszuk M., Cena A.,
    Genie: A new, fast, and outlier-resistant hierarchical
    clustering algorithm, *Information Sciences* **363**, 2016, pp. 8–23,
    DOI: [10.1016/j.ins.2016.05.003](https://doi.org/10.1016/j.ins.2016.05.003).
    The datasets have been archived at
    <https://github.com/gagolews/clustering-data-v0>.


## See Also

<https://clustering-benchmarks.gagolewski.com> gives a detailed description
of the whole framework for benchmarking clustering algorithms.

It also mentions where to find raw and aggregated results generated
by many clustering methods when run on the datasets from this repository.
