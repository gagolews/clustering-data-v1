#!/bin/bash

# Copyleft (C) 2018-2025, Marek Gagolewski <https://www.gagolewski.com>

# please run from within the repo's root folder

batteries="fcps graves other sipu uci wut mnist h2mg g2mg"
for b in $batteries; do
    ./.devel/catalogue_generate.py $b
    #pandoc .catalogue/$b.md --to html -o .catalogue/$b.html
done
