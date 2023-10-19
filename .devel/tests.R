#!/usr/bin/env Rscript

# Unit tests for the Clustering Datasets and their Catalogue
#
# Copyleft (C) 2018-2023, Marek Gagolewski <https://www.gagolewski.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


library("stringi")
options(stringsAsFactors=FALSE)


test <- function(metadata)
{
    data_file <- file.path(metadata$battery,
        stri_paste(metadata$dataset, ".data.gz"))
    labels_file <- file.path(metadata$battery,
        stri_paste(metadata$dataset, ".", metadata$labels, ".gz"))
    cat(labels_file, "...\n")

    X       <- read.table(data_file)
    labels  <- as.integer(read.table(labels_file)[,1])

    stopifnot(nrow(X) == metadata$n)
    stopifnot(ncol(X) == metadata$d)
    stopifnot(max(labels) == metadata$k)
}


metadata <- do.call(
    rbind,
    lapply(
        list.files(".catalogue/", pattern="\\.csv$", full.names=TRUE),
        read.csv
    )
)

for (b in unique(metadata$battery)) {
    p <- file.path(b, "README.txt")
    cat(p, "...\n")
    stopifnot(file.exists(p))
}

for (i in seq_len(nrow(metadata)))
    test(metadata[i,])


cat("OK.\n")
