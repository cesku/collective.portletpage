#!/bin/sh

# ./bootstrap (5.2) (py2|py3)
rm -r ./lib ./include ./local ./bin
virtualenv --clear .
./bin/pip install -U pip
./bin/pip install -r requirements-$1.txt
ln -s plone-$1.x-$2.cfg buildout.cfg
./bin/buildout