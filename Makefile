OUTDIR := ~/Documents/Covid-19/covid_facebook_mobility/data/Facebook_Data #output directory

COLDATASETS := colocation_datsets.csv #Target colocation datasets
MOBDATASETS := mobility_datsets.csv #Target mobility datasets

pull_colocation:
	python pull_colocation.py ${COLDATASETS} ${OUTDIR}

pull_mobility:	
	python pull_mobility.py ${MOBDATASETS} ${OUTDIR}

test:
	python -m unittest discover