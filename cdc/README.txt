Synthetic benchmark datasets from:
Peng, D., Gui, Z., Wang, D. et al, Clustering by measuring local direction
centrality for data with heterogeneous density and weak connectivity,
Nature Communications 13, 5455, 2022, DOI:10.1038/s41467-022-33136-9.

Source: https://github.com/ZPGuiGroupWhu/ClusteringDirectionCentrality/tree/master/Toolkit/Synthetic%20Data%20Analysis

The project was released under the Apache 2.0 License.


Exclusions:

* DS2 - a version of compound
* DS3 - a version of chameleon_t5_8k (no background noise, but with added ring)
* DS5 - exactly the aggregation dataset
* DS9 - a version of chameleon_t5_8k (no background noise)
* DS14 - a version of DS10 (no background noise), similar to jain


```r
# conversion:
process_original_file <- function(fname) {
    df <- read.table(fname)

    x <- df[,-NCOL(df)]
    y <- df[,NCOL(df),drop=FALSE]

    cat(sprintf("%s n=%d d=%d k=%d\n", fname, NROW(x), NCOL(x), max(y)))
    stopifnot(min(y) == 1 || min(y) == 0)
    stopifnot(NCOL(x) >= 2)
    stopifnot(NROW(x) == NROW(y))

    f <- gzfile(stringi::stri_replace_first_regex(fname, ".txt$", ".data.gz"), open="w")
    write.table(x, f, col.names=FALSE, row.names=FALSE, sep=" ", quote=FALSE)
    close(f)

    f <- gzfile(stringi::stri_replace_first_regex(fname, ".txt$", ".labels0.gz"), open="w")
    write.table(y, f, col.names=FALSE, row.names=FALSE, sep=" ", quote=FALSE)
    close(f)

    writeLines(con=fname, c(
        "Synthetic benchmark dataset from",
        "Peng, D., Gui, Z., Wang, D. et al., Clustering by measuring local direction centrality for data with heterogeneous density and weak connectivity, Nature Communications 13, 5455, 2022, DOI:10.1038/s41467-022-33136-9.",
        "",
        "Source: https://github.com/ZPGuiGroupWhu/ClusteringDirectionCentrality/tree/master/Toolkit/Synthetic%20Data%20Analysis",
        "",
        "The project is released under the Apache 2.0 License.",
        "",
        "`0` denotes the noise class (if present)."
    ))
}
for (f in list.files(pattern="DS.*\\.txt")) process_original_file(f)
```
