# gimme-wisdom

## Requirements
```
Python 3.6.X
```

## Installation
```
% pip install -U -r requirements.txt.in
```

## Usage
```
# Run on local
% scrapy crawl yanswers -a qid=1013160720 -o yanswers.csv

# Run on scrapinghub.com (please see below for deployment)
% open https://app.scrapinghub.com/p/$PROJECT_ID/jobs
# Click "Run", Spiders: "windom", Arguments: {"qid": "1013160720"}
# Enjoy Serverless!!
```

## Deployment
```
# Login to scrapinghub.com
% shub login

# Create project on your browser (and copy PROJECT_ID)
% open https://app.scrapinghub.com/

# Deploy to scrapinghub.com to generate `scrapinghub.yaml`. But it occurs dependency error 
% shub deploy

# Generate eggs to generate `setup.py` and `requirements.txt`
% shub migrate-eggs

# Add dependencies
% cat requirements.txt.in >> requirements.txt

# Re-Deploy to scrapinghub.com including dependencies
% shub deploy
```
