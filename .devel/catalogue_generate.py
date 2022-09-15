#!/usr/bin/env python3

"""Generates the Catalogue of Clustering Datasets

Copyleft (C) 2018-2022, Marek Gagolewski <https://www.gagolewski.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import os
import glob
import re
import sys
import genieclust
from natsort import natsorted
import shutil

#################################################################################
# Global options

plt.style.use("seaborn")  # overall plot style

_colours = [  # the "R4" palette
    "#000000", "#DF536B", "#61D04F", "#2297E6",
    "#28E2E5", "#CD0BBC", "#F5C710", "#999999"
]

_linestyles = [
    "solid", "dashed", "dashdot", "dotted"
]

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    # each plotted line will have a different plotting style
    color=_colours, linestyle=_linestyles*2
)
plt.rcParams["patch.facecolor"] = _colours[0]

np.random.seed(123)  # initialise the pseudorandom number generator

plt.rcParams.update({  # further graphical parameters
    "font.size":         13,
    "font.family":       "sans-serif",
    "font.sans-serif":   ["Alegreya Sans", "Alegreya"],
    "figure.autolayout": True,
    "figure.dpi":        240,
    "figure.figsize":    (5.9375, 3.4635),
})


#################################################################################



# TODO: rewrite using clustbench.load_dataset etc.

def process(f, battery, dataset):
    """
    Processes a single dataset
    """
    X = np.loadtxt(os.path.join(battery, dataset+".data.gz"), ndmin=2)
    # X = (X-X.mean(axis=0))/X.std(axis=None, ddof=1) # scale all axes proportionally

    print('## %s/%s (n=%d, d=%d) <a name="%s"></a>\n' % (
        battery, dataset, X.shape[0], X.shape[1], dataset
    ), file=f)

    readme = os.path.join(battery, dataset+".txt")
    shutil.copyfile(readme, os.path.join(".catalogue", readme))
    with open(readme, "r") as readme_file:
        for readme_line in readme_file.read().split("\n"):
            print("    "+readme_line, file=f)
    print("\n", file=f)

    label_names = sorted(
        [
            re.search(r'\.(labels[0-9]+)\.gz$', name).group(1)
            for name in glob.glob(dataset+".labels*.gz", root_dir=battery)
        ])

    labels = [
        np.loadtxt(
            os.path.join(battery, "%s.%s.gz" % (dataset, name)),
            dtype='int'
        ) for name in label_names
    ]
    label_counts = [np.bincount(ll) for ll in labels]
    noise_counts = [c[0] for c in label_counts]
    #have_noise = [bool(c[0]) for c in label_counts]
    label_counts = [c[1:] for c in label_counts]
    true_K = [len(c) for c in label_counts]
    #true_G = [genieclust.inequity.gini_index(c) for c in label_counts]

    for i in range(len(label_names)):
        print("#### `%s`\n\ntrue_k=%2d, noise=%5d\n\nlabel_counts=%r\n" % (
                label_names[i], true_K[i], noise_counts[i],
                label_counts[i].tolist()
            ),
            file=f
        )

        if X.shape[1] not in [1, 2, 3]:
            print('> **(preview generation suppressed)**\n\n', file=f)
            continue

        plt.figure()
        ax = plt.subplot(111, projection=None if X.shape[1] in [1, 2] else '3d')


        if X.shape[1] == 2:
            genieclust.plots.plot_scatter(X, labels=labels[i]-1, alpha=0.5)
            plt.axis("equal")

        elif X.shape[1] == 1:
            X_aug = np.insert(X, 1, np.random.randn(len(X))*(X.max()-X.min())*1e-6, axis=1)
            genieclust.plots.plot_scatter(X_aug, labels=labels[i]-1, alpha=0.5)
            plt.axis("equal")

        elif X.shape[1] == 3:
            ax.scatter(
                X[:, 0],
                X[:, 1],
                c=np.array(genieclust.plots.col, dtype=object)[
                    (labels[i]-1) % len(genieclust.plots.col)
                ],
                alpha=0.5
            )
            #plt.axis("equal")

        plt.title("%s/%s.%s (n=%d, d=%d, k=%d%s)" % (
            battery,
            dataset,
            label_names[i],
            X.shape[0],
            X.shape[1],
            true_K[i],
            ", noise=%d" % noise_counts[i] if noise_counts[i] else ""
        ))

        _fig_name = os.path.join(battery, "%s.%s.png" % (dataset, label_names[i]))
        _fig_path = os.path.join(".catalogue", _fig_name)
        plt.savefig(_fig_path, format='png',
                    #transparent=True,
                    bbox_inches='tight',
                    #dpi=150
        )
        plt.close()

        print("![](%s)\n" % (_fig_name), file=f)

        # with open(_fig_path, "rb") as img:
            # encoded_string = base64.b64encode(img.read()).decode("US-ASCII")
        #print("<img src='data:image/png;base64,"+encoded_string+"' alt='%s.%s' />\n"%(dataset, label_names[i]), file=f)




    print("\n\n", file=f)

    return [
        dict(
            battery=battery,
            dataset=dataset,
            n=X.shape[0],
            d=X.shape[1],
            labels=label_names[i],
            k=true_K[i],
            noise=noise_counts[i]
        )
        for i in range(len(label_names))
    ]


###############################################################################
# Do the job.

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: %s benchmark_folder" % sys.argv[0])

    battery = sys.argv[1]
    if not os.path.isdir(battery):
        raise Exception("`%s` is not a directory")

    fnames = glob.glob("*.data.gz", root_dir=battery)
    datasets = natsorted(
        [re.search(r"(.*)\.data\.gz$", name)[1] for name in fnames]
    )

    image_folder = os.path.join(".catalogue", battery)
    if not os.path.isdir(image_folder): os.mkdir(image_folder)

    output = os.path.join(".catalogue", "%s.md" % battery)
    f = open(output, "w")

    print("The **[Framework for Benchmarking Clustering Algorithms](https://clustering-benchmarks.gagolewski.com)", file=f)
    print("is authored/edited/maintained by [Marek Gagolewski](https://www.gagolewski.com)**\n", file=f)
    print("\n"+("-"*80)+"\n", file=f)

    print("**Datasets**\n", file=f)
    for dataset in datasets:
        print("* [%s/%s](#%s)" % (
            battery, dataset, dataset
        ), file=f)
    print("\n"+("-"*80)+"\n", file=f)

    metadata = []
    for dataset in datasets:
        print("Generating %s/%s..." % (battery, dataset))
        metadata += process(f, battery, dataset)
    f.close()

    metadata_file = os.path.join(".catalogue", "%s.csv" % battery)
    pd.DataFrame(metadata).\
        loc[:, ["battery", "dataset", "n", "d", "labels", "k", "noise"]].\
        to_csv(metadata_file, header=True, index=False)

    print("Done.")
