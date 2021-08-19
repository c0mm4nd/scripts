# BitcoinLabels

Download/Crawl the bitcoin address labels from the walletexplorer.com

## Usage

no deps required

```python
python ./crawler.py  
```

With proxy
```
# if bash
export https_proxy=http://127.0.0.1:8080
# if powershell
$Env:https_proxy = "http://127.0.0.1:8080"
# if cmd
set https_proxy=http://127.0.0.1:8080

python ./crawler.py
```

Fetch with known id
```python
python ./crawler.py 3 # fetching 'Poloniex.com'
```

Fetch with known name
```python
python ./crawler.py Poloniex.com # fetching 'Poloniex.com'
```
