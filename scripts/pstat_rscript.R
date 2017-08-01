#!/usr/bin/env Rscript

require(PathoStat)
args =  commandArgs(trailingOnly=TRUE)
options(shiny.port=as.numeric(args[1]))
runPathoStat()
